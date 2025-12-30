#!/usr/bin/env python3
"""
Day 8: SQL Basics with Python
Learning to work with databases using SQL
"""

import sqlite3
from typing import List, Dict, Any

# 1. Connect to SQLite Database
def connect_database(db_name='students.db'):
    """Create connection to SQLite database"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None, None

# 2. Create Table
def create_table(cursor, conn):
    """Create a students table"""
    sql = '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade REAL,
        enrollment_date DATE
    )
    '''
    try:
        cursor.execute(sql)
        conn.commit()
        print("Table created successfully")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# 3. Insert Data
def insert_student(cursor, conn, name, age, grade):
    """Insert a single student record"""
    sql = 'INSERT INTO students (name, age, grade) VALUES (?, ?, ?)'
    try:
        cursor.execute(sql, (name, age, grade))
        conn.commit()
        print(f"Student {name} inserted successfully")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

# 4. Insert Multiple Records
def insert_multiple_students(cursor, conn, students):
    """Insert multiple student records"""
    sql = 'INSERT INTO students (name, age, grade) VALUES (?, ?, ?)'
    try:
        cursor.executemany(sql, students)
        conn.commit()
        print(f"Inserted {len(students)} records")
    except sqlite3.Error as e:
        print(f"Error: {e}")

# 5. Select/Query Data
def select_all_students(cursor) -> List[Dict[str, Any]]:
    """Retrieve all students"""
    cursor.execute('SELECT * FROM students')
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    return [dict(zip(columns, row)) for row in rows]

# 6. Select with Conditions
def select_by_grade(cursor, min_grade):
    """Select students with grade >= min_grade"""
    sql = 'SELECT * FROM students WHERE grade >= ?'
    cursor.execute(sql, (min_grade,))
    return cursor.fetchall()

# 7. Update Record
def update_student_grade(cursor, conn, student_id, new_grade):
    """Update student's grade"""
    sql = 'UPDATE students SET grade = ? WHERE id = ?'
    try:
        cursor.execute(sql, (new_grade, student_id))
        conn.commit()
        print(f"Updated student {student_id} grade to {new_grade}")
    except sqlite3.Error as e:
        print(f"Error updating: {e}")

# 8. Delete Record
def delete_student(cursor, conn, student_id):
    """Delete a student record"""
    sql = 'DELETE FROM students WHERE id = ?'
    try:
        cursor.execute(sql, (student_id,))
        conn.commit()
        print(f"Deleted student {student_id}")
    except sqlite3.Error as e:
        print(f"Error deleting: {e}")

# 9. Aggregation Functions
def get_statistics(cursor):
    """Get grade statistics"""
    stats = {}
    
    # Average grade
    cursor.execute('SELECT AVG(grade) FROM students')
    stats['average'] = cursor.fetchone()[0]
    
    # Maximum grade
    cursor.execute('SELECT MAX(grade) FROM students')
    stats['maximum'] = cursor.fetchone()[0]
    
    # Minimum grade
    cursor.execute('SELECT MIN(grade) FROM students')
    stats['minimum'] = cursor.fetchone()[0]
    
    # Count
    cursor.execute('SELECT COUNT(*) FROM students')
    stats['count'] = cursor.fetchone()[0]
    
    return stats

# 10. Transactions
def transaction_example(cursor, conn):
    """Example of database transaction"""
    try:
        cursor.execute('BEGIN')
        cursor.execute('UPDATE students SET grade = grade + 5')
        cursor.execute('UPDATE students SET grade = 100 WHERE grade > 100')
        conn.commit()
        print("Transaction completed")
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed: {e}")

if __name__ == "__main__":
    print("=== Day 8: SQL Basics ===")
    
    # Connect to database
    conn, cursor = connect_database()
    
    if cursor:
        # Create table
        create_table(cursor, conn)
        
        # Insert sample data
        students = [
            ('Alice', 20, 85.5),
            ('Bob', 21, 90.0),
            ('Charlie', 19, 78.5)
        ]
        insert_multiple_students(cursor, conn, students)
        
        # Query data
        all_students = select_all_students(cursor)
        print(f"\nAll students: {len(all_students)}")
        
        # Get statistics
        stats = get_statistics(cursor)
        print(f"Statistics: {stats}")
        
        # Close connection
        conn.close()
