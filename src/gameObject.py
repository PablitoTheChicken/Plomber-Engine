import glm


class GameObject:
    def __init__(self, position=glm.vec3(0.0, 0.0, 0.0), scale=glm.vec3(1.0, 1.0, 1.0)):
        self.position = position
        self.scale = scale
        self.rotation = glm.vec3(0.0, 0.0, 0.0)
        self.components = []

    def setPosition(self, position):
        self.position = position

    def setScale(self, scale):
        self.scale = scale

    def addComponent(self, component):
        self.components.append(component)

    def getComponent(self, componentType):
        for component in self.components:
            if isinstance(component, componentType):
                return component
        return None

    def update(self, deltaTime):
        for component in self.components:
            component.update(deltaTime)
