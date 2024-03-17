from Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dimension(self):
        return '2D'

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b