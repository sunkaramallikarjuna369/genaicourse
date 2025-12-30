#!/usr/bin/env python3
"""
Day 6: Making API Requests with Python
Learning how to fetch data from APIs using requests library
"""

import requests
import json
from typing import Dict, Any

# 1. Basic GET Request
def basic_get_request():
    """Simple GET request to fetch data from an API"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Status Code:", response.status_code)
        print("Response:", json.dumps(data, indent=2))
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

# 2. GET Request with Parameters
def get_with_parameters():
    """GET request with query parameters"""
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {
        'userId': 1,
        '_limit': 5
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Fetched {len(data)} posts")
        return data
    else:
        return None

# 3. POST Request
def post_request():
    """POST request to create new data"""
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Learning APIs with Python",
        "body": "This is a test post",
        "userId": 1
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 201:
        data = response.json()
        print("Post created successfully")
        print("New ID:", data.get('id'))
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

# 4. PUT Request (Update)
def put_request():
    """PUT request to update existing data"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {
        "title": "Updated Title",
        "body": "Updated content",
        "userId": 1
    }
    
    response = requests.put(url, json=payload)
    
    if response.status_code == 200:
        print("Post updated successfully")
        return response.json()
    else:
        return None

# 5. DELETE Request
def delete_request():
    """DELETE request to remove data"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    response = requests.delete(url)
    
    if response.status_code == 200:
        print("Post deleted successfully")
        return True
    else:
        return False

# 6. Request with Headers
def request_with_headers():
    """Making request with custom headers"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Custom)',
        'Accept': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

# 7. Timeout and Error Handling
def request_with_timeout():
    """Request with timeout and error handling"""
    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.ConnectionError:
        print("Connection error")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    return None

if __name__ == "__main__":
    print("=== Day 6: API Requests ===")
    
    print("\n1. Basic GET Request:")
    basic_get_request()
    
    print("\n2. GET with Parameters:")
    get_with_parameters()
    
    print("\n3. POST Request:")
    post_request()
    
    print("\n4. PUT Request:")
    put_request()
    
    print("\n5. DELETE Request:")
    delete_request()
    
    print("\n6. Request with Headers:")
    request_with_headers()
    
    print("\n7. Request with Timeout:")
    request_with_timeout()
