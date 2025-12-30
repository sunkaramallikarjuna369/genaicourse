# Day 27: Performance Testing
import time
def slow_function():
    time.sleep(1)
    return 'done'
def test_performance():
    start = time.time()
    result = slow_function()
    duration = time.time() - start
    assert duration < 2, 'Too slow'
    assert result == 'done'
