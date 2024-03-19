import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import cv2

from shapes.quad import quad_vertices_texturecoords, quad_indices


class RenderPipeline:
    def __init__(self):
        VBO = glGenBuffers(1)
        VAO = glGenVertexArrays(1)
        EBO = glGenBuffers(1)

        glBindVertexArray(VAO)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(
            GL_ARRAY_BUFFER,
            (GLfloat * len(quad_vertices_texturecoords))(*quad_vertices_texturecoords),
            GL_STATIC_DRAW,
        )

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(
            GL_ELEMENT_ARRAY_BUFFER,
            (GLint * len(quad_indices))(*quad_indices),
            GL_STATIC_DRAW,
        )

        textureData = cv2.imread("src/assets/container.jpg")

        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGB,
            512,
            512,
            0,
            GL_RGB,
            GL_UNSIGNED_BYTE,
            textureData,
        )
        glGenerateMipmap(GL_TEXTURE_2D)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), None)
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(
            1, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), 3 * sizeof(GLfloat)
        )
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        self.VBO = VBO
        self.VAO = VAO
        self.EBO = EBO

    def cleanup(self):
        glDeleteBuffers(1, VBO)
        glDeleteVertexArrays(1, VAO)
