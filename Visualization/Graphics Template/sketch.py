import pygame
from pygame.locals import *


class Sketch:

    def setup(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.screen.fill((15,50,70))



    def draw(self):
        pygame.draw.rect(self.screen, (40, 161, 151), (10,10,15,15))
        pygame.display.update()
