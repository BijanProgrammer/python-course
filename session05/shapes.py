import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_surface(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"(radius: {self.radius}, perimeter: {self.calculate_perimeter()}, surface: {self.calculate_surface()})"


def add(a, b):
    return a + b


numbers = [4, 8, 15, 16, 23, 42]
