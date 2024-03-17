from Rectangle import Rectangle

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.height = h

    def dimension(self):
        return '3D'

    def volume(self):
        return ( 1 /3) * super().square() * self.height