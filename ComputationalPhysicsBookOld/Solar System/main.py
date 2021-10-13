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

position = theta_real
velocity = velocity_real * myEnv.SI2Sim(1,'length')/myEnv.SI2Sim(1,'time')
q = q_real * (1/myEnv.SI2Sim(1,'time')**2)
FD = FD_real * (1/myEnv.SI2Sim(1,'time')**2)
g = g_real * myEnv.SI2Sim(1, 'length')/myEnv.SI2Sim(1, "time")**2
dt = myEnv.SI2Sim(dt_real, 'time')
l = L_real * myEnv.SI2Sim(1,'length')
tmax_simulation =  myEnv.SI2Sim(t_max, 'time')
Omega = Omega_real / myEnv.SI2Sim(1,'time')

parameters = dict()
parameters['q'] = q
parameters['FD'] = FD
parameters['g'] = g
parameters['dt'] = dt
parameters['l'] = l
parameters['Omega'] = Omega
parameters['tmax_simulation'] = tmax_simulation
parameters['env'] = myEnv

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
    print(t)
