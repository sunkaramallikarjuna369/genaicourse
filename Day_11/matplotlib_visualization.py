#!/usr/bin/env python3
"""Day 11: Data Visualization with Matplotlib"""
import matplotlib.pyplot as plt
import numpy as np

# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Plot')
plt.legend()
# plt.show()

# Bar chart
categories = ['A', 'B', 'C']
values = [10, 20, 15]
plt.figure(figsize=(8, 6))
plt.bar(categories, values)
plt.title('Bar Chart')
# plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter([1,2,3,4], [1,4,2,3])
plt.title('Scatter Plot')
# plt.show()

print("Visualization complete")
