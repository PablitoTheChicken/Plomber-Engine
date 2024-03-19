import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from window import Window


class Engine:
    def __init__(self):
        clock = pygame.time.Clock()
        pygame.display.init()

        self.window = None
        self.clock = clock
        self.deltaTime = 0
        self.running = True

    def createWindow(self, winSize):
        newWindow = Window(winSize)
        self.window = newWindow
        return newWindow

    def bindPipeline(self, pipeline):
        self.pipeline = pipeline

    def render(self, deltaTime):
        if self.running == False:
            return

        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.pipeline.texture)

        glBindVertexArray(self.pipeline.VAO)
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)

        pygame.display.flip()

    def physicsStep(self, deltaTime):
        if self.running == False:
            return

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
        self.deltaTime = self.clock.tick(fps) / 1000
        return self.deltaTime

    def close(self):
        pygame.quit()
        self.running = False
