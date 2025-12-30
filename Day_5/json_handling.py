#!/usr/bin/env python3
"""Day 5: JSON - The Language of APIs"""

import json

# Create a dictionary (like JSON)
student = {
    "name": "Rahul",
    "age": 20,
    "subjects": ["Math", "Physics", "AI"]
}

# Convert to JSON string
json_string = json.dumps(student)
print(f"JSON string: {json_string}")

# Convert back to Python
data = json.loads(json_string)
print(f"Name: {data['name']}")
print(f"Subjects: {data['subjects']}")

# Write to file
with open('data.json', 'w') as f:
    json.dump(student, f)

# Read from file
with open('data.json', 'r') as f:
    loaded = json.load(f)
    print(f"Loaded from file: {loaded}")
