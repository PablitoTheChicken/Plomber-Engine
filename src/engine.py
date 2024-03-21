import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import glm

from gameObject import GameObject
from window import Window
from camera import Camera
from texture import Texture
from shader import ShaderProgram, Shader
from meshFile import MeshFile

light_positions = [
    glm.vec3(0.0, 1.0, 2.0),
]

engine = None


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
        self.shaderProgram = shaderProgram

        self.gameObjects = []
        self.window = window
        self.clock = clock
        self.deltaTime = 0
        self.running = True
        self.camera = camera

        self.lastMouseX = 0
        self.lastMouseY = 0

        global engine
        engine = self

    def createGameObject(self):
        gameObject = GameObject()
        self.gameObjects.append(gameObject)
        return gameObject

    def render(self, deltaTime):
        if self.running == False:
            return

        self.shaderProgram.use()
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        model = glm.mat4(1.0)
        modelLoc = glGetUniformLocation(self.shaderProgram.program, "model")
        glUniformMatrix4fv(modelLoc, 1, GL_FALSE, glm.value_ptr(model))

        # Camera
        view = self.camera.getViewMatrix()
        projection = self.camera.getProjectionMatrix(self.window.winSize)
        self.shaderProgram.setUniformMatrix4fv("view", view)
        self.shaderProgram.setUniformMatrix4fv("projection", projection)
        self.shaderProgram.setUniformVec3f("viewPos", self.camera.position)

        for gameObject in self.gameObjects:
            gameObject.update(deltaTime)

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

            if not self.isMovingCamera:
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
