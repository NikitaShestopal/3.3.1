from Circle import Circle

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.height = h

    def dimension(self):
        return '3D'

    def volume(self):
        return (1 /3) * super().square() * self.height