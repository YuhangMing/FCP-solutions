# square.py

def square(x):
    """Returns the square of x"""
    return x * x

def test_square():
    assert square(0) == 0
    assert square(2) == 4
    assert square(-2) == 4