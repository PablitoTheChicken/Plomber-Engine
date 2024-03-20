import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import glm

from shapes.cube import *

quad = Cube()

class RenderPipeline:
    def __init__(self, shaderProgram):
        VBO = glGenBuffers(1)
        VAO = glGenVertexArrays(1)
        EBO = glGenBuffers(1)

        self.shaderProgram = shaderProgram
        shaderProgram.use()

        glBindVertexArray(VAO)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)

        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, cube_vertices.nbytes, cube_vertices.ptr, GL_STATIC_DRAW)

        #glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        #glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        #glBufferData(GL_ELEMENT_ARRAY_BUFFER, cube_indices.nbytes, cube_indices.ptr, GL_STATIC_DRAW)

        # position attribute
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), None)
        glEnableVertexAttribArray(0)
        # normal attribute
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), ctypes.c_void_p(3 * glm.sizeof(glm.float32)))
        glEnableVertexAttribArray(1)
        # texture coord attribute
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), ctypes.c_void_p(6 * glm.sizeof(glm.float32)))
        glEnableVertexAttribArray(2)

        model = glm.mat4(1.0)
        modelLoc = glGetUniformLocation(shaderProgram.program, "model")

        glUniformMatrix4fv(modelLoc, 1, GL_FALSE, glm.value_ptr(model))
        glUniform1i(glGetUniformLocation(shaderProgram.program, "texture1"), 0)

        self.VBO = VBO
        self.VAO = VAO
        self.EBO = EBO

    def cleanup(self):
        glDeleteBuffers(1, self.VBO)
        glDeleteVertexArrays(1, self.VAO)
