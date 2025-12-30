#!/usr/bin/env python3
"""
Day 1: Welcome & Environment Setup
Topic: What is Generative AI and setting up Python

Learning Objectives:
- Understand what Generative AI is
- Set up Python environment
- Write and run first Python program
"""

# Simple exercise: Create a program that introduces GenAI

print("=" * 50)
print("Welcome to the 50-Day GenAI Course!")
print("=" * 50)

# Part 1: Print Information
print("\nWhat is Generative AI?")
print("-" * 50)
print("Generative AI refers to AI models that can generate new")
print("content like text, images, code, and more based on prompts.")
print()
print("Examples:")
print("  - ChatGPT: Generates text responses")
print("  - DALL-E: Generates images from descriptions")
print("  - GitHub Copilot: Generates code suggestions")

# Part 2: Variables and Data Types
print("\n" + "=" * 50)
print("Python Basics: Variables")
print("=" * 50)

name = "Student"
age = 20
course_duration_days = 50
is_excited = True

print(f"\nName: {name}")
print(f"Age: {age}")
print(f"Course Duration: {course_duration_days} days")
print(f"Are you excited? {is_excited}")

# Part 3: Simple Calculation
print("\n" + "=" * 50)
print("Time Commitment Calculation")
print("=" * 50)

hours_per_day = 1
total_hours = course_duration_days * hours_per_day

print(f"\nHours per day: {hours_per_day}")
print(f"Days in course: {course_duration_days}")
print(f"Total hours: {total_hours}")
print(f"\nBy the end of this course, you will have {total_hours} hours")
print("of focused learning in Generative AI!")

# Part 4: Simple Function
print("\n" + "=" * 50)
print("Creating Your First Function")
print("=" * 50)

def greet_student(student_name):
    """A simple greeting function"""
    return f"Hello {student_name}! Welcome to GenAI learning journey."

greeting = greet_student(name)
print(f"\n{greeting}")

# Part 5: Summary
print("\n" + "=" * 50)
print("Day 1 Summary")
print("=" * 50)
print("\nToday you learned:")
print("  1. What Generative AI is")
print("  2. How to use Python variables")
print("  3. How to perform basic calculations")
print("  4. How to create and use functions")
print("  5. How to use Python's print() function")

print("\n" + "=" * 50)
print("Ready for Day 2! Continue learning.")
print("=" * 50)
