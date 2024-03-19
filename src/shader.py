import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Shader:
    def __init__(self, shaderType, shaderPath):
        shader = glCreateShader(shaderType)
        shaderSource = open(shaderPath, "r").read()
        glShaderSource(shader, shaderSource)
        glCompileShader(shader)
        self.shader = shader


class ShaderProgram:
    def __init__(self):
        self.program = glCreateProgram()

    def attachShader(self, shader):
        glAttachShader(self.program, shader.shader)

    def link(self):
        glLinkProgram(self.program)

    def use(self):
        glUseProgram(self.program)

    def unuse(self):
        glUseProgram(0)

    def getUniformLocation(self, name):
        return glGetUniformLocation(self.program, name)

    def getAttribLocation(self, name):
        return glGetAttribLocation(self.program, name)

    def setUniform1f(self, name, value):
        glUniform1f(self.getUniformLocation(name), value)

    def setUniform1i(self, name, value):
        glUniform1i(self.getUniformLocation(name), value)

    def setUniform2f(self, name, value1, value2):
        glUniform2f(self.getUniformLocation(name), value1, value2)

    def setUniform3f(self, name, value1, value2, value3):
        glUniform3f(self.getUniformLocation(name), value1, value2, value3)

    def setUniform4f(self, name, value1, value2, value3, value4):
        glUniform4f(self.getUniformLocation(name), value1, value2, value3, value4)

    def setUniformMatrix4fv(self, name, matrix):
        glUniformMatrix4fv(self.getUniformLocation(name), 1, GL_FALSE, matrix)

    def clean(self):
        glDeleteProgram(self.program)
        self.program = None
        self.__init__()
