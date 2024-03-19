import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Window:
    def __init__(self, winSize):
        pygame.display.set_mode(winSize, DOUBLEBUF | OPENGL)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        glViewport(0, 0, winSize[0], winSize[1])

        self.winSize = winSize
