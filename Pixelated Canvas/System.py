import numpy as np
import pygame
from pygame.locals import *


## TODO: Adding the mouse interaction. Can be able to draw using the mouse


class System:

    def __init__(self, screen):
        self.resolution = 10
        self.rows = int(screen.get_width() / self.resolution)
        self.columns = int(screen.get_height() / self.resolution)
        self.screen = screen


        y = np.arange(-int(self.rows/2), int(self.rows/2))
        x = np.arange(-int(self.columns/2), int(self.columns/2))

        X,Y = np.meshgrid(x,y)
        self.mat = np.zeros((self.rows, self.columns))



        #self.mat = np.random.randint(2, size=(self.rows, self.columns))

        #self.mat[10*np.sin(X/5)+Y > 0] = 1

        # for i in range(20):
        #     centers = (np.random.randint(x[0],x[-1]), np.random.randint(y[0],y[-1]))
        #     self.mat[(X-centers[0])**2 + (Y-centers[1])**2 <40] = 1

    def renderMatToBuffer(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.mat[i,j] == 0:
                    color = (0,0,0)
                else:
                    color = (255,255,255)
                pygame.draw.rect(self.screen, color,
                                 (i * self.resolution, j * self.resolution, self.resolution-1, self.resolution-1))

    def update(self):
        # select = (np.random.randint(1, self.rows - 1), np.random.randint(1, self.columns - 1))
        # x = select[0]
        # y = select[1]
        # H = self.mat[x - 1, y] + self.mat[x, y - 1] + self.mat[x + 1, y] + self.mat[
        #     x, y + 1]
        #
        # if H * self.mat[select] > 0:
        #     color = (0, 0, 0)
        #     self.mat[select] = 0
        # else:
        #     color = (255, 255, 255)
        #     self.mat[select] = 1
        #
        # pygame.draw.rect(self.screen, color,
        #                  (x * self.resolution, y * self.resolution, self.resolution - 1,
        #                   self.resolution - 1))

        self.mat = np.roll(self.mat,1, axis=1)
        self.mat = np.roll(self.mat,-1, axis=0)
        self.renderMatToBuffer()


    def gameOfLife(self):
        pass


    def mouseDrawEventLoop(self, event):
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_presses = pygame.mouse.get_pressed()
        #     if mouse_presses[0]:
        #         pos = pygame.mouse.get_pos()
        #         i = pos[0]//self.resolution
        #         j = pos[1]//self.resolution
        #         self.mat[i,j] = 1
        #         pygame.draw.rect(self.screen, (255,255,255),
        #                          (i * self.resolution, j * self.resolution, self.resolution - 1,
        #                           self.resolution - 1))

        left, middle, right = pygame.mouse.get_pressed()
        if left:
            pos = pygame.mouse.get_pos()
            i = pos[0]//self.resolution
            j = pos[1]//self.resolution
            self.mat[i,j] = 1
            pygame.draw.rect(self.screen, (255,255,255),
                             (i * self.resolution, j * self.resolution, self.resolution - 1,
                              self.resolution - 1))

        if right:
            pos = pygame.mouse.get_pos()
            i = pos[0]//self.resolution
            j = pos[1]//self.resolution
            self.mat[i,j] = 1
            pygame.draw.rect(self.screen, (0,0,0),
                             (i * self.resolution, j * self.resolution, self.resolution - 1,
                              self.resolution - 1))





