import pygame
import random
from abc import ABC, abstractmethod


# Base abstract class for shapes
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, surface):
        pass


# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = random.randint(10, 50)
        self.color = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))

    # Draw circle on the given surface
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = random.randint(10, 100)
        self.height = random.randint(10, 100)
        self.color = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))

    # Draw rectangle on given surface
    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.width, self.height))


# ShapeFactory class for creating shape instances
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, x, y):
        if shape_type == "Circle":
            return Circle(x, y)
        elif shape_type == "Rectangle":
            return Rectangle(x, y)
        else:
            raise ValueError("Invalid Shape type")
