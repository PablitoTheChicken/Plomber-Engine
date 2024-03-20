import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import glm

from window import Window
from camera import Camera
from texture import Texture
from pipeline import RenderPipeline
from shader import ShaderProgram, Shader

light_positions = [
    glm.vec3(0.0, 0.0, 49.0),
    glm.vec3(0.0, 0.0, -49.0),
]

class Engine:
    def __init__(self, winSize=(800, 800)):
        clock = pygame.time.Clock()
        camera = Camera()
        pygame.display.init()

        window = Window(winSize)
        vertShader = Shader(GL_VERTEX_SHADER, "src/shaders/vert.glsl")
        fragShader = Shader(GL_FRAGMENT_SHADER, "src/shaders/frag.glsl")

        shaderProgram = ShaderProgram()
        shaderProgram.attachShader(vertShader)
        shaderProgram.attachShader(fragShader)
        shaderProgram.link()
        shaderProgram.use()

        pipeline = RenderPipeline(shaderProgram)
        self.pipeline = pipeline

        texture1 = Texture(pipeline.shaderProgram, "container.jpg")
        self.texture1 = texture1

        self.window = window
        self.clock = clock
        self.deltaTime = 0
        self.running = True
        self.camera = camera

    def render(self, deltaTime):
        if self.running == False:
            return

        self.pipeline.shaderProgram.use()
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Binding
        glBindVertexArray(self.pipeline.VAO)

        # Texture
        self.texture1.use()

        # Camera
        view = self.camera.getViewMatrix()

        projection = self.camera.getProjectionMatrix(self.window.winSize)
        self.pipeline.shaderProgram.setUniformMatrix4fv("view", view)
        self.pipeline.shaderProgram.setUniformMatrix4fv("projection", projection)

        # Lighting
        for i in range(len(light_positions)):
            self.pipeline.shaderProgram.setUniformVec3f(f"lightPositions[{i}]", light_positions[i])
            self.pipeline.shaderProgram.setUniformVec3f(f"lightColors[{i}]", glm.vec3(1.0, 1.0, 1.0))

        # Draw
        #glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)
        glDrawArrays(GL_TRIANGLES, 0, 36)

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

        self.camera.processInput(self.deltaTime)

    def tick(self, fps):
        self.deltaTime = self.clock.tick(fps) / 1000
        return self.deltaTime

    def close(self):
        pygame.quit()
        self.running = False
