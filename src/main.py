import math

from engine import *

from components.MeshRenderer import MeshRenderer
from components.PointLight import PointLight


def main():
    engine = Engine(winSize=(1400, 900))

    nanosuit = engine.createGameObject()
    nanosuit.addComponent(MeshRenderer("src/assets/nanosuit/nanosuit.obj"))
    nanosuit.scale = glm.vec3(0.8, 0.8, 0.8)

    backpack = engine.createGameObject()
    backpack.addComponent(MeshRenderer("src/assets/backpack/backpack.obj"))
    backpack.position = glm.vec3(5, 0, 0)
    backpack.rotation = glm.vec3(-30, 10, 15)

    light1 = engine.createGameObject()
    light1.position = glm.vec3(0, 3, 2)
    light1.addComponent(PointLight(color=glm.vec3(0, 1, 0)))

    light2 = engine.createGameObject()
    light2.position = glm.vec3(0, 7, 2)
    light2.addComponent(PointLight())

    light3 = engine.createGameObject()
    light3.position = glm.vec3(0, 11, 2)
    light3.addComponent(PointLight(color=glm.vec3(1, 0, 0)))

    elapsed = 0
    while engine.running == True:
        deltaTime = engine.tick(144)
        elapsed += deltaTime

        pygame.display.set_caption(f"FPS: {int(1 / deltaTime)}")

        light1.position = glm.vec3(math.sin(elapsed * 3) * 2, 3, 2)
        light2.position = glm.vec3(-math.sin(elapsed * 3) * 2, 7, 2)

        # Base Engine Loop
        engine.registerEvents()
        engine.physicsStep(deltaTime)
        engine.render(deltaTime)


if __name__ == "__main__":
    main()
