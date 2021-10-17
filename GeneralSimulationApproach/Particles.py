import numpy as np

class Particles:
    def __init__(self, type, X,V,color, radii):
        self.type = type
        self.X = X
        self.V = V
        self.color = color
        self.X0 = self.X
        self.V0 = self.V
        self.radii = radii
        self.force = np.array((0,0), dtype='float')

