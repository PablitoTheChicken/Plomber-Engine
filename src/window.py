import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Window:
    def __init__(self, winSize):
        pygame.display.set_mode(winSize, DOUBLEBUF | OPENGL)

        glViewport(0, 0, winSize[0], winSize[1])

        self.winSize = winSize
