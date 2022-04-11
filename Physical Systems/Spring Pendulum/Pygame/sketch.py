import pygame
import numpy as np
from pygame.locals import *
from Physics import Physics
import matplotlib.pyplot as plt




class Sketch:
    def setup(self):
        self.Width = 640
        self.Height = 480
        self.screen = pygame.display.set_mode((self.Width, self.Height))
        self.screen.fill((15,50,70))
        self.counter = 0

        self.physics = Physics()
        self.physics.calculate()
        #plt.plot(self.physics.Psi[0,0,:]); plt.show()



        ball = Ball(self)
        spring = Spring(self)

        self.sprites = SpritesGroup()
        self.sprites.add(ball)
        self.sprites.add(spring)




    def draw(self):
        self.screen.fill((15, 50, 70))
        data = self.physics.Psi[:,:,self.counter]
        self.sprites.update(data)
        self.sprites.draw(self.counter)
        pygame.display.update()
        self.counter += 1





class Spring:
    def __init__(self, sketch):
        self.sketch = sketch
        self.twoEnds = np.array([[0, 0],[0, 0]], dtype='float') +np.array([self.sketch.Width/2, 50])
        self.color = pygame.Color((255,255,255))
        self.width = 5

        self.transMat = np.array([[50,0], [0,-50]])

    def update(self, data): ## data[0] --> x, theta | data[1] --> x_dot, theta_dot
        L = data[0,0] + self.sketch.physics.L
        theta = data[0,1]
        self.twoEnds[1,0] = (L)*np.sin(theta)   ## x coordinate of end
        self.twoEnds[1,1] = -(L)*np.cos(theta)   ## y cooridnate of end

    def draw(self,i):
        ## Note that before drawing we need to make the transformation to the
        ## visualization world
        twoEnds = self.transform()
        pygame.draw.line(self.sketch.screen, self.color, self.twoEnds[0], twoEnds , width=self.width)

    def transform(self): ## data is [x,y] in the real world
        twoEnds = np.matmul(self.transMat, self.twoEnds[1])+np.array([self.sketch.Width/2, 50])
        return twoEnds


class Ball:
    def __init__(self, sketch):
        self.sketch = sketch
        self.pos = np.array([0, 0], dtype='float')
        self.color = pygame.Color((255, 155, 200))
        self.rad = 20
        self.tail = 30

        self.transMat = np.array([[50, 0], [0, -50]])

    def update(self, data):
        L = data[0, 0] + self.sketch.physics.L
        theta = data[0, 1]
        self.pos[0] = (L) * np.sin(theta)  ## x coordinate of end
        self.pos[1] = -(L) * np.cos(theta)  ## y cooridnate of end

    def draw(self,i):
        ## Note that before drawing we need to make the transformation to the
        ## visualization world
        pos = self.transform()
        pygame.draw.circle(self.sketch.screen, self.color, pos, self.rad)

        # for j in range(i):
        #     data = self.sketch.physics.Psi[:,:,i]
        #     self.update(data)
        #     pos = self.transform()
        #     pygame.draw.circle(self.sketch.screen, self.color, pos, self.rad/5)



    def transform(self): ## data is [x,y] in the real world
        pos = np.matmul(self.transMat, self.pos)+np.array([self.sketch.Width/2, 50])
        return pos


class SpritesGroup:
    def __init__(self):
        self.allSprites = []

    def add(self, sprite):
        self.allSprites.append(sprite)

    def draw(self,i):
        for sprite in self.allSprites:
            sprite.draw(i)

    def update(self, data):
        for sprite in self.allSprites:
            sprite.update(data)
