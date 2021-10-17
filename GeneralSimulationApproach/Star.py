from Type import *
import numpy as np
from Particles import *

class Star:
    def __init__(self, core):
        self.n = 400
        self.aroundCore1 = 200
        self.aroundCore2 = 200

        self.rmax = 10
        self.vmax = 10

        self.coeff = 1
        self.cores = core


    def GenerateParticleInstance(self, Type):
        for i in range(self.aroundCore1):
            theta = np.random.random()*np.pi*2
            r = np.random.random()*self.rmax
            x = r*np.cos(theta) + self.cores.coreConfig['core1']['X0'][0]
            y = r*np.sin(theta) + self.cores.coreConfig['core1']['X0'][1]
            self.vmax = 1/np.sqrt(r)
            vx = -self.vmax*np.sin(theta)
            vy = self.vmax*np.cos(theta)
            particle = Particles('star', np.array((x,y)),np.array((vx,vy)), np.random.random(3)*255 %255, 2)
            Type.Particles.append(particle)

        for i in range(self.aroundCore2):
            theta = np.random.random()*np.pi*2
            r = np.random.random()*self.rmax
            x = r*np.cos(theta) + self.cores.coreConfig['core2']['X0'][0]
            y = r*np.sin(theta) + self.cores.coreConfig['core2']['X0'][1]
            self.vmax = 1/np.sqrt(r)
            vx = -self.vmax*np.sin(theta)
            vy = self.vmax*np.cos(theta)
            particle = Particles('star', np.array((x,y)),np.array((vx,vy)), np.random.random(3)*255 %255, 2)
            Type.Particles.append(particle)


    def GenerateTypeInstance(self):
        Star = Type('star', self.n, ['core'], [], self.coeff)
        return Star
