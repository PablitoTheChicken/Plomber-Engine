from meshFile import *
import engine


class MeshRenderer:
    def __init__(self, meshFile):
        mesh = MeshFile(meshFile)
        self.parent = None
        self.mesh = mesh

    def update(self, dt):
        model = glm.mat4(1.0)
        model = glm.translate(model, self.parent.position)
        model = glm.rotate(
            model, glm.radians(self.parent.rotation.x), glm.vec3(1, 0, 0)
        )
        model = glm.rotate(
            model, glm.radians(self.parent.rotation.y), glm.vec3(0, 1, 0)
        )
        model = glm.rotate(
            model, glm.radians(self.parent.rotation.z), glm.vec3(0, 0, 1)
        )

        model = glm.scale(model, self.parent.scale)

        modelLoc = glGetUniformLocation(engine.engine.shaderProgram.program, "model")
        glUniformMatrix4fv(modelLoc, 1, GL_FALSE, glm.value_ptr(model))
        self.mesh.draw(engine.engine.shaderProgram)
