import pytest
import src.shape as shape

@pytest.fixture
def test_universal_circle():
    return shape.Circle(5)

@pytest.fixture
def test_universal_rectangle():
    return shape.Rectangle(5, 10.5)

@pytest.fixture
def test_universal_square():
    return shape.Square(7)