import pygame
import pygame.surface
from pygame.locals import *
import numpy as np



## In general we have two methods to add a surface to the main screen. One method is by using sprite objects (which you
## can find its implementation here. And the other method, which you can find it in the other folder, is by creating and
## manipulating the surface objects directly (which out using the high level classes like sprite that do things behind
## the curtains!

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.surface = pygame.Surface([30, 30])
        self.surface.fill((255, 255, 255))


        pygame.draw.rect(self.surface, (54, 125, 247), pygame.Rect(5, 5, 15, 15))
        self.rect = self.surface.get_rect()     ## this will return rect(0,0,width, height). This is the properties of
                                                ## The this surface. The default value for position is [0,0].
                                                ## So we need to set it to the position we want. Note that we can
                                                ## store the coordinates of this surface in even an numpy array. But it
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

        self.allSpritsList = pygame.sprite.Group()  ## In order to have different layers, we can
                                                    ## put sprites in each group in a common group. All of these things
                                                    ## can be done manually by creating and manipulating the surface
                                                    ## object directly. You can find that implementation in the other
                                                    ## folder.

        self.surf1 = Sprite(np.array([50,20]))
        self.allSpritsList.add(self.surf1)

        pygame.display.update()

    def draw(self):

        self.screen.fill((15, 50, 70))
        #self.pos += np.random.randint(-0,2, size=2)
        self.surf1.move(np.random.randint(-2,0, size=2))

        #self.allSpritsList.update()    ## default implementation does nothing. However we can over
                                        ## over ride this function for sprites
        self.allSpritsList.draw(self.screen)

        pygame.display.update()
        pass
