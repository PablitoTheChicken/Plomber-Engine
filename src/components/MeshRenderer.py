from meshFile import *
import engine


class MeshRenderer:
    def __init__(self, meshFile):
        mesh = MeshFile(meshFile)
        self.mesh = mesh

    def update(self, dt):
        self.mesh.draw(engine.engine.shaderProgram)
