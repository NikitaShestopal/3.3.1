from Figure import Figure
from math import pi

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def volume(self):
        return (4 / 3) * pi * self.r ** 3