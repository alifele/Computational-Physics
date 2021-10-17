import pygame
from sys import exit
from pygame.locals import *
from Type import *
import numpy as np

class Main:
    def __init__(self, realWorld, simWorld, screen, solver, typesList):
        self.realWorld = realWorld
        self.simWorld = simWorld
        self.screen = screen
        self.solver = solver
        self.typesList = typesList

        self.X = np.array((10,0), dtype='float')


        self.TypeClassList = []
        self.TypeClassList.append(self.typesList['core'].GenerateTypeInstance())
        self.TypeClassList.append(self.typesList['star'].GenerateTypeInstance())
        #
        self.typesList['core'].GenerateParticleInstance(self.TypeClassList[0])
        self.typesList['star'].GenerateParticleInstance(self.TypeClassList[1])



    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            self.draw()


    def draw(self):
        screen = self.screen.screen

        for elem in self.TypeClassList:
            for particle in elem.Particles:
                X = particle.X
                XDisp = self.screen.Transform(X)
                pygame.draw.circle(screen, particle.color, XDisp, particle.radii)



        pygame.display.update()

