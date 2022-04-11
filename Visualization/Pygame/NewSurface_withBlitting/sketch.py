import pygame
import pygame.surface
from pygame.locals import *
import numpy as np



## In general we have two methods to add a surface to the main screen. One method is by using sprite objects (which you
## can find its implementation in the other folder. And the other method, which you can see here, is by creating and
## manipulating the surface objects directly (which out using the high level classes like sprite that do things behind
## the curtains!

class Surface():
    def __init__(self, pos):
        self.surface = pygame.Surface([30, 30])
        self.surface.fill((255, 255, 255))


        pygame.draw.rect(self.surface, (54, 125, 247), pygame.Rect(5, 5, 15, 15))
        self.rect = self.surface.get_rect()     ## this will return rect(0,0,width, height). This is the properties of
                                                ## The this surface. The default value for position is [0,0].
                                                ## So we need to set it to the position we want. Note that we can
                                                ## store the cooridnate of this surface in even an numpy array. But it
                                                ## is better to save that in a rect object because it is more useful
                                                ## for example if you have changed something in the surf only, then you
                                                ## can pass rect object to the update function in the main loop so that
                                                ## only this portion gets updated which is faster.
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def draw(self, destination):
        self.blit = destination.blit(self.surface, self.rect)   ## Note that we can use a 2d vector instead of self.rect.
                                                                ## in fact we only want to pass the coordinate of the surface
                                                                ## in the destination. But working with rect object is better
                                                                ## since it can be used in other places as well (for example
                                                                ## I have read that passing self.rect object to update function
                                                                ## updates that portion only so it is faster.


    def move(self, dr):
        self.rect = self.rect.move(dr[0], dr[1])


class Sketch:
    def setup(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.screen.fill((15, 50, 70))

        self.surf1 = Surface(np.array([550,450]))
        self.surf1.draw(self.screen)

        pygame.display.update()

    def draw(self):

        self.screen.fill((15, 50, 70))
        #self.pos += np.random.randint(-0,2, size=2)
        self.surf1.move(np.random.randint(-2,0, size=2))
        self.surf1.draw(self.screen)
        pygame.display.update() ## A possible pitfall: I was thinking to pass the self.surf1.rect to this function
                                ## So at each loop only the part which is updated gets updated on screen (which is
                                ## faster. I did that but it was not working! (you can try that. just put this function
                                ## instead of the current function: pygame.display.update(self.surf1.rect).
                                ## I found out that it will not work and a shadow of the previous surface. So I can pass
                                ## self.surf1.rect to this function when something inside the surf1 is changes not when
                                ## I move the surf1 itself.

        pass
