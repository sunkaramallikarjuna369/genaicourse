#!/usr/bin/env python3
"""Day 12: Machine Learning with scikit-learn"""
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)
print(f"Accuracy: {score}")

# Predict
prediction = model.predict([[5.1, 3.5, 1.4, 0.2]])
print(f"Prediction: {prediction}")
