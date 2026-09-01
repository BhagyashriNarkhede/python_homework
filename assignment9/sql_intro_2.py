#task 5

import sqlite3
import pandas as pd

# Connect to the lesson database
conn = sqlite3.connect("../db/lesson.db")

# Read data from the database into a DataFrame
query = """
SELECT line_items.line_item_id,
       line_items.quantity,
       line_items.product_id,
       products.product_name,
       products.price
FROM line_items
JOIN products
ON line_items.product_id = products.product_id
"""

df = pd.read_sql_query(query, conn)

# Step 3: Print the first 5 rows
print("First 5 rows:")
print(df.head())


# Step 4: Add total column
df["total"] = df["quantity"] * df["price"]

print("\nFirst 5 rows with total:")
print(df.head())


# Step 5: Group by product_id
df = df.groupby("product_id").agg(
    {
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    }
)

print("\nFirst 5 rows after grouping:")
print(df.head())


# Step 6: Sort by product_name
df = df.sort_values("product_name")

print("\nSorted DataFrame:")
print(df.head())


# Step 7: Write the DataFrame to CSV
df.to_csv("order_summary.csv")

print("\norder_summary.csv created successfully!")


# Close the database connection
conn.close()

