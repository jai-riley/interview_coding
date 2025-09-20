"""
Build a pipeline that:
    Standardizes the data.
    Trains a RandomForestClassifier.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

X = pd.read_csv("/Users/jairiley/Desktop/interview_coding/scikit-learn_questions/X.csv")
y = pd.read_csv("/Users/jairiley/Desktop/interview_coding/scikit-learn_questions/y.csv").squeeze()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("rf", RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(accuracy_score(y_test, y_pred))