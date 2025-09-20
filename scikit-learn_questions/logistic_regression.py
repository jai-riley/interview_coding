"""
Train/Test Split + Model Training
Given a dataset X, y, split into train/test and train a logistic regression. Report accuracy on the test set.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


X = pd.read_csv("/Users/jairiley/Desktop/interview_coding/scikit-learn_questions/X.csv")
y = pd.read_csv("/Users/jairiley/Desktop/interview_coding/scikit-learn_questions/y.csv")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_pred))