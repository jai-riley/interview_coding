"""Cross-validation
Perform 5-fold cross-validation on a decision tree model and print the mean accuracy.
"""
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

X = pd.read_csv("/Users/jairiley/Desktop/interview_coding/scikit-learn_questions/X.csv")
y = pd.read_csv("/Users/jairiley/Desktop/interview_coding/scikit-learn_questions/y.csv").squeeze() 

dt_model = DecisionTreeClassifier(random_state=42)
scores = cross_val_score(dt_model, X, y, cv=5, scoring="accuracy")
print(scores.mean())