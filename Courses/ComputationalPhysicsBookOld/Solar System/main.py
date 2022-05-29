from sys import exit
from sketch import *

g_real = 10  # m/s^2
L_real = 10  # m
t_max = 120  # s
dt_real = 0.005  # s

theta_real = 0.2  # theta
velocity_real = 0  # degree/sec
FD_real = 1.2  # 1/s^2
q_real = 0.5  # 1/s^2
Omega_real = 2 / 3  # 1/s^2

myEnv = Env(1, (L_real / g_real) ** 0.5, 1)  # length, time, mass

pygame.init()
sketch = Sketch()
sketch.setup()
t = 0
dt = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    t += dt
    sketch.update(t)
