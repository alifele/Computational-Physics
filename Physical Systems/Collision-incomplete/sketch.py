import pygame
from pygame.locals import *
from physics import Physics


class Sketch:

    def setup(self):
        self.screen = pygame.display.set_mode((500, 500))
        self.screen.fill((15,50,70))

        self.physics = Physics(self.screen)





    def draw(self):
        self.screen.fill((15,50,70))
        self.physics.balls.move(0.005)
        self.drawBalls(self.physics.Phys2DispyTrans())
        pygame.display.update()



    def drawBalls(self, phi):
        for i in range(self.physics.balls.N):
            pygame.draw.circle(self.screen, (40, 161, 151), phi[:2,i],10)