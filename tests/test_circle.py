import pytest
import math
import src.shape as shape

class Test_Circle:
    def setup_method(self, method):
        self.circle = shape.Circle(5)
        print(f"Setup method called for {method}")

    def teardown_method(self, method):
        print(f"Teardown method called for {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == round(math.pi * self.circle.radius ** 2, 2)

    def test_perimeter(self):
        assert self.circle.perimeter() == round(2 * 3.14 * self.circle.radius, 2)

    def test_area_type(self):
        assert type(self.circle.area()) == float

    def test_perimeter_type(self):
        assert type(self.circle.perimeter()) == float
