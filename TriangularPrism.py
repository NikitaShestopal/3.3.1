from Triangle import Triangle

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, height):
        super().__init__(a, b, c)
        self.height = height

    def dimension(self):
        return '3D'

    def volume(self):
        return super().square() * self.height