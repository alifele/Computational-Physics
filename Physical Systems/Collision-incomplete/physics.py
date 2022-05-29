from balls import Balls
import numpy as np


class Physics:
    def __init__(self, screen):
        self.screen = screen
        self.physConf = {"width": 500,
                         "height": 500,
                         "N": 100,
                         "R": 3,
                         "Kb": 500,
                         "Kw": 500}
        self.balls = Balls(screen, self.physConf)

        screenWidth = self.screen.get_width()
        screenHeight = self.screen.get_height()
        scaleMat = np.array([[screenWidth / self.physConf["width"], 0, 0],
                             [0, -screenHeight / self.physConf["height"], 0],
                             [0, 0, 1]])

        shiftMat = np.array([[1, 0, screenWidth / 2],
                             [0, 1, screenHeight / 2],
                             [0, 0, 1]])

        self.Phys2DispMat = shiftMat @ scaleMat

        self.Phys2DispMat = np.array([[screenWidth / self.physConf["width"], 0, screenWidth / 2],
                                      [0, -screenHeight / self.physConf["height"], screenHeight / 2],
                                      [0, 0, 1]])

        dt = 0.1
        # for i in range(100):
        #     balls.move(dt)

    def Phys2DispyTrans(self):
        return self.Phys2DispMat @ self.balls.Phi[:3, :]
