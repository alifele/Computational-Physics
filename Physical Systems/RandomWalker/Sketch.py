import pygame
from pygame.locals import *
import numpy as np
from Walker import Walker





class Sketch:

    def setup(self):
        self.Height = 1000
        self.Width = 1000
        self.screen = pygame.display.set_mode((self.Height, self.Width))
        self.screen.fill((0, 68, 102))

        self.walker = Walker(self.screen)
        self.walker.run()

        self.posList = np.ones((3, self.walker.N_steps))

        self.counter = 2


        self.transform()


    def scale(self, sx, sy):
        return np.array([[sx,0,0],[0,sy,0],[0,0,1]])

    def shift(self, dx, dy):
        return np.array([[1,0,dx],[0,1,dy],[0,0,1]])


    def draw(self):
        self.screen.fill((0, 68, 102))
        self.walker.drawTail(self.posList, self.counter)
        self.walker.draw(self.posList[:2,self.counter])

        pygame.display.update()

        self.counter += 1


    def transform(self):
        self.posList[:2, :] = self.walker.posList
        self.posList = self.shift(self.Height/2, self.Width/2) @ (self.scale(10,10)@self.posList)




