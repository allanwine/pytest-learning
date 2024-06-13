import pytest
import src.main as main

def test_add():
    assert main.add(1, 2) == 3
    assert main.add(0, 0) == 0
    assert main.add(-1, -1) == -2

def test_subtract():
    assert main.subtract(1, 2) == -1
    assert main.subtract(0, 0) == 0
    assert main.subtract(-1, -1) == 0

def test_multiply():
    assert main.multiply(1, 2) == 2
    assert main.multiply(0, 0) == 0
    assert main.multiply(-1, -1) == 1

def test_divide():
    assert main.divide(1, 2) == 0.5
    with pytest.raises(ZeroDivisionError):
        main.divide(0, 0)
    assert main.divide(-1, -1) == 1

def test_newDivide():
    assert main.newDivide(1, 2) == 0.5
    with pytest.raises(ValueError):
        main.newDivide(1, 0)
    assert main.newDivide(-1, -1) == 1
