from Figure import Figure
from math import sqrt

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def dimension(self):
        return '2D'

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        s = self.perimeter() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))