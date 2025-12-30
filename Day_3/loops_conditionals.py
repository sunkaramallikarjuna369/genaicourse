#!/usr/bin/env python3
"""Day 3: Loops & Conditionals - If/else, for, while"""

print("\n=== Day 3: Loops and Conditionals ===")

# Conditional Statements
age = 25
if age >= 18:
    print(f"{age} is an adult")
else:
    print(f"{age} is a minor")

# For loop
print("\nCounting 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# While loop
count = 0
while count < 3:
    print(f"While loop: {count}")
    count += 1

# List iteration
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

print("\n=== Completed ===")
