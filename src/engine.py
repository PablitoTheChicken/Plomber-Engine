import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

VBO = 0
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, 9*4, (GLfloat*9)(1, 0, 0, 0, 1, 0, 0, 0, 1), GL_STATIC_DRAW)

Shader = glCreateShader(GL_VERTEX_SHADER)
glShaderSource(Shader, "")
glCompileShader(Shader)

class Engine:
    def __init__(self):
        clock = pygame.time.Clock()
        pygame.display.init()
        
        self.clock = clock
        self.deltaTime = 0
        
    def createWindow(self, winSize):
        pygame.display.set_mode(winSize, DOUBLEBUF|OPENGL)
        glViewport(0, 0, winSize[0], winSize[1])
        self.winSize = winSize
        
    def render(self, deltaTime):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        
        pygame.display.flip()
    
    def physicsStep(self, deltaTime):
        pass
    
    def registerEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.close()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    self.close()
        
    def tick(self, fps):
        self.deltaTime = self.clock.tick(fps)/1000
        return self.deltaTime
    
    def close(self):
        pygame.quit()
        quit()