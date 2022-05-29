import pygame
from pygame.locals import *
import numpy as np






class Sketch:

    def setup(self):
        self.screen = pygame.display.set_mode((50*15, 45*15))
        self.screen.fill((0, 68, 102))


        self.resolution = 15
        self.rows = int(self.screen.get_width()/self.resolution)
        self.columns = int(self.screen.get_height()/self.resolution)


        self.mat = np.random.randint(2, size=(self.rows, self.columns))

        for i in range(self.rows):
            for j in range(self.columns):
                if self.mat[i,j] == 0:
                    color = (0,0,0)
                else:
                    color = (255,255,255)
                pygame.draw.rect(self.screen, color,
                                 (i * self.resolution, j * self.resolution, self.resolution-1, self.resolution-1))




    def draw(self):

        select = (np.random.randint(1,self.rows-1), np.random.randint(1,self.columns-1))

        x = select[0]
        y = select[1]
        H = self.mat[x-1,y] +  self.mat[x,y-1] + self.mat[x+1,y] + self.mat[x,y+1]

        if H * self.mat[select] > 0:
            color = (0, 0, 0)
            self.mat[select] = 0
        else:
            color = (255,255,255)
            self.mat[select] = 1

        pygame.draw.rect(self.screen, color,
                         (x * self.resolution, y * self.resolution, self.resolution - 1, self.resolution - 1))


        pygame.display.update()