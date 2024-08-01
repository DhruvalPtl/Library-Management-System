# test_calculator.py
import pytest
from calculator import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(2, 0) == 2
    assert subtract(2, -2) == 4

def test_add_invalid_type():
    with pytest.raises(TypeError):
        add("one", "two")