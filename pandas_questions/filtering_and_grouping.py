"""
Filtering and Grouping
You’re given sales data with columns: date, store_id, product_id, sales.
Find the top 3 products by total sales across all stores.
Compute average daily sales per store.
"""
import pandas as pd

file = "/Users/jairiley/Desktop/interview_coding/pandas_questions/sales_data.csv"
df = pd.read_csv(file)

# (a) Find the top 3 products by total sales across all stores.
top_products = df.groupby("product_id")["sales"].sum().nlargest(3)

# (b) Compute average daily sales per store.
average_sales = df.groupby("store_id")["sales"].mean()
