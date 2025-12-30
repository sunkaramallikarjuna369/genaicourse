# Day 28: Security Testing
import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def test_password_hashing():
    pwd = 'mypassword'
    hashed = hash_password(pwd)
    assert len(hashed) == 64
    assert hashed != pwd
