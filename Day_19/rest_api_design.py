#!/usr/bin/env python3
"""
Day 19: REST API Design Principles
Understanding RESTful API best practices and design patterns
"""

from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

print("=== Day 19: REST API Design ===")

# In-memory database
students = {
    1: {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'grade': 'A', 'created_at': '2024-01-01'},
    2: {'id': 2, 'name': 'Bob', 'email': 'bob@example.com', 'grade': 'B', 'created_at': '2024-01-02'},
    3: {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com', 'grade': 'C', 'created_at': '2024-01-03'}
}

# ===== REST API Endpoints =====

@app.route('/api/v1/students', methods=['GET'])
def get_all_students():
    """GET - Retrieve all students
    HTTP 200: Success
    """
    try:
        return jsonify({
            'status': 'success',
            'data': list(students.values()),
            'count': len(students)
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/v1/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """GET - Retrieve specific student
    HTTP 200: Found
    HTTP 404: Not Found
    """
    if student_id not in students:
        return jsonify({
            'status': 'error',
            'message': f'Student {student_id} not found'
        }), 404
    
    return jsonify({
        'status': 'success',
        'data': students[student_id]
    }), 200

@app.route('/api/v1/students', methods=['POST'])
def create_student():
    """POST - Create new student
    HTTP 201: Created
    HTTP 400: Bad Request
    HTTP 409: Conflict (Duplicate email)
    """
    try:
        data = request.get_json()
        
        # Validation
        if not data or not all(k in data for k in ['name', 'email', 'grade']):
            return jsonify({
                'status': 'error',
                'message': 'Missing required fields: name, email, grade'
            }), 400
        
        # Check duplicate email
        for student in students.values():
            if student['email'] == data['email']:
                return jsonify({
                    'status': 'error',
                    'message': 'Email already exists'
                }), 409
        
        # Create new student
        new_id = max(students.keys()) + 1 if students else 1
        new_student = {
            'id': new_id,
            'name': data['name'],
            'email': data['email'],
            'grade': data['grade'],
            'created_at': datetime.now().isoformat()
        }
        students[new_id] = new_student
        
        return jsonify({
            'status': 'success',
            'message': 'Student created',
            'data': new_student
        }), 201
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/v1/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """PUT - Update entire student record
    HTTP 200: Updated
    HTTP 404: Not Found
    """
    if student_id not in students:
        return jsonify({
            'status': 'error',
            'message': f'Student {student_id} not found'
        }), 404
    
    try:
        data = request.get_json()
        students[student_id].update(data)
        
        return jsonify({
            'status': 'success',
            'message': 'Student updated',
            'data': students[student_id]
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/v1/students/<int:student_id>', methods=['PATCH'])
def partial_update_student(student_id):
    """PATCH - Partial update of student record
    HTTP 200: Updated
    HTTP 404: Not Found
    """
    if student_id not in students:
        return jsonify({
            'status': 'error',
            'message': f'Student {student_id} not found'
        }), 404
    
    try:
        data = request.get_json()
        # Only update provided fields
        for key, value in data.items():
            if key in students[student_id]:
                students[student_id][key] = value
        
        return jsonify({
            'status': 'success',
            'message': 'Student partially updated',
            'data': students[student_id]
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/v1/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """DELETE - Remove student record
    HTTP 204: No Content
    HTTP 404: Not Found
    """
    if student_id not in students:
        return jsonify({
            'status': 'error',
            'message': f'Student {student_id} not found'
        }), 404
    
    deleted = students.pop(student_id)
    return jsonify({
        'status': 'success',
        'message': 'Student deleted',
        'data': deleted
    }), 200

# ===== Error Handling =====

@app.errorhandler(404)
def not_found(error):
    """Handle 404 Not Found"""
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found',
        'code': 404
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 Method Not Allowed"""
    return jsonify({
        'status': 'error',
        'message': 'Method not allowed',
        'code': 405
    }), 405

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 Internal Server Error"""
    return jsonify({
        'status': 'error',
        'message': 'Internal server error',
        'code': 500
    }), 500

if __name__ == '__main__':
    print("""
=== REST API Design Best Practices ===""")
    print("""
1. VERSION YOUR API
   - Use /api/v1/ prefix for version control
   - Allows backward compatibility

2. USE PROPER HTTP METHODS
   - GET: Retrieve data (safe, idempotent)
   - POST: Create new resource
   - PUT: Replace entire resource (idempotent)
   - PATCH: Partial update
   - DELETE: Remove resource

3. CONSISTENT NAMING
   - Use nouns for resources: /api/v1/students
   - Use plural forms for collections
   - Use hyphens in multi-word names: /api/v1/student-reports

4. PROPER HTTP STATUS CODES
   - 200 OK: Request successful
   - 201 Created: Resource created
   - 204 No Content: Successful, no response body
   - 400 Bad Request: Invalid request
   - 404 Not Found: Resource not found
   - 409 Conflict: Resource conflict
   - 500 Internal Server Error: Server error

5. REQUEST/RESPONSE STRUCTURE
   - Send JSON in request body (Content-Type: application/json)
   - Include status field in responses
   - Wrap data in 'data' field
   - Include helpful error messages

6. PAGINATION FOR LARGE DATASETS
   - Use ?page=1&limit=10 query parameters
   - Return total count

7. FILTERING & SORTING
   - ?filter=grade:A (filter)
   - ?sort=created_at (sort)

8. AUTHENTICATION
   - Use Bearer tokens or API keys
   - Include in Authorization header

9. RATE LIMITING
   - Prevent abuse
   - Return X-Rate-Limit headers

10. DOCUMENTATION
    - Use Swagger/OpenAPI
    - Clear endpoint documentation
    """)
    # Uncomment to run: app.run(debug=True)
