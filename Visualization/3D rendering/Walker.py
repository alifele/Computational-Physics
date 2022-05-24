import numpy as np
import pygame


class Walker:
    def __init__(self, screen):
        self.N_steps = 10000
        self.pos = np.array([0,0])
        self.posList = np.zeros((2,self.N_steps))
        self.screen = screen


    def run(self):
        for t in range(self.N_steps):
            self.posList[:,t] = self.pos
            self.pos += np.random.randint(-1,2,2)


    def draw(self, pos):
        pygame.draw.circle(self.screen, pygame.Color("Red"), pos, 4)

    def drawTail(self, posList, count):
        # for i, pos in enumerate(posList):
        pygame.draw.lines(self.screen, pygame.Color("White"), False, posList[:2, :count].T.tolist())
