import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def mag(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f"({str(self.x)}, {str(self.y)})"
