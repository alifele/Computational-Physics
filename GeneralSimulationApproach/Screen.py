import pygame
import numpy as np


class Screen:
    def __init__(self, parameters):
        self.parameters = parameters
        self.setTransformations()

        self.screen = pygame.display.set_mode((self.parameters['width'], self.parameters['height']))
        self.screen.fill(self.parameters['background'])

        pygame.init()

    def setTransformations(self):
        self.scale = 5
        self.transitoin = np.array([self.parameters['width']/2, self.parameters['height']/2])
        self.rotation = np.eye(2)

    def Transform(self,X):
        return self.scale*X + self.transitoin

    def update(self):
        pass


    def fill(self):
        self.screen.fill(self.parameters['background'])
