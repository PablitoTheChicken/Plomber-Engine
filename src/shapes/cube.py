import math
import glm

cube_vertices = glm.array(glm.float32,
            0.5,  0.5,  0.5,  1.0, 0.0, 0.0,  1.0, 1.0,
            0.5,  0.5, -0.5,  0.0, 1.0, 0.0,  1.0, 0.0,
            0.5, -0.5, -0.5,  0.0, 0.0, 1.0,  0.0, 0.0,
            0.5, -0.5,  0.5,  1.0, 1.0, 0.0,  0.0, 1.0,
            -0.5,  0.5,  0.5,  1.0, 0.0, 0.0,  1.0, 1.0,
            -0.5,  0.5, -0.5,  0.0, 1.0, 0.0,  1.0, 0.0,
            -0.5, -0.5, -0.5,  0.0, 0.0, 1.0,  0.0, 0.0,
            -0.5, -0.5,  0.5,  1.0, 1.0, 0.0,  0.0, 1.0
        )

cube_indices = glm.array(glm.uint32,
        0, 1, 3, # first triangle
        1, 2, 3, # second triangle
        4, 5, 7, # third triangle
        5, 6, 7, # fourth triangle
        0, 1, 5, # fifth triangle
        0, 5, 4, # sixth triangle
        1, 2, 6, # seventh triangle
        1, 6, 5, # eighth triangle
        2, 3, 7, # ninth triangle
        2, 7, 6, # tenth triangle
        0, 3, 7, # eleventh triangle
        0, 7, 4  # twelfth triangle
    )

class Cube:
    def __init__(self, width=1, height=1, rotation=0):
        self.width = width
        self.height = height
        self.vertices = cube_vertices
        self.indices = cube_indices

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
