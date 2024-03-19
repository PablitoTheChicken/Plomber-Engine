from engine import *

def main():
    engine = Engine(winSize=(800, 800))

    while engine.running == True:
        deltaTime = engine.tick(60)

        pygame.display.set_caption(f"FPS: {int(1 / deltaTime)}")

        # Base Engine Loop
        engine.registerEvents()
        engine.physicsStep(deltaTime)
        engine.render(deltaTime)


if __name__ == "__main__":
    main()
