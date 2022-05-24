import pygame
from pygame.locals import *
import numpy as np
from Square import Square




class Sketch:

    def setup(self):
        self.Width = 800
        self.Height = 800
        self.theta = np.pi/1.5
        self.phi = self.Width/self.Height * self.theta
        self.f = 10
        self.n = 0.01
        self.screen = pygame.display.set_mode((self.Width, self.Height))
        self.screen.fill("#778c81")

        self.square = Square(self.screen)

        self.edges_NDC = self.project(self.square.edges)
        self.edgesRaster = self.raster(self.edges_NDC)

        print("hey")

        self.counter = 0.0



    def draw(self):
        self.screen.fill("#778c81")


        self.square.update(1/10)
        self.edges_NDC = self.project(self.square.edges)
        self.edgesRaster = self.raster(self.edges_NDC)

        for i, face in enumerate(self.square.faces):
            pointsList = self.edgesRaster.T[face][:,:2].tolist()
            # pygame.draw.polygon(self.screen, self.square.colors[i], pointsList)
            pygame.draw.polygon(self.screen, pygame.Color("White"), pointsList,5)

        # for i, elem in enumerate(self.edgesRaster.T):
        #     pygame.draw.circle(self.screen, np.array([255,255,255])*elem[2], elem[:2], 5)
        #     # if i != 7:
        #     #     pygame.draw.line(self.screen, pygame.Color("White"), elem[:2], self.edgesRaster[:2,i+1])
        #     # else:
        #     #     pygame.draw.line(self.screen, pygame.Color("White"), elem[:2], self.edgesRaster[:2,0])


        pygame.display.update()
        self.counter += 1



    def project(self, edges):
        s1 = 1/np.tan(self.theta/2)
        s2 = 1/np.tan(self.phi/2)
        c = (self.f/(self.f-self.n))
        d = -(self.f*self.n)/(self.f-self.n)

        mat = np.array([[s1,0,0,0],[0,s2,0,0],[0,0,c,d],[0,0,1,0]])
        result = mat @ edges
        results = result / result[-1,:]

        return results

    def raster(self, edges):
        shift = np.array([[1,0,0,self.Width/4],[0,1,0,self.Height/4],[0,0,0,0],[0,0,0,1]])
        scale = np.array([[self.Width/1.25,0,0,0],[0,self.Height/1.25,0,0],[0,0,1,0],[0,0,0,1]])
        return shift @ (scale @ edges)



