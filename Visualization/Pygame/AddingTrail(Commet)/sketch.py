import pygame
from pygame.locals import *
import numpy as np


class Ball():
    def __init__(self, surface):
        self.destSurface = surface
        self.v = pygame.math.Vector2([1.5412, 2.7421])
        self.pos = pygame.math.Vector2([300,300])

        self.tailLength = 100
        self.tailList = np.ones((self.tailLength,2)) * (-1)

        self.sizeMainSurface = self.destSurface.get_size()
        print(self.sizeMainSurface)




    def draw(self):
        pygame.draw.circle(self.destSurface, (123,154,188), self.pos, 10)

    def drawTail(self, t):
        self.tailList = np.roll(self.tailList, 2)
        self.tailList[0,:] = self.pos

        for i, elem in enumerate(self.tailList):
            if elem.sum != -2 :
                pygame.draw.circle(self.destSurface, pygame.Color(200,154,188, a=0), elem+20*np.sin(i/8+t/15), -8/50*i + 508/50)

    def move(self,t):
        if self.pos[0] >= self.sizeMainSurface[0] or self.pos[0] <= 0:
            self.v[0] *= (-1)
        if self.pos[1] >= self.sizeMainSurface[1] or self.pos[1] <= 0:
            self.v[1] *= (-1)

        self.pos += self.v

        self.drawTail(t)
        #self.draw()






class Sketch:

    def setup(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.screen.fill((15,50,70))

        self.ball = Ball(self.screen)

        self.t = 0




    def draw(self):
        self.t += 1
        self.screen.fill((15,50,70))
        self.ball.move(self.t)
        pygame.display.update()
