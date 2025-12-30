#!/usr/bin/env python3
"""
Day 9: ORM with SQLAlchemy
Learning Object-Relational Mapping
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Create base class
Base = declarative_base()

# Define Model
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    gpa = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Student(name='{self.name}', email='{self.email}', gpa={self.gpa})>"

# Initialize database
def init_database():
    """Create database and tables"""
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)
    return engine

# Create session
def create_session(engine):
    """Create database session"""
    Session = sessionmaker(bind=engine)
    return Session()

# Add record
def add_student(session, name, email, gpa):
    """Add new student"""
    student = Student(name=name, email=email, gpa=gpa)
    session.add(student)
    session.commit()
    return student

# Query all
def get_all_students(session):
    """Get all students"""
    return session.query(Student).all()

# Query with filter
def get_students_by_gpa(session, min_gpa):
    """Get students with GPA >= min_gpa"""
    return session.query(Student).filter(Student.gpa >= min_gpa).all()

# Update
def update_student_gpa(session, student_id, new_gpa):
    """Update student GPA"""
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        student.gpa = new_gpa
        session.commit()
    return student

# Delete
def delete_student(session, student_id):
    """Delete student"""
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        session.delete(student)
        session.commit()
    return student

if __name__ == "__main__":
    print("=== Day 9: SQLAlchemy ORM ===")
    engine = init_database()
    session = create_session(engine)
    
    # Add students
    add_student(session, 'Alice', 'alice@example.com', 3.8)
    add_student(session, 'Bob', 'bob@example.com', 3.5)
    
    # Query all
    students = get_all_students(session)
    print(f"\nTotal students: {len(students)}")
