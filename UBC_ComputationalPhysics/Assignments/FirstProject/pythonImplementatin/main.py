from sys import exit
from sketch import *
from Compute import *

pygame.init()
sketch = Sketch()
sketch.setup()

StarsX, CoresX = Compute()
t = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    sketch.update(StarsX, CoresX, t)
    t+=1
    t = t % StarsX.shape[-1]
    pygame.time.delay(5)
    print(t)
