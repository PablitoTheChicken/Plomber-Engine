import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from PIL import Image

from shapes.quad import *

quad = Quad()


class RenderPipeline:
    def __init__(self, shaderProgram):
        VBO = glGenBuffers(1)
        VAO = glGenVertexArrays(1)
        EBO = glGenBuffers(1)

        self.shaderProgram = shaderProgram

        glBindVertexArray(VAO)

        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(
            GL_ARRAY_BUFFER,
            (GLfloat * len(quad.vertices))(*quad.vertices),
            GL_STATIC_DRAW,
        )

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(
            GL_ELEMENT_ARRAY_BUFFER,
            (GLint * len(quad.indices))(*quad.indices),
            GL_STATIC_DRAW,
        )

        img = Image.open("src/assets/container.jpg")
        textureData = np.array(list(img.getdata()), np.int8)
        shaderProgram.use()

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), None)
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(
            1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), 3 * sizeof(GLfloat)
        )
        glEnableVertexAttribArray(1)

        glVertexAttribPointer(
            2, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), 6 * sizeof(GLfloat)
        )
        glEnableVertexAttribArray(2)

        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGB,
            img.width,
            img.height,
            0,
            GL_RGB,
            GL_UNSIGNED_BYTE,
            textureData,
        )
        glGenerateMipmap(GL_TEXTURE_2D)

        glUniform1i(glGetUniformLocation(shaderProgram.program, "texture1"), 0)

        self.texture = texture
        self.VBO = VBO
        self.VAO = VAO
        self.EBO = EBO

    def cleanup(self):
        glDeleteBuffers(1, VBO)
        glDeleteVertexArrays(1, VAO)
