import math
import glm

triangle_vertices = glm.array(glm.float32,
         0.5,  0.5, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0,
        -0.5, -0.5, 0.0,   0.0, 1.0, 0.0,   0.0, 0.0,
        -0.5,  0.5, 0.0,   0.0, 0.0, 1.0,   0.0, 1.0
    )

triangle_indices = glm.array(glm.uint32,
        0, 1, 2
    )


class Triangle:
    def __init__(self, width=1, height=1, rotation=0):
        self.width = width
        self.height = height
        self.vertices = triangle_vertices
        self.indices = triangle_indices

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
