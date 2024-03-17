from Triangle import Triangle

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimension(self):
        return '3D'

    def volume(self):
        base_area = super().square()
        if base_area is None:
            return None
        return (1 / 3) * base_area * self.h