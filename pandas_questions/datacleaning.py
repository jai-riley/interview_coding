"""
Given a DataFrame with missing values and duplicates, write code to:
    Drop rows with missing target values.
    Fill missing numeric features with the column mean.
    Remove duplicates.
"""

import pandas as pd

file = "/Users/jairiley/Desktop/interview_coding/pandas_questions/test.csv"
df = pd.read_csv(file)

# (a) Drop rows with missing target values.
df = df[df["one"] == 1]

# (b) Fill missing numeric features with the column mean.
df.fillna(df.mean(), inplace=True)

# (c) Remove duplicates.
df.drop_duplicates(inplace=True)

print(df)