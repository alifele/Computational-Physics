import pygame
from pygame.locals import *
import numpy as np
from System import System
from MainWindow import MainWindow

from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation






class Sketch:

    def setup(self, simulateForDifferentCells, dataPoints):
        self.screen = pygame.display.set_mode((3*20*16, 3*20*16))
        self.screen.fill((0, 68, 102))
        self.system = System(self)
        self.mainWindow = MainWindow(self)

        self.scenes = {"Main": self.mainWindow,
                       "Sim": self.system}

        self.scene = self.scenes["Sim"]
        self.renderMatToBuffer(self.scene)
        self.updateFlag = 0

        if simulateForDifferentCells == 1:
            self.t = np.array([1], dtype="int16")
            self.i = np.array([1], dtype="uint16")
            self.data = np.zeros(dataPoints, dtype='float32')



    def draw(self):
        #pygame.display.update()

        self.scene.update(self.t)
        if self.i % 4096 == 0:
            self.renderMatToBuffer(self.scene)
            pygame.display.update()

        if self.i % 60 == 0:
            self.data[self.t-1] = self.scene.p + self.scene.q
            self.t += 1
            print(self.t)


        self.i += 1
        return self.t


    def eventManager(self, event):
        self.scene.handleEvent(self, event)


    def clean(self):
        self.screen.fill((0, 68, 102))


    def renderMatToBuffer(self, window):
        for i in range(window.rows):
            for j in range(window.columns):
                # if window.popMat[i,j] == 0:
                #     color = (0,0,0)
                # else:
                color = window.colors[window.typeMat[i,j]]
                pygame.draw.rect(self.screen, color,
                                 (i * window.resolution, j * window.resolution, window.resolution-1, window.resolution-1))


