from Figure import Figure
from math import sqrt

class Trapezoid(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def dimension(self):
        return '2D'

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        return (self.a + self.b) * self.height() / 2

    def square_surface(self):
        return None

    def square_base(self):
        return None

    def height(self):
        return sqrt(self.c ** 2 - ((self.b - self.a) ** 2) / 4)