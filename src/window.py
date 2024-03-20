import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Window:
    def __init__(self, winSize=(800, 800)):
        pygame.display.set_mode(winSize, DOUBLEBUF | OPENGL)

        glViewport(0, 0, winSize[0], winSize[1])
        glEnable(GL_DEPTH_TEST)

        self.winSize = winSize
