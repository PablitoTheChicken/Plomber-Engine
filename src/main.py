from engine import *
from pipeline import *
from shader import *


def main():
    engine = Engine()
    engine.createWindow(winSize=(800, 800))

    vertShader = Shader(GL_VERTEX_SHADER, "src/shaders/vert.glsl")
    fragShader = Shader(GL_FRAGMENT_SHADER, "src/shaders/frag.glsl")

    shaderProgram = ShaderProgram()
    shaderProgram.attachShader(vertShader)
    shaderProgram.attachShader(fragShader)
    shaderProgram.link()
    shaderProgram.use()

    pipeline = RenderPipeline()
    engine.bindPipeline(pipeline)

    while engine.running == True:
        deltaTime = engine.tick(60)

        pygame.display.set_caption(f"FPS: {int(1 / deltaTime)}")

        # Base Engine Loop
        engine.registerEvents()
        engine.physicsStep(deltaTime)

        shaderProgram.use()
        engine.render(deltaTime)

    shaderProgram.clean()
    pipeline.cleanup()


if __name__ == "__main__":
    main()
