#!/usr/bin/env python3
"""
Day 16: Flask Web Framework
Building a simple web application
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

print("=== Day 16: Flask Web Framework ===")

# In-memory database
students = [
    {'id': 1, 'name': 'Alice', 'grade': 'A'},
    {'id': 2, 'name': 'Bob', 'grade': 'B'},
]

# Route 1: Home page
@app.route('/')
def home():
    """Home page route"""
    return 'Welcome to Flask! Hello World'

# Route 2: Get all students (API endpoint)
@app.route('/api/students', methods=['GET'])
def get_students():
    """Return all students as JSON"""
    return jsonify(students)

# Route 3: Get single student
@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Get student by ID"""
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({'error': 'Student not found'}), 404

# Route 4: Create new student
@app.route('/api/students', methods=['POST'])
def create_student():
    """Create new student"""
    data = request.get_json()
    new_student = {
        'id': len(students) + 1,
        'name': data.get('name'),
        'grade': data.get('grade')
    }
    students.append(new_student)
    return jsonify(new_student), 201

# Route 5: Update student
@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """Update student details"""
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        data = request.get_json()
        student.update(data)
        return jsonify(student)
    return jsonify({'error': 'Student not found'}), 404

# Route 6: Delete student
@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete student"""
    global students
    students = [s for s in students if s['id'] != student_id]
    return jsonify({'message': 'Student deleted'})

# Error handler
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

if __name__ == '__main__':
    print("\nFlask App Running!")
    print("Key Concepts:")
    print("1. @app.route() - Define URL routes")
    print("2. request - Handle incoming data")
    print("3. jsonify - Return JSON responses")
    print("4. HTTP methods - GET, POST, PUT, DELETE")
    print("5. Error handling - 404, etc.")
    print("\nAPI Endpoints:")
    print("GET    /api/students         - Get all students")
    print("GET    /api/students/<id>    - Get specific student")
    print("POST   /api/students         - Create new student")
    print("PUT    /api/students/<id>    - Update student")
    print("DELETE /api/students/<id>    - Delete student")
    
    # Uncomment to run: app.run(debug=True)
