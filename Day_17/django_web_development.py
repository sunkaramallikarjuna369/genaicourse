#!/usr/bin/env python3
"""
Day 17: Django Web Framework
Full-featured web framework with ORM
"""

print("=== Day 17: Django Web Framework ===")

print("""
Django Key Concepts:

1. MODELS - Database models
   from django.db import models
   class Student(models.Model):
       name = models.CharField(max_length=100)
       email = models.EmailField()
       gpa = models.FloatField()

2. VIEWS - Handle requests
   from django.shortcuts import render
   from django.http import JsonResponse
   
   def student_list(request):
       students = Student.objects.all()
       return render(request, 'students.html', {'students': students})

3. URLS - Route mapping
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('students/', views.student_list, name='students'),
       path('students/<int:id>/', views.student_detail, name='detail'),
   ]

4. TEMPLATES - HTML rendering
   <!-- students.html -->
   {% for student in students %}
     <p>{{ student.name }}: {{ student.email }}</p>
   {% endfor %}

5. ADMIN PANEL - Built-in admin
   from django.contrib import admin
   admin.site.register(Student)

6. FORMS - Data validation
   from django import forms
   class StudentForm(forms.ModelForm):
       class Meta:
           model = Student
           fields = ['name', 'email', 'gpa']

7. AUTHENTICATION - User management
   from django.contrib.auth.models import User
   User.objects.create_user(username='alice', password='pass123')

8. MIDDLEWARE - Request/Response processing
   Custom middleware for authentication, logging, etc.

9. MIGRATIONS - Database schema management
   python manage.py makemigrations
   python manage.py migrate

10. DJANGO ORM - Query database
    students = Student.objects.filter(gpa__gte=3.5)
    student = Student.objects.get(id=1)
    student.delete()
""")

print("\n=== Concepts Learned ===")
print("1. Models - Define data structure")
print("2. Views - Handle HTTP requests")
print("3. URL routing - Map URLs to views")
print("4. Templates - Render HTML dynamically")
print("5. Forms - User input validation")
print("6. Admin panel - Built-in management")
print("7. ORM - Database interactions")
print("8. Authentication - User management")
print("9. Migrations - Schema versioning")
print("10. Middleware - Request processing")
