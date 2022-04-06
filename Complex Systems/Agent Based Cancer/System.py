import numpy as np
import pygame
from pygame.locals import *
import matplotlib.pyplot as plt




## TODO: Showing the results dynamically on the canvas or on another window

## TODO: the value of G becomes negative and I am holding it positive by taking absolute value of it. It is not a
## TODO: very good solution. There must be some errors with my calculations.

class System:

    def __init__(self, Sketch):
        self.resolution = 5
        self.sketch = Sketch
        screen = self.sketch.screen
        self.rows = int(screen.get_width() / self.resolution)
        self.columns = int(screen.get_height() / self.resolution)
        self.screen = screen
        self.directions = [np.array([-1, -1]), np.array([-1, 0]), np.array([-1, 1]), np.array([1, -1])
            , np.array([1, 0]), np.array([1, 1]), np.array([0, -1]), np.array([0, 1])]

        self.alpha = 0.01
        self.w = 0.0055
        self.beta = 1.5 ## Dynamics scaling factor


        y = np.arange(-int(self.rows / 2), int(self.rows / 2))
        x = np.arange(-int(self.columns / 2), int(self.columns / 2))

        self.X, self.Y = np.meshgrid(x, y)
        self.popMat = np.zeros((self.rows, self.columns))
        self.typeMat = np.ones((self.rows, self.columns), dtype='int16') * (-2)
        ## 0,1,2 (core-mantle-surface) ## -2 -> black, -1 -> white
        ## Type 1 means q cells
        ## Type 2 means p cells
        self.ageMat = np.random.randint(0, 255, size=(self.rows, self.columns), dtype="uint8")

        self.colors = [(102, 102, 51), (0, 153, 204), (255, 153, 102), (0, 0, 0), (255, 255,255)]
        ## Zero layer - First Layer - Second layer (outer layer) - Black pixel (noting) - Neutral element(white)

        self.penColor = self.colors[-1]  ## -1 --> white, -2 --> Black
        self.initMats()



    def initMats(self):
        center = [0, 0]
        R0 = 30
        R1 = R0 * 40
        self.R2 = R1 * 1.1
        #
        # R0 = 10
        # R1 = R0 * 40
        # self.R2 = R1 * 1.3

        self.K = self.R2 - R1
        self.popMat[(self.X - center[0]) ** 2 + (self.Y - center[1]) ** 2 < self.R2] = 1
        self.typeMat[(self.X - center[0]) ** 2 + (self.Y - center[1]) ** 2 < self.R2] = 2
        self.typeMat[(self.X - center[0]) ** 2 + (self.Y - center[1]) ** 2 < R1] = 1
        self.typeMat[(self.X - center[0]) ** 2 + (self.Y - center[1]) ** 2 < R0] = 1
        self.ageMat[self.popMat == 0] = 0

        self.calculate_pq()



    def handleEvent(self, Sketch, event):
        self.mouseDrawEventLoop(event)
        self.keyBoardEvent(Sketch, event)

    def keyBoardEvent(self, Sketch, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                self.penColor = self.colors[0]
            if event.key == pygame.K_1:
                self.penColor = self.colors[1]
            if event.key == pygame.K_2:
                self.penColor = self.colors[2]
            if event.key == pygame.K_w:
                self.penColor = self.colors[-1]

            if event.key == pygame.K_o:
                Sketch.scene = Sketch.scenes["Main"]
                Sketch.clean()
                Sketch.renderMatToBuffer(Sketch.scene)

    def mouseDrawEventLoop(self, event):
        left, middle, right = pygame.mouse.get_pressed()

        if left:
            pos = pygame.mouse.get_pos()
            i = pos[0] // self.resolution
            j = pos[1] // self.resolution
            self.popMat[i, j] = 1
            self.typeMat[i, j] = self.colors.index(self.penColor)
            pygame.draw.rect(self.screen, self.penColor,
                             (i * self.resolution, j * self.resolution, self.resolution - 1,
                              self.resolution - 1))
        if right:
            pos = pygame.mouse.get_pos()
            i = pos[0] // self.resolution
            j = pos[1] // self.resolution
            self.popMat[i, j] = 1
            self.typeMat[i, j] = self.colors.index(self.colors[-2])
            pygame.draw.rect(self.screen, self.colors[-2],
                             (i * self.resolution, j * self.resolution, self.resolution - 1,
                              self.resolution - 1))
        if middle:
            self.popMat *= 0
            self.typeMat = np.ones(self.typeMat.shape, dtype = 'int') * (-2 )

            self.sketch.renderMatToBuffer(self)

    def update(self,t):
        # self.gameOfLife()
        self.TumorGrowth()




    def gameOfLife(self):  ## By using this update rule you will have the game of life simulation
        mat1 = np.roll(np.roll(self.popMat, -1, axis=0), -1, axis=1)
        mat2 = np.roll(self.popMat, -1, axis=0)
        mat3 = np.roll(np.roll(self.popMat, -1, axis=0), 1, axis=1)
        mat4 = np.roll(self.popMat, 1, axis=1)
        mat5 = np.roll(np.roll(self.popMat, 1, axis=0), 1, axis=1)
        mat6 = np.roll(self.popMat, 1, axis=0)
        mat7 = np.roll(np.roll(self.popMat, 1, axis=0), -1, axis=1)
        mat8 = np.roll(self.popMat, -1, axis=1)

        result = mat1 + mat2 + mat3 + mat4 + mat5 + mat6 + mat7 + mat8

        self.popMat[(result == 2) + (result == 3)] *= 1
        self.popMat[(result == 3)] = 1
        self.popMat[(result != 2) * (result != 3)] = 0  ## !((result==2)+(result==3))

        self.sketch.renderMatToBuffer(self)


    def TumorGrowth(self):
        # self.death()
        self.calculateGamma()
        self.calculateG()
        self.update_pq()


    def calculateGamma(self):
        ### Calculating R0,R1,R2
        ## We have the position of the grids on self.X and self.Y arrays. So by masking them we can
        ## get the X,Y coordinates of each type of cells easily. Here I assume R is the mean of the distance of
        ## all cells from a certain type

        ### Calculating R0
        self.X0 = self.X[self.typeMat==0]
        self.Y0 = self.Y[self.typeMat==0]
        # R0 = (np.sqrt(self.X0 ** 2+self.Y0 ** 2)).mean()
        R0 = (np.sqrt(self.X0 ** 2+self.Y0 ** 2)).mean() * 0


        ### Calculating R1 (i.e. the radius of q cells)
        self.X1 = self.X[self.typeMat == 1]
        self.Y1 = self.Y[self.typeMat == 1]
        R1 = (np.sqrt(self.X1 ** 2 + self.Y1 ** 2)).mean()

        ### Calculating R2 (i.e. the radius of p cells)
        self.X2 = self.X[self.typeMat == 2]
        self.Y2 = self.Y[self.typeMat == 2]
        self.R2_next = (np.sqrt(self.X2 ** 2 + self.Y2 ** 2)).mean()

        #pygame.draw.circle(self.screen, (255,255,255), (int(self.columns ),int(self.rows )),5*R1)
        #print(R1)

        self.K = self.R2 - R1


        #self.gamma = 3*self.K/self.R**2 * (1-self.K/self.R)**2
        self.gamma = 2*self.K/self.R2**2 * (1-self.K/self.R2) * (self.R2_next - self.R2)   ## For 2D

        self.R2 = self.R2_next




    def calculateG(self):
        self.calculate_pq()
        self.G = (self.p + self.q)/(self.q) * self.gamma - self.p/(self.p+self.q) * self.alpha


    def update_pq(self):
        ### Let's select one random cell (it can be p cell or q cell)
        rand = np.random.random()
        if rand < self.X2.size / (self.X2.size + self.X1.size): ## the selected cell is 2 type cell
            randint = np.random.randint(self.X2.size)
            x = self.X2[randint]
            y = self.Y2[randint]
            self.pos = np.array([x,y])

            ### Now let's find out the cell will divide or die?
            ## First we should calculate the normalization factor
            c1 = 1/(self.w + self.alpha)
            rand = np.random.random()
            if rand  < self.beta * self.w/(self.beta * self.w+self.alpha):  ## Cell will die
                # if (x ** 2 + y ** 2 < (50+np.random.randn()*20) ** 2) and rand < 0.1:
                #     self.typeMat[(self.X == x) * (self.Y == y)] = 0
                # else:
                #     self.popMat[(self.X==x) * (self.Y == y)] = 0
                #     self.typeMat[(self.X==x) * (self.Y == y)] = -2

                if rand < 0.07: ## Cell will turn into necrotic cell
                    self.typeMat[(self.X == x) * (self.Y == y)] = 0
                else:           ## Cell will die and disappear
                    self.popMat[(self.X==x) * (self.Y == y)] = 0
                    self.typeMat[(self.X==x) * (self.Y == y)] = -2

            else:                                   ## Cell will proliferate
                flag = 0
                np.random.shuffle(self.directions)
                for dirs in self.directions:
                    pos_ = self.pos + dirs
                    if self.popMat[(self.X==pos_[0]) * (self.Y == pos_[1])] == 0:
                        self.popMat[(self.X == pos_[0]) * (self.Y == pos_[1])] = 1
                        self.typeMat[(self.X == pos_[0]) * (self.Y == pos_[1])] = 2
                        flag = 1
                        break

                if flag == 0:
                    dirRand = np.random.randint(8)
                    direction = self.directions[dirRand]
                    pos_ = self.pos + direction
                    while self.popMat[(self.X==pos_[0]) * (self.Y == pos_[1])] != 0:
                        pos_ += direction
                    self.popMat[(self.X == pos_[0]) * (self.Y == pos_[1])] = 1
                    rand = np.random.randint(2)
                    if rand == 0: ## daughter will turn into blue cells
                        self.typeMat[(self.X == pos_[0]) * (self.Y == pos_[1])] = 1
                    elif rand ==1:  ## daughter cell will remain orange cell
                        self.typeMat[(self.X == pos_[0]) * (self.Y == pos_[1])] = 2
                    # else:   ## Cells close to the center will become necrotic
                    #     if (pos_[0]**2 + pos_[1]**2 < 50**2):
                    #         self.typeMat[(self.X == pos_[0]) * (self.Y == pos_[1])] = 0



        else: ## The selected cell is 1 type cell
            randint = np.random.randint(self.X1.size)
            x = self.X1[randint]
            y = self.Y1[randint]

            rand = np.random.random()
            #print("G=",self.G)
            if rand < self.beta*self.w/(np.abs(self.G)*10 + self.beta*self.w):     ## Cell will die
                # if (x ** 2 + y ** 2 < (50+np.random.randn()*20) ** 2) and rand < 0.04:
                #     self.typeMat[(self.X == x) * (self.Y == y)] = 0
                # else:
                #     self.popMat[(self.X == x) * (self.Y == y)] = 0
                #     self.typeMat[(self.X == x) * (self.Y == y)] = -2

                if  rand < 0.07:    ## The cell will become necrotic cell
                    self.typeMat[(self.X == x) * (self.Y == y)] = 0
                else:               ## The cell will die and disappear
                    self.popMat[(self.X == x) * (self.Y == y)] = 0
                    self.typeMat[(self.X == x) * (self.Y == y)] = -2

            else:                                   ## Cell will turn into 2 type cell
                if self.G>0:
                    self.typeMat[(self.X == x) * (self.Y == y)] = 2

            # else:
            #     if rand < self.w / (np.abs(self.G) + self.w):  ## Cell will die
            #         self.popMat[(self.X == x) * (self.Y == y)] = 0
            #         self.typeMat[(self.X == x) * (self.Y == y)] = -2
            #
            #     else:  ## Cell will turn into 2 type cell
            #         self.typeMat[(self.X == x) * (self.Y == y)] = 1





    def calculate_pq(self):
        self.p = (self.typeMat==2).sum()
        self.q = (self.typeMat==1).sum()


    def getCellType(self,x,y):
        return self.typeMat[(self.X==x) * (self.Y == y)]

