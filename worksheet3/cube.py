# cube.py

def cube(x):
    """Returns the cube of x"""
    # return 0  # <--- This obviously doesn't work correctly
    return x**3

def test_square():
    assert cube(0) == 0
    assert cube(2) == 8
    # assert cube(-2) == 8
    assert cube(-2) == -8