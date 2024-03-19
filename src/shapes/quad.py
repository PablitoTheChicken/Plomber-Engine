import math

quad_vertices = [
    0.5,
    0.5,
    0.0,
    1.0,
    0.0,
    0.0,
    1.0,
    1.0,  # top right
    0.5,
    -0.5,
    0.0,
    0.0,
    1.0,
    0.0,
    1.0,
    0.0,  # bottom right
    -0.5,
    -0.5,
    0.0,
    0.0,
    0.0,
    1.0,
    0.0,
    0.0,  # bottom left
    -0.5,
    0.5,
    0.0,
    1.0,
    1.0,
    0.0,
    0.0,
    1.0,  # top left
]

quad_indices = [0, 1, 3, 1, 2, 3]


class Quad:
    def __init__(self, width=1, height=1, rotation=0):
        self.width = width
        self.height = height
        self.vertices = quad_vertices
        self.indices = quad_indices

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
