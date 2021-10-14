import pygame
from pygame.locals import *
import numpy as np


class Sketch:

    def setup(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((15, 50, 70))
        self.sunList= []
        self.ratio = 30


        #self.sunList.append(Sun(self.screen, (-5,0), self.ratio))
        self.sunList.append(Sun(self.screen, np.array((-5,2),dtype='float'),np.array((0.1,0), dtype='float'), self.ratio))
        self.sunList.append(Sun(self.screen, np.array((5,-2),dtype='float'),np.array((-0.1,0), dtype='float'), self.ratio))

        for sun in self.sunList:
            sun.setSunList((self.sunList))



        self.particleList = []
        for i in range(100):
            theta = np.random.random()*np.pi*2
            r = 0.005*i+0.5
            x = r*np.cos(theta) +5
            y = r*np.sin(theta) - 2
            velocity = np.sqrt(1/r)
            vx = -velocity*np.sin(theta)
            vy = velocity*np.cos(theta)
            self.particleList.append(Particle(np.array((x,y),dtype='float'),np.array((vx,vy),dtype='float'), self.screen, self.sunList,self.ratio,(0,220,255)))
            #
            theta = np.random.random() * np.pi * 2
            r = 0.005 * i + 0.5
            x = r * np.cos(theta) - 5
            y = r * np.sin(theta) + 2
            velocity = np.sqrt(1 / r)
            vx = -velocity * np.sin(theta)
            vy = velocity * np.cos(theta)
            self.particleList.append(Particle(np.array((x,y),dtype='float'),np.array((vx,vy),dtype='float'), self.screen, self.sunList,self.ratio,(35,255,0)))

        for elem in self.particleList:
            elem.setParticleList(self.particleList)

    def update(self, t):

        for elem in self.particleList:
            elem.move()
        for elem in self.sunList:
            elem.move()

        if t%20==0:
            self.screen.fill((15, 50, 70))
            for elem in self.sunList:
                elem.move()
                elem.draw()
            for elem in self.particleList:
                elem.move()
                elem.draw()

            pygame.display.update()


class Sun:
    def __init__(self, screen, X,V, ratio):
        self.X = X
        self.ratio = ratio
        self.screen = screen
        self.V = V
        self.dt = 0.008
        self.t = 0
        self.r = 0
        self.sunList = []

    def draw(self):
        x = self.ratio*self.X[0] + 400
        y = self.ratio*self.X[1] + 300
        pygame.draw.circle(self.screen, (255,255,0), (x,y),8)

    def setSunList(self, sunList):
        self.sunList = sunList

    def move(self):
        self.solveV()
        self.solveX()


    def solveX(self):
        self.X += self.V * self.dt

    def solveV(self):
        acceleration = 0
        for sun in self.sunList:
            self.r = np.linalg.norm(self.X - sun.X) + 0.5
            if sun != self:
                acceleration += -(self.X - sun.X) / self.r ** 3
        self.V += acceleration * self.dt


class Particle:
    def __init__(self, X, V, surface, sunList, ratio, color):
        self.X = X
        self.r = np.linalg.norm(self.X)
        self.V = V
        self.t = 0
        self.dt = 0.008
        self.surface = surface
        self.ratio = ratio
        self.particleList = 0
        self.sunList = sunList
        self.color = color

    def setParticleList(self, particleList):
        self.particleList = particleList

    def move(self):
        self.solveV()
        self.solveX()
        self.t += self.dt

    def solveX(self):
        self.X += self.V * self.dt

    def solveV(self):
        acceleration = 0
        for sun in self.sunList:
            self.r = np.linalg.norm(self.X - sun.X) + 0.01
            acceleration += -(self.X - sun.X)/self.r**3
        self.V += acceleration * self.dt

    def draw(self):
        X = self.ratio * self.X[0] + 400
        Y = self.ratio * self.X[1] + 300

        # gray scale color based on velocity
        # color = np.linalg.norm(self.V)/5 * np.array((255,255,255))
        # color.astype('int')
        # color = color % 255

        color = self.color


        pygame.draw.circle(self.surface, color, (X,Y), 1)


class Env:
    def __init__(self, lengthD, timeD, massD):
        self.lengthD = lengthD
        self.timeD = timeD
        self.massD = massD

    def Sim2SI(self, value, quantity):
        if quantity == "mass":
            return value * self.massD
        if quantity == "length":
            return value * self.lengthD
        if quantity == "time":
            return value * self.timeD

    def SI2Sim(self, value, quantity):
        return value / self.Sim2SI(1, quantity)