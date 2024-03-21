import math
import glm

quad_vertices = glm.array(
    glm.float32,
    0.5,
    0.5,
    0.0,
    1.0,
    0.0,
    0.0,
    1.0,
    1.0,
    0.5,
    -0.5,
    0.0,
    0.0,
    1.0,
    0.0,
    1.0,
    0.0,
    -0.5,
    -0.5,
    0.0,
    0.0,
    0.0,
    1.0,
    0.0,
    0.0,
    -0.5,
    0.5,
    0.0,
    1.0,
    1.0,
    0.0,
    0.0,
    1.0,
)

quad_indices = glm.array(
    glm.uint32, 0, 1, 3, 1, 2, 3  # first triangle  # second triangle
)


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
