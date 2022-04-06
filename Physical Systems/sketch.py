import pygame
import numpy as np
from Physics import Physics
from pygame.locals import *


class Box:
    def __init__(self, position, screen):
        self.pos = position
        self.screen = screen
        self.color = np.random.randint(100 ,255, size=(3))

    def draw(self, Phi, i, PhiMax, scale):
        square_size = 30
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1],square_size,square_size))

        phi = Phi[1,i]
        if (np.abs(phi) > 0*PhiMax):
            pygame.draw.circle(self.screen, (255,0,0), self.pos+np.array([square_size/2,square_size/2]), int(np.abs(scale*phi)))





class Sketch:

    def setup(self):
        self.width = 200
        self.length = 2500
        self.screen = pygame.display.set_mode((self.length, self.width))
        self.screen.fill((15,50,70))

        self.N = 20
        self.skip = 0

        self.physics = Physics(self.N)

        self.L0 = self.length/20
        self.L = self.L0 * 0.8

        self.Boxes = []
        for i in range(self.N):
            self.Boxes.append(Box([self.L0 + self.L*i, int(self.width/2)], self.screen))


    def Transform(self, Phi):
        for i, box in enumerate(self.Boxes):
            box.pos[0] = self.L0 + self.L*i + 100*Phi[0,i]


    def draw(self):
        Phi = self.physics.calculate()
        if self.skip%5 == 0:
            self.screen.fill((15, 50, 70))
            self.Transform(Phi)
            PhiMax = np.max(Phi[1,:])
            for i, box in enumerate(self.Boxes):
                box.draw(Phi, i, PhiMax, scale=100)
            pygame.display.update()

        self.skip += 1
