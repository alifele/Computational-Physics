import pygame
from pygame.locals import *
import numpy as np


class Sketch:

    def setup(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((15, 50, 70))
        self.particle = Particle(np.array((0.5,0),dtype='float'),np.array((0.5,1.5),dtype='float'), self.screen)
        self.sun = Sun(self.screen)

        self.particleList = []
        for i in range(4):
            self.particleList.append(Particle((np.random.random(2)*2-1)*2,(np.random.random(2)*2-1)*2, self.screen))

        for elem in self.particleList:
            elem.setParticleList(self.particleList)

    def update(self, t):

        for elem in self.particleList:
            elem.move()
            #elem.draw()

        if t%1==0:
            self.screen.fill((15, 50, 70))
            for elem in self.particleList:
                elem.move()
                elem.draw()
                self.sun.draw()

            pygame.display.update()


class Sun:
    def __init__(self, screen):
        self.X = 400
        self.Y = 300
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, (255,255,0), (self.X, self.Y),8)


class Particle:
    def __init__(self, X, V, surface):
        self.X = X
        self.V = V
        self.t = 0
        self.dt = 0.0004
        self.surface = surface
        self.ratio = 100
        self.particleList = 0

    def setParticleList(self, particleList):
        self.particleList = particleList

    def move(self):
        self.solveV()
        self.solveX()
        self.t += self.dt

    def solveX(self):
        self.X += self.V * self.dt

    def solveV(self):
        acceleration = 0
        for elem in self.particleList:
            acceleration += (elem.X - self.X)
        acceleration += (-0.5*self.X)
        self.V += (acceleration) * self.dt

    def draw(self):
        X = self.ratio * self.X[0] + 400
        Y = self.ratio * self.X[1] + 300

        # gray scale color based on velocity
        # color = np.linalg.norm(self.V)/5 * np.array((255,255,255))
        # color.astype('int')
        # color = color % 255

        color = (255,255,255)


        pygame.draw.circle(self.surface, color, (X,Y), 5)


class Env:
    def __init__(self, lengthD, timeD, massD):
        self.lengthD = lengthD
        self.timeD = timeD
        self.massD = massD

    def Sim2SI(self, value, quantity):
        if quantity == "mass":
            return value * self.massD
        if quantity == "length":
            return value * self.lengthD
        if quantity == "time":
            return value * self.timeD

    def SI2Sim(self, value, quantity):
        return value / self.Sim2SI(1, quantity)