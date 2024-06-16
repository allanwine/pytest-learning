import pytest
import time
import src.calculator_functions as calculator_functions

def test_add():
    assert calculator_functions.add(1, 2) == 3
    assert calculator_functions.add(0, 0) == 0
    assert calculator_functions.add(-1, -1) == -2

def test_add_string():
    with pytest.raises(TypeError):
        calculator_functions.add(1, "2")

def test_subtract():
    assert calculator_functions.subtract(1, 2) == -1
    assert calculator_functions.subtract(0, 0) == 0
    assert calculator_functions.subtract(-1, -1) == 0

def test_subtract_string():
    with pytest.raises(TypeError):
        calculator_functions.subtract(1, "2")

def test_multiply():
    assert calculator_functions.multiply(1, 2) == 2
    assert calculator_functions.multiply(0, 0) == 0
    assert calculator_functions.multiply(-1, -1) == 1

def test_multiply_string():
    with pytest.raises(TypeError):
        calculator_functions.multiply(1, "2")

def test_divide():
    assert calculator_functions.divide(1, 2) == 0.5
    with pytest.raises(ZeroDivisionError):
        calculator_functions.divide(0, 0)
    assert calculator_functions.divide(-1, -1) == 1

def test_divide_string():
    with pytest.raises(TypeError):
        calculator_functions.divide(1, "2")

def test_new_divide():
    assert calculator_functions.new_divide(1, 2) == 0.5
    with pytest.raises(ValueError):
        calculator_functions.new_divide(1, 0)
    assert calculator_functions.new_divide(-1, -1) == 1

def test_new_divide_string():
    with pytest.raises(TypeError):
        calculator_functions.new_divide(1, "2")

# run pytest -m slow to run slow tests
@pytest.mark.slow
def test_slow_divide():
    start = time.time()
    time.sleep(1)
    assert calculator_functions.divide(1, 2) == 0.5
    end = time.time()
    assert end - start >= 0.5

def test_skip_add():
    pytest.skip("Skipping the test")
    assert calculator_functions.add(1, 2) == 4

@pytest.mark.skip(reason="This will always fail")
def test_skip_subtract():
    assert calculator_functions.subtract(1, 2) == -1

@pytest.mark.xfail(reason="This will always fail")
def test_xfail_multiply():
    assert calculator_functions.multiply(1, 2) == 3