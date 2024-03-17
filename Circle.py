from Figure import Figure
from math import pi

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return '2D'

    def perimeter(self):
        return 2 * pi * self.r

    def square(self):
        return pi * self.r ** 2