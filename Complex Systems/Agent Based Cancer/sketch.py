import pygame
from pygame.locals import *
import numpy as np
from System import System
from MainWindow import MainWindow





class Sketch:

    def setup(self):
        self.screen = pygame.display.set_mode((3*20*16, 3*20*16))
        self.screen.fill((0, 68, 102))
        self.system = System(self)
        self.mainWindow = MainWindow(self)

        self.scenes = {"Main": self.mainWindow,
                       "Sim": self.system}

        self.scene = self.scenes["Sim"]
        self.renderMatToBuffer(self.scene)

    def draw(self):
        self.scene.update()
        pygame.display.update()


    def eventManager(self, event):
        self.scene.handleEvent(self, event)


    def clean(self):
        self.screen.fill((0, 68, 102))


    def renderMatToBuffer(self, window):
        for i in range(window.rows):
            for j in range(window.columns):
                if window.popMat[i,j] == 0:
                    color = (0,0,0)
                else:
                    color = window.colors[window.typeMat[i,j]]
                pygame.draw.rect(self.screen, color,
                                 (i * window.resolution, j * window.resolution, window.resolution-1, window.resolution-1))


