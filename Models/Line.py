from Models.Point import Point


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Line({self.a}, {self.b})"

    @classmethod
    def from_coordinates(cls, x1, y1, x2, y2):
        return cls(Point(x1, y1), Point(x2, y2))

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b