import pygame
from pygame.locals import *
from sys import exit
from sketch import Sketch

pygame.init()
sketch = Sketch()
sketch.setup()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    sketch.draw()
