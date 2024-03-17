from Rectangle import Rectangle

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.height = h

    def dimension(self):
        return '3D'

    def volume(self):
        return super().square() * self.height

