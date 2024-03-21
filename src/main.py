from engine import *

from components.MeshRenderer import MeshRenderer
from components.PointLight import PointLight


def main():
    engine = Engine(winSize=(1400, 900))

    test1 = engine.createGameObject()
    test1.addComponent(MeshRenderer("src/assets/nanosuit/nanosuit.obj"))

    test2 = engine.createGameObject()
    test2.position = glm.vec3(0, 3, 0)
    test2.addComponent(PointLight(position=glm.vec3(0, 3, 2)))

    test3 = engine.createGameObject()
    test3.position = glm.vec3(0, 13, 0)
    test3.addComponent(PointLight(position=glm.vec3(0, 7, 2)))

    while engine.running == True:
        deltaTime = engine.tick(144)

        pygame.display.set_caption(f"FPS: {int(1 / deltaTime)}")

        # Base Engine Loop
        engine.registerEvents()
        engine.physicsStep(deltaTime)
        engine.render(deltaTime)


if __name__ == "__main__":
    main()
