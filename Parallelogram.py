from Figure import Figure


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def dimension(self):
        return '2D'

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h