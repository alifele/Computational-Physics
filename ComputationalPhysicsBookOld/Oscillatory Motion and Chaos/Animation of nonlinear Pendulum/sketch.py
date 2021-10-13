import pygame
from pygame.locals import *
import numpy as np


class Sketch:

    def setup(self, parameters):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((15, 50, 70))
        # self.particle = Particle(self.screen.get_width()/2,self.screen.get_height()/2,self.screen)
        # self.particles = []
        # self.n_particles = 150
        # for i in range(self.n_particles):
        #     self.particles.append(Particle(self.screen.get_width()/2,self.screen.get_height()/2,self.screen))


        self.particle_list = []

        for i in range(300):
            pivotX = 400
            pivotY = 300
            self.particle = Particle(0+0.0001*i, 0, parameters, self.screen)
            self.pivot = Pivot(pivotX, pivotY, (123, 154, 100), 5, self.screen)
            self.line = Line((pivotX, pivotY), (0, 0), self.screen)
            self.particle_list.append((self.particle, self.pivot, self.line))

    def update(self, t):
        self.screen.fill((15, 50, 70))
        for elem in self.particle_list:
            elem[0].move()
            X2 = elem[0].getCenter()
            elem[2].draw(X2)
            elem[0].draw()

        pygame.display.update()


class Particle:
    def __init__(self, theta, thetaDot, parameters, surface):
        self.theta = theta
        self.thetaDot = thetaDot
        self.thetaDDot = 0
        self.parameters = parameters  # dictionary contains the information of parameters like g,l,t, etc
        # self.parameters contians information about g,l,q,FD,Omega

        self.dt = parameters['dt']
        self.t = 0
        self.surface = surface

        self.x = 0
        self.y = 0
        self.x_real = 0
        self.y_real = 0
        self.myEnv = parameters['env']
        self.ratio = 15
        # self.vx = vx
        # self.vy = vy
        # self.surface = surface
        # self.color = color

    def move(self):
        self.solveThetaDot()
        self.solveTheta()
        self.t += self.dt

    def solveThetaDot(self):
        self.thetaDot += (-self.parameters['g'] / self.parameters['l'] * np.sin(self.theta) -
                          self.parameters['q'] * self.thetaDot + self.parameters['FD'] *
                          np.sin(self.parameters['Omega'] * self.t)) * self.dt

    def solveTheta(self):
        self.theta += self.thetaDot * self.dt

    def position(self):
        theta = self.theta
        self.x = self.parameters['l'] * np.sin(theta)
        self.y = self.parameters['l'] * np.cos(theta)

    def draw(self):
        self.position()
        self.backToRealWorld()
        pygame.draw.circle(self.surface, (255, 255, 255), (self.x_real, self.y_real), 5)

    def getCenter(self):
        return self.x_real, self.y_real

    def backToRealWorld(self):
        self.x_real = self.ratio * self.x * self.myEnv.Sim2SI(1, 'length') + 400
        self.y_real = self.ratio * self.y * self.myEnv.Sim2SI(1, 'length')  + 300




class Pivot:
    def __init__(self, x, y, color, rad, screen):
        self.x = x
        self.y = y
        self.color = color
        self.rad = rad
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 4)


class Line:
    def __init__(self, X1, X2, screen):
        self.X1 = X1
        self.X2 = X2
        self.screen = screen

    def draw(self, X2):
        self.X2 = X2
        pygame.draw.line(self.screen, (240, 154, 190), self.X1, self.X2, 2)

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