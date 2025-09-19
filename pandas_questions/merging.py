"""
Merge two DataFrames:
customers(customer_id, name)
transactions(transaction_id, customer_id, amount)
Return a DataFrame of total spend per customer.
"""
import pandas as pd

file_cus = "/Users/jairiley/Desktop/interview_coding/pandas_questions/customers.csv"
df_customer = pd.read_csv(file_cus)

file_trans = "/Users/jairiley/Desktop/interview_coding/pandas_questions/transactions.csv"
df_transactions = pd.read_csv(file_trans)

df = pd.merge(df_customer, df_transactions, on=["customer_id"])
df.drop(columns=['transaction_id'], inplace=True)
totals = df.groupby("name")["amount"].sum()
totals.rename(columns={"amount": "total_spend"}, inplace=True)

