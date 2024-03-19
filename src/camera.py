import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
import glm

class Camera:
    def __init__(self) -> None:
        self.position = glm.vec3(0, 1.2, 4)
        self.front = glm.vec3(0, 0, -1)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.worldUp = glm.vec3(0, 1, 0)

        self.yaw = -90
        self.pitch = 0
        self.fov = 45

        self.updateCameraVectors()

    def getViewMatrix(self):
        return glm.lookAt(self.position, self.position + self.front, self.up)
    
    def getProjectionMatrix(self, winSize):
        return glm.perspective(glm.radians(self.fov), winSize[0] / winSize[1], 0.1, 100)
    
    def processInput(self, deltaTime):
        cameraSpeed = 2.5 * deltaTime
        if pygame.key.get_pressed()[pygame.K_w]:
            self.position += cameraSpeed * self.front
        if pygame.key.get_pressed()[pygame.K_s]:
            self.position -= cameraSpeed * self.front
        if pygame.key.get_pressed()[pygame.K_a]:
            self.position -= glm.normalize(glm.cross(self.front, self.up)) * cameraSpeed
        if pygame.key.get_pressed()[pygame.K_d]:
            self.position += glm.normalize(glm.cross(self.front, self.up)) * cameraSpeed

    def processMouseMovement(self, xoffset, yoffset, constrainPitch=True):
        xoffset *= 0.1
        yoffset *= 0.1

        self.yaw += xoffset
        self.pitch += yoffset

        if constrainPitch:
            if self.pitch > 89:
                self.pitch = 89
            if self.pitch < -89:
                self.pitch = -89

        self.updateCameraVectors()

    def updateCameraVectors(self):
        front = glm.vec3()
        front.x = glm.cos(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch))
        front.y = glm.sin(glm.radians(self.pitch))
        front.z = glm.sin(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch))
        self.front = glm.normalize(front)

        self.right = glm.normalize(glm.cross(self.front, self.worldUp))
        self.up = glm.normalize(glm.cross(self.right, self.front))