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
from meshFile import MeshFile

light_positions = [
    glm.vec3(0.0, 1.0, 2.0),
]

class Engine:
    def __init__(self, winSize=(800, 800)):
        pygame.display.init()
        clock = pygame.time.Clock()

        window = Window(winSize)
        camera = Camera()
        
        vertShader = Shader(GL_VERTEX_SHADER, "src/shaders/vert.glsl")
        fragShader = Shader(GL_FRAGMENT_SHADER, "src/shaders/frag.glsl")

        shaderProgram = ShaderProgram()
        shaderProgram.attachShader(vertShader)
        shaderProgram.attachShader(fragShader)
        shaderProgram.link()
        glUseProgram(0)

        pipeline = RenderPipeline(shaderProgram)
        self.pipeline = pipeline

        texture1 = Texture(pipeline.shaderProgram, "container.jpg")
        self.texture1 = texture1

        self.meshFileText = MeshFile("src/assets/nanosuit/nanosuit.obj")

        self.window = window
        self.clock = clock
        self.deltaTime = 0
        self.running = True
        self.camera = camera

        self.lastMouseX = 0
        self.lastMouseY = 0

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
        model = glm.mat4(1.0)
        modelLoc = glGetUniformLocation(self.pipeline.shaderProgram.program, "model")

        glUniformMatrix4fv(modelLoc, 1, GL_FALSE, glm.value_ptr(model))
        glUniform1i(glGetUniformLocation(self.pipeline.shaderProgram.program, "texture1"), 0)

        # Camera
        view = self.camera.getViewMatrix()
        projection = self.camera.getProjectionMatrix(self.window.winSize)
        self.pipeline.shaderProgram.setUniformMatrix4fv("view", view)
        self.pipeline.shaderProgram.setUniformMatrix4fv("projection", projection)
        self.pipeline.shaderProgram.setUniformVec3f("viewPos", self.camera.position)
        self.pipeline.shaderProgram.setUniform1i("material.diffuse", 0)
        self.pipeline.shaderProgram.setUniform1i("material.specular", 1)
        self.pipeline.shaderProgram.setUniform1f("material.shininess", 32.0)

        # Lighting
        for i in range(len(light_positions)):
            self.pipeline.shaderProgram.setUniformVec3f("pointLights[0].position", light_positions[0])
            self.pipeline.shaderProgram.setUniformVec3f("pointLights[0].ambient", glm.vec3(0.05, 0.05, 0.05))
            self.pipeline.shaderProgram.setUniformVec3f("pointLights[0].diffuse", glm.vec3(0.8, 0.8, 0.8))
            self.pipeline.shaderProgram.setUniformVec3f("pointLights[0].specular", glm.vec3(1.0, 1.0, 1.0))
            self.pipeline.shaderProgram.setUniform1f("pointLights[0].constant", 1.0)
            self.pipeline.shaderProgram.setUniform1f("pointLights[0].linear", 0.09)
            self.pipeline.shaderProgram.setUniform1f("pointLights[0].quadratic", 0.032)

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

        if pygame.mouse.get_pressed()[2]:
            x, y = pygame.mouse.get_pos()

            if (not self.isMovingCamera):
                self.lastMouseX, self.lastMouseY = pygame.mouse.get_pos()

            self.isMovingCamera = True
            dx = x - self.lastMouseX
            dy = self.lastMouseY - y
            self.camera.processMouseMovement(dx, dy, self.deltaTime)
            self.lastMouseX = x
            self.lastMouseY = y
            pygame.mouse.set_visible(True)
        else:
            self.isMovingCamera = False

    def tick(self, fps):
        self.deltaTime = self.clock.tick(fps) / 1000
        return self.deltaTime

    def close(self):
        pygame.quit()
        self.running = False
