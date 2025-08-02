categories_schema = [
    {"name": "CategoryID", "type": "INTEGER", "pk": True},
    {"name": "CategoryName", "type": "TEXT"},
    {"name": "Description", "type": "TEXT"},
    {"name": "Picture", "type": "BLOB"},
]

customer_customer_demo_schema = [
    {"name": "CustomerID", "type": "TEXT", "pk": True},
    {"name": "CustomerTypeID", "type": "TEXT", "pk": True},
]

customer_demographics_schema = [
    {"name": "CustomerTypeID", "type": "TEXT", "pk": True},
    {"name": "CustomerDesc", "type": "TEXT"},
]

customers_schema = [
    {"name": "CustomerID", "type": "TEXT", "pk": True},
    {"name": "CompanyName", "type": "TEXT"},
    {"name": "ContactName", "type": "TEXT"},
    {"name": "ContactTitle", "type": "TEXT"},
    {"name": "Address", "type": "TEXT"},
    {"name": "City", "type": "TEXT"},
    {"name": "Region", "type": "TEXT"},
    {"name": "PostalCode", "type": "TEXT"},
    {"name": "Country", "type": "TEXT"},
    {"name": "Phone", "type": "TEXT"},
    {"name": "Fax", "type": "TEXT"},
]

employees_schema = [
    {"name": "EmployeeID", "type": "INTEGER", "pk": True},
    {"name": "LastName", "type": "TEXT"},
    {"name": "FirstName", "type": "TEXT"},
    {"name": "Title", "type": "TEXT"},
    {"name": "TitleOfCourtesy", "type": "TEXT"},
    {"name": "BirthDate", "type": "DATE"},
    {"name": "HireDate", "type": "DATE"},
    {"name": "Address", "type": "TEXT"},
    {"name": "City", "type": "TEXT"},
    {"name": "Region", "type": "TEXT"},
    {"name": "PostalCode", "type": "TEXT"},
    {"name": "Country", "type": "TEXT"},
    {"name": "HomePhone", "type": "TEXT"},
    {"name": "Extension", "type": "TEXT"},
    {"name": "Photo", "type": "BLOB"},
    {"name": "Notes", "type": "TEXT"},
    {"name": "ReportsTo", "type": "INTEGER"},
    {"name": "PhotoPath", "type": "TEXT"},
]

employee_territories_schema = [
    {"name": "EmployeeID", "type": "INTEGER", "pk": True},
    {"name": "TerritoryID", "type": "TEXT", "pk": True},
]

order_details_schema = [
    {"name": "OrderID", "type": "INTEGER", "pk": True},
    {"name": "ProductID", "type": "INTEGER", "pk": True},
    {"name": "UnitPrice", "type": "NUMERIC", "default": 0},
    {"name": "Quantity", "type": "INTEGER", "default": 1},
    {"name": "Discount", "type": "REAL", "default": 0},
]

orders_schema = [
    {"name": "OrderID", "type": "INTEGER", "pk": True},
    {"name": "CustomerID", "type": "TEXT"},
    {"name": "EmployeeID", "type": "INTEGER"},
    {"name": "OrderDate", "type": "DATETIME"},
    {"name": "RequiredDate", "type": "DATETIME"},
    {"name": "ShippedDate", "type": "DATETIME"},
    {"name": "ShipVia", "type": "INTEGER"},
    {"name": "Freight", "type": "NUMERIC", "default": 0},
    {"name": "ShipName", "type": "TEXT"},
    {"name": "ShipAddress", "type": "TEXT"},
    {"name": "ShipCity", "type": "TEXT"},
    {"name": "ShipRegion", "type": "TEXT"},
    {"name": "ShipPostalCode", "type": "TEXT"},
    {"name": "ShipCountry", "type": "TEXT"},
]

products_schema = [
    {"name": "ProductID", "type": "INTEGER", "pk": True},
    {"name": "ProductName", "type": "TEXT"},
    {"name": "SupplierID", "type": "INTEGER"},
    {"name": "CategoryID", "type": "INTEGER"},
    {"name": "QuantityPerUnit", "type": "TEXT"},
    {"name": "UnitPrice", "type": "NUMERIC", "default": 0},
    {"name": "UnitsInStock", "type": "INTEGER", "default": 0},
    {"name": "UnitsOnOrder", "type": "INTEGER", "default": 0},
    {"name": "ReorderLevel", "type": "INTEGER", "default": 0},
    {"name": "Discontinued", "type": "TEXT", "default": "'0'"},
]

regions_schema = [
    {"name": "RegionID", "type": "INTEGER", "pk": True},
    {"name": "RegionDescription", "type": "TEXT"},
]

shippers_schema = [
    {"name": "ShipperID", "type": "INTEGER", "pk": True},
    {"name": "CompanyName", "type": "TEXT"},
    {"name": "Phone", "type": "TEXT"},
]

suppliers_schema = [
    {"name": "SupplierID", "type": "INTEGER", "pk": True},
    {"name": "CompanyName", "type": "TEXT"},
    {"name": "ContactName", "type": "TEXT"},
    {"name": "ContactTitle", "type": "TEXT"},
    {"name": "Address", "type": "TEXT"},
    {"name": "City", "type": "TEXT"},
    {"name": "Region", "type": "TEXT"},
    {"name": "PostalCode", "type": "TEXT"},
    {"name": "Country", "type": "TEXT"},
    {"name": "Phone", "type": "TEXT"},
    {"name": "Fax", "type": "TEXT"},
    {"name": "HomePage", "type": "TEXT"},
]

territories_schema = [
    {"name": "TerritoryID", "type": "TEXT", "pk": True},
    {"name": "TerritoryDescription", "type": "TEXT"},
    {"name": "RegionID", "type": "INTEGER"},
]
