import pygame
from pygame.locals import *
from sys import exit
from sketch import Sketch
import matplotlib.pyplot as plt

pygame.init()
sketch = Sketch()
simulateForDifferentCells = 1
dataPoints = 3000
sketch.setup(simulateForDifferentCells, dataPoints)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        sketch.eventManager(event)
    stopFlag = sketch.draw()

    # if simulateForDifferentCells == 1:
    #     if stopFlag % dataPoints == 0:
    #         pygame.quit()
    #         break
        #pygame.time.wait(3)

plt.plot(sketch.data[1:-1]); plt.show()