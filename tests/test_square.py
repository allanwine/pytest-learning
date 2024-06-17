import pytest
import src.shape as shape

@pytest.mark.parametrize("side_length, expected_area", [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
def test_multiple_square_areas(side_length, expected_area):
    assert shape.Square(side_length).area() == expected_area

@pytest.mark.parametrize("side_length, expected_perimeter", [(1, 4), (2, 8), (3, 12), (4, 16), (5, 20)])
def test_multiple_square_perimeters(side_length, expected_perimeter):
    assert shape.Square(side_length).perimeter() == expected_perimeter
