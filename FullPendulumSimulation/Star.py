from Type import *
import numpy as np
from Particles import *

class Star:
    def __init__(self):
        self.n = 500
        self.aroundCore1 = 200
        self.aroundCore2 = 200

        self.rmax = 50
        self.vmax = 3


    def GenerateParticleInstance(self, Type):
        for i in range(self.n):
            theta = np.random.random()*np.pi*2
            r = np.random.random()*self.rmax
            x = r*np.cos(theta)
            y = r*np.sin(theta)
            vx = -self.vmax*np.sin(theta)
            vy = self.vmax*np.cos(theta)
            particle = Particles('star', np.array((x,y)),np.array((vx,vy)), np.random.random(3)*255 %255, 2)
            Type.Particles.append(particle)


    def GenerateTypeInstance(self):
        Star = Type('star', self.n, ['core'], [])
        return Star
