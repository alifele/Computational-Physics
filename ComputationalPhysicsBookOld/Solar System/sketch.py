import pygame
from pygame.locals import *
import numpy as np


class Sketch:

    def setup(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((15, 50, 70))
        self.particle = Particle(np.array((1,0),dtype='float'),np.array((5,0),dtype='float'), self.screen)

    def update(self, t):
        self.particle.move()
        self.particle.draw()

        if t%1000==0:
            self.screen.fill((15, 50, 70))
            self.particle.move()
            self.particle.draw()
            pygame.display.update()


class Particle:
    def __init__(self, X, V, surface):
        self.X = X
        self.V = V
        self.t = 0
        self.dt = 0.001
        self.surface = surface
        self.ratio = 50

    def move(self):
        self.solveX()
        self.solveV()
        self.t += self.dt

    def solveX(self):
        self.X += self.V * self.dt

    def solveV(self):
        self.V = (-self.X) * self.dt

    def draw(self):

        X = self.ratio * self.X[0] + 400
        Y = self.ratio * self.X[0] + 300
        pygame.draw.circle(self.surface, (255, 255, 255), (X,Y), 5)


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