from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import google.generativeai as genai
import pandas as pd
import re
from schemas import products_schema, orders_schema, order_details_schema, suppliers_schema, shippers_schema, regions_schema, employees_schema, employee_territories_schema

# Configure Gemini API key
genai.configure(api_key="AIzaSyC8c46LdP6WramexJpJoE-jXe_CxCuDVDc")

# Initialize Gemini model (use Gemini 1.5 Flash)
model = genai.GenerativeModel("gemini-2.5-pro")

app = Flask(__name__)
CORS(app)

# Path to your Northwind SQLite DB
DB_PATH = 'db/northwind.db'

# ...existing code...

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json['question']

    schemas_dict = {
        "products_schema": products_schema,
        "orders_schema": orders_schema,
        "order_details_schema": order_details_schema,
        "suppliers_schema": suppliers_schema,
        "shippers_schema": shippers_schema,
        "regions_schema": regions_schema,
        "employees_schema": employees_schema,
        "employee_territories_schema": employee_territories_schema,
    }
    schemas_list = list(schemas_dict.keys())

    topic_prompt = f"""
The following are the tables in the Northwind SQLite database: {', '.join(schemas_list)}.

You are an expert SQL query generator. Given a user question, choose the correct schema from the list above and provide the schema name.

User question: {user_query}
"""
    

    try:
        schema_response = model.generate_content(topic_prompt)
        # Clean and extract schema name(s)
        schema_text = schema_response.text.strip()
        # Remove markdown formatting, quotes, brackets
        schema_text = re.sub(r'[`"\[\]]', '', schema_text)
        # Split by comma or whitespace, filter valid schema names
        possible_names = [name for name in re.split(r'[,\s]+', schema_text) if name in schemas_list]
        if not possible_names:
            return jsonify({"error": f"Invalid schema name returned: {schema_text}"}), 400
        schema_name = possible_names[0]  # Always use the first valid schema name
        chart_type = model.generate_content(
            f"Determine the chart type for the question give bar or line or pie: {user_query} give only the chart type"
        ).text.strip()
        print(f"Schema name returned: {schema_name}, Chart type: {chart_type}")
    except Exception as e:
        return jsonify({"error": f"Gemini API error (schema selection): {e}"}), 500

    if schema_name not in schemas_list:
        return jsonify({"error": f"Invalid schema name returned: {schema_name}"}), 400

    schema_def = schemas_dict[schema_name]
    prompt = f"""
    Schema:
    {schema_def}

    Use the exact table and column names from the schema above.
    Write ONLY a valid SQL query (no explanation, no markdown formatting, no triple backticks) to answer this user question:
    {user_query}
    """
    try:
        sql_response = model.generate_content(prompt)
    except Exception as e:
        return jsonify({"error": f"Gemini API error (SQL generation): {e}"}), 500

    if not hasattr(sql_response, 'text') or sql_response.text is None:
        return jsonify({"error": "Gemini API did not return SQL.", "sql": ""}), 500

    sql_query = sql_response.text.strip()
    print(f"Generated SQL: {sql_query}")

    # Clean SQL if wrapped in ```sql ... ```
    if sql_query.startswith("```sql"):
        sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

    # Run the SQL query on the local SQLite DB
    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql_query(sql_query, conn)
    except Exception as e:
        return jsonify({"error": f"SQL execution failed: {e}", "sql": sql_query}), 400
    finally:
        conn.close()

    # Generate Summary
    summary_prompt = f"Summarize this data in 1-2 sentences:\n{df.head().to_markdown()}"
    summary_response = model.generate_content(summary_prompt)
    summary = summary_response.text.strip() if hasattr(summary_response, 'text') else ""

    # --- Chart type logic ---
    ''' chart_type = "bar"
    if "list" in user_query.lower() and len(df.columns) == 2 and df.shape[0] <= 10:
        chart_type = "pie"
    elif "trend" in user_query.lower() or "over" in user_query.lower() or "year" in user_query.lower():
        chart_type = "line" '''

    return jsonify({
        'sql': sql_query,
        'data': df.to_dict(orient='records'),
        'columns': list(df.columns),
        'summary': summary,
        'chartType': chart_type

    })

# ...existing code...

if __name__ == '__main__':
    app.run(debug=True)
