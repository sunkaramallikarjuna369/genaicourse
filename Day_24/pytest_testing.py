"""Day 24: Pytest Unit Testing"""
import pytest
from typing import List

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.parametrize("a,b,expected", [(2,3,5), (0,0,0), (-1,1,0)])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
