import pygame
from pygame.locals import *
import numpy as np
from pygame import gfxdraw


class Sketch:

    def setup(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((15, 50, 70))
        self.sunList = []
        self.ratio = 30
        self.transition = np.array([400,300,0])
        self.scale  = 30

    def update(self, StarsX, CoresX, frameNumber):
        self.screen.fill((15, 50, 70))
        for star in range(int(StarsX.shape[0]/2)):
            X = StarsX[star, :, frameNumber]
            XDisp = self.scale*X + self.transition
            pygame.draw.circle(self.screen, (255, 0, 0), XDisp[:-1], 1)


            j = star + int(StarsX.shape[0]/2)
            X = StarsX[j, :, frameNumber]
            XDisp = self.scale * X + self.transition
            pygame.draw.circle(self.screen, (0, 255, 0), XDisp[:-1], 1)

        # for i in range(int(StarsX.shape[0]/2)):
        #     j = i+star+1
        #     X = StarsX[j, :, frameNumber]
        #     XDisp = self.scale*X + self.transition
        #     pygame.draw.circle(self.screen, (0, 255, 0), XDisp[:-1], 1)

        for core in range(CoresX.shape[0]):
            X = CoresX[core, :, frameNumber]
            XDisp = self.scale * X + self.transition
            pygame.draw.circle(self.screen, (255, 255, 0), XDisp[:-1], 6)

        pygame.display.update()
