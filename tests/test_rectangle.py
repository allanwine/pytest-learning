import pytest
import src.shape as shape

@pytest.fixture
def test_rectangle():
    return shape.Rectangle(5, 10.5)

@pytest.fixture
def second_test_rectangle():
    return shape.Rectangle(3, 27)

def test_area(test_rectangle):
    assert test_rectangle.area() == 52.5

def test_perimeter(test_rectangle):
    assert test_rectangle.perimeter() == 31

def test_area_type(test_rectangle):
    assert type(test_rectangle.area()) == float

def test_perimeter_type(test_rectangle):
    assert type(test_rectangle.perimeter()) == float

def test_equal(test_rectangle, test_universal_rectangle):
    assert test_rectangle == test_universal_rectangle

def test_not_equal(test_rectangle, second_test_rectangle):
    assert test_rectangle != second_test_rectangle
