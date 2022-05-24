import numpy as np
import pygame


class Square:
    def __init__(self, screen):
        self.screen = screen

        self.edges = np.array([[0,0,0,1],[0,1,0,1],[0,1,1,1],[0,0,1,1],[1,0,1,1],[1,1,1,1],[1,1,0,1],[1,0,0,1]], dtype="float").T
        self.edges[2,:] += 4
        self.edges[0,:] += 1
        self.edges[1,:] += 1

        # theta = -np.pi/2
        # rotMatY = np.array([[np.cos(theta),0,np.sin(theta),0],
        #                    [0,1,0,0],
        #                    [-np.sin(theta), 0, np.cos(theta), 0],
        #                    [0,0,0,1]])
        #
        # rotMatZ = np.array([[np.cos(theta),-np.sin(theta),0,0],
        #                    [np.sin(theta), np.cos(theta),0,0],
        #                    [0,0,1,0],
        #                    [0,0,0,1]])
        #
        # rotMatX = np.array([[1,0,0,0],
        #                     [0,np.cos(theta),-np.sin(theta),0],
        #                     [0,np.sin(theta),np.cos(theta),0],
        #                     [0,0,0,1]])

        # self.edges = rotMatY @ self.edges


        self.faces = np.array([[0,1,6,7],[7,6,5,4],[7,4,3,0],[0,1,2,3],[1,6,5,2],[2,3,4,5]])
        self.colors = np.random.randint(0,256,(6,3)).tolist()


    def draw(self):

        pygame.draw.lines(self.screen, pygame.Color("Red"), True, self.edgesTransformed[:2, :].T.tolist(), 5)
        for i in range(4):
            pygame.draw.circle(self.screen, pygame.Color("White"), self.edgesTransformed[:2, i], 10)


    def rotateX(self, theta):
        rotMat = rotMatX = np.array([[1,0,0,0],
                            [0,np.cos(theta),-np.sin(theta),0],
                            [0,np.sin(theta),np.cos(theta),0],
                            [0,0,0,1]])
        return rotMat


    def rotateY(self, theta):
        rotMat = np.array([[np.cos(theta),0,np.sin(theta),0],
                           [0,1,0,0],
                           [-np.sin(theta), 0, np.cos(theta), 0],
                           [0,0,0,1]])
        return rotMat



    def rotateZ(self, theta):
        rotMat = np.array([[np.cos(theta),-np.sin(theta),0,0],
                           [np.sin(theta), np.cos(theta),0,0],
                           [0,0,1,0],
                           [0,0,0,1]])
        return rotMat


    def update(self, theta):
        rotMatX = np.array([[1, 0, 0, 0],
                            [0, np.cos(theta), -np.sin(theta), 0],
                            [0, np.sin(theta), np.cos(theta), 0],
                            [0, 0, 0, 1]])
        x = self.edges[0,0]
        y = self.edges[1,0]
        z = self.edges[2,0]

        shift_minus = np.array([[1, 0, 0, -x],
                                [0, 1, 0, -y],
                                [0, 0, 1, -z],
                                [0, 0, 0, 1]])

        shift_plus = np.array([[1, 0, 0, x],
                                [0, 1, 0, y],
                                [0, 0, 1, z],
                                [0, 0, 0, 1]])

        self.edges = shift_plus @ ( self.rotateZ(theta/5) @ self.rotateY(theta) @ self.rotateX(theta) @ (shift_minus @ self.edges) )



