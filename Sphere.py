from Figure import Figure
from math import pi

class Sphere(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return '3D'

    def volume(self):
        return (4 / 3) * pi * self.r ** 3