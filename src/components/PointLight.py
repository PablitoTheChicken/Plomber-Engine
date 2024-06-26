import engine
import glm

lightIndex = 0


class PointLight:
    def __init__(self, color=glm.vec3(1, 1, 1)):
        global lightIndex
        self.parent = None
        self.color = color
        self.lightIndex = lightIndex
        lightIndex += 1

    def update(self, dt):
        engine.engine.shaderProgram.setUniform1i("material.diffuse", 1)
        engine.engine.shaderProgram.setUniform1i("material.specular", 1)
        engine.engine.shaderProgram.setUniform1f("material.shininess", 32.0)

        engine.engine.shaderProgram.setUniformVec3f(
            "pointLights[" + str(self.lightIndex) + "].position", self.parent.position
        )
        engine.engine.shaderProgram.setUniformVec3f(
            "pointLights[" + str(self.lightIndex) + "].ambient", self.color
        )
        engine.engine.shaderProgram.setUniformVec3f(
            "pointLights[" + str(self.lightIndex) + "].diffuse", glm.vec3(0.8, 0.8, 0.8)
        )
        engine.engine.shaderProgram.setUniformVec3f(
            "pointLights[" + str(self.lightIndex) + "].specular",
            glm.vec3(1.0, 1.0, 1.0),
        )
        engine.engine.shaderProgram.setUniform1f(
            "pointLights[" + str(self.lightIndex) + "].constant", 0.1
        )
        engine.engine.shaderProgram.setUniform1f(
            "pointLights[" + str(self.lightIndex) + "].linear", 0.01
        )
        engine.engine.shaderProgram.setUniform1f(
            "pointLights[" + str(self.lightIndex) + "].quadratic", 0.032
        )
