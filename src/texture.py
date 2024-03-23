import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import glm
from PIL import Image
import os

LOAD_IMAGE = lambda name: Image.open(os.path.join("src/assets/", name)).transpose(
    Image.FLIP_TOP_BOTTOM
)


class Texture:
    def __init__(self, shaderProgram, texturePath):
        self.shaderProgram = shaderProgram
        self.texturePath = texturePath
        self.texture = glGenTextures(1)
        self.loadTexture()

    def loadTexture(self):
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        img = LOAD_IMAGE(self.texturePath)
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGB,
            img.width,
            img.height,
            0,
            GL_RGB,
            GL_UNSIGNED_BYTE,
            img.tobytes(),
        )
        glGenerateMipmap(GL_TEXTURE_2D)
        img.close()

    def use(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        self.shaderProgram.setUniform1i("texture1", 0)

    def cleanup(self):
        glDeleteTextures(1, self.texture)
