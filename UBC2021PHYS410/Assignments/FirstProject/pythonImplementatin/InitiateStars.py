import numpy as np

def initiateStars(StarsTimeCut, StarsV0, CoresTimeCut, NStars1, NStars2, CoresV0):

    rmax = 0.625
    rmin = 0.3
    vcoeff = 1

    for i in range(NStars1):
        theta = np.random.random() * np.pi * 2
        r = rmax * np.random.random() + rmin
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        z = 0
        vmax = vcoeff*np.sqrt(1 / r)
        vx = -vmax * np.sin(theta)
        vy = vmax * np.cos(theta)
        vz = 0
        StarsTimeCut[i] = np.array([x, y, z]) + CoresTimeCut[0,:]
        StarsV0[i] = np.array([vx, vy, vz]) + CoresV0[0,:]



    for j in range(NStars2):
        k = j+i+1
        theta = np.random.random() * np.pi * 2
        r = rmax * np.random.random() + rmin
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        z = 0
        vmax = vcoeff*np.sqrt(1 / r)
        vx = -vmax * np.sin(theta)
        vy = vmax * np.cos(theta)
        vz = 0
        StarsTimeCut[k] = np.array([x, y, z]) + CoresTimeCut[1,:]
        StarsV0[k] = np.array([vx, vy, vz]) + CoresV0[1,:]

    #
    # for i, star in enumerate(StarsTimeCut):
    #     theta = np.random.random()*np.pi*2
    #     r = rmax * np.random.random() + 0.5
    #     x = r * np.cos(theta)
    #     y = r * np.sin(theta)
    #     z = 0
    #     vmax = np.sqrt(1/r)
    #     vx = -vmax*np.sin(theta)
    #     vy = vmax*np.cos(theta)
    #     vz = 0
    #     StarsTimeCut[i] = np.array([x,y,z])
    #     StarsV0[i] = np.array([vx,vy,vz])


