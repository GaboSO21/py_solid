"""
Open-closed principle
"""
import math
from abc import ABC, abstractmethod

"""
Incorrect implementation, conditional logic in area calculator
makes class open for modification, which should not be the case.
It should be open for extension, closed for modification.
"""


class AreaCalculator:
    def area(self, shape):
        if isinstance(shape, Circle):
            return math.pi * shape.radius**2
        elif isinstance(shape, Rectangle):
            return shape.width * shape.height


class Circle:
    def __init__(self, radius):
        self.radius = radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


"""
Solution:
Interface that will always have area method. Now
creating new shapes will not mean the modification of
the calculator.
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class AreaCalculator:
    def area(self, shape: Shape):
        return shape.area()
