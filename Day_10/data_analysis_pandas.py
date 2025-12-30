#!/usr/bin/env python3
"""Day 10: Data Analysis with Pandas"""
import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [20, 21, 19],
    'score': [85, 90, 78]
})

# Basic operations
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Mean score: {df['score'].mean()}")
print(f"Filtered: {df[df['score'] > 80]}")

# Group by
df.groupby('age')['score'].mean()

# Sorting
df.sort_values('score', ascending=False)

print("Pandas operations complete")
