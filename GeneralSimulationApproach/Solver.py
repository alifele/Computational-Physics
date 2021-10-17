import numpy as np

class Solver:
    def __init__(self, parameters):
        self.parameters = parameters
        self.dt = 0.02


    def SolveX(self,particle, coeff):
        particle.V += particle.force*self.dt
        particle.X += particle.V*self.dt
        #particle.X += coeff*(np.random.random(2)*2 -1)
