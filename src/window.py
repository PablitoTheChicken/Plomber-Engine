import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import imgui


class Window:
    def __init__(self, winSize=(800, 800)):
        pygame.display.set_mode(winSize, DOUBLEBUF | OPENGL)
        glViewport(0, 0, winSize[0], winSize[1])
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)

        imgui.create_context()
        imgui.get_io().display_size = winSize
        imgui.get_io().fonts.get_tex_data_as_rgba32()

        self.winSize = winSize
