import pygame
from pygame.locals import *
import numpy as np
from System import System





class Sketch:

    def setup(self):
        self.screen = pygame.display.set_mode((3*20*16, 3*20*16))
        self.screen.fill((0, 68, 102))
        self.system = System(self.screen)
        self.system.renderMatToBuffer()

    def draw(self):
        self.system.update()
        pygame.display.update()


    def eventManager(self, event):
        self.system.mouseDrawEventLoop(event)
