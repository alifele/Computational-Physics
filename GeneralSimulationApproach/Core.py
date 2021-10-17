from Type import *
from Particles import *
import numpy as np

class Core:
    def __init__(self):
        self.n = 2
        self.coreList = ['core1', 'core2']
        self.coreConfig = {'core1': {"X0": np.array((-15,  -1 ), dtype='float'),
                                     "V0": np.array((0.15, 0), dtype='float'),
                                     "color": (255, 255, 0)},
                           'core2': {"X0": np.array((15, 1), dtype='float'),
                                     "V0": np.array((-0.15, 0), dtype='float'),
                                     "color": (255, 255, 0)}}

        self.radii = 5
        self.coeff = 1


    def GenerateParticleInstance(self, Type):
        for key in self.coreConfig.keys():
            item = self.coreConfig[key]
            particle = Particles('core',item['X0'],item["V0"],item["color"], self.radii)
            Type.Particles.append(particle)

    def GenerateTypeInstance(self):
        Core = Type('core', self.n, ['core'], ['star'], self.coeff)
        return Core
