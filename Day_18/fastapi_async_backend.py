#!/usr/bin/env python3
"""Day 18: FastAPI - Async Web Framework"""
from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()

print("=== Day 18: FastAPI Async Backend ===")

# Define data model
class Student(BaseModel):
    id: int
    name: str
    grade: str

# In-memory database
students_db = [
    Student(id=1, name="Alice", grade="A"),
    Student(id=2, name="Bob", grade="B")
]

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to FastAPI"}

@app.get("/students")
async def get_students():
    """Get all students"""
    await asyncio.sleep(0.1)  # Simulate async operation
    return students_db

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    """Get student by ID"""
    for student in students_db:
        if student.id == student_id:
            return student
    return {"error": "Student not found"}

@app.post("/students")
async def create_student(student: Student):
    """Create new student"""
    students_db.append(student)
    return {"message": "Student created", "student": student}

@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    """Update student"""
    for i, s in enumerate(students_db):
        if s.id == student_id:
            students_db[i] = student
            return {"message": "Updated", "student": student}
    return {"error": "Not found"}

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    """Delete student"""
    global students_db
    students_db = [s for s in students_db if s.id != student_id]
    return {"message": "Deleted"}

print("""
FastAPI Key Features:
1. Async/await - Non-blocking operations
2. Pydantic models - Data validation
3. Automatic API docs - Swagger UI
4. Type hints - Better IDE support
5. CRUD operations - Create, Read, Update, Delete
6. Fast performance - One of the fastest Python frameworks
7. Easy deployment - Docker compatible
""")

# Uncomment to run: uvicorn day_18:app --reload
