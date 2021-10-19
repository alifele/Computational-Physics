import numpy as np
from InitiateCores import *
from InitiateStars import *


def Compute():
    tmax = 25
    l = 10
    N_timeSteps = np.power(2, l)
    dt = tmax / N_timeSteps

    params = {'dt': dt}


    NStars1 = 100
    NStars2 = 100
    NStars = NStars1 + NStars2
    NCores = 2

    StarsX = np.zeros((NStars, 3, N_timeSteps), dtype='float')
    CoresX = np.zeros((NCores, 3, N_timeSteps), dtype='float')

    StarsV0 = np.zeros((NStars, 3), dtype='float')
    CoresV0 = np.zeros((NCores, 3), dtype='float')

    StarsTimeCut = np.zeros((NStars, 3), dtype='float')
    CoresTimeCut = np.zeros((NCores, 3), dtype='float')

    initiateCores(CoresTimeCut, CoresV0)
    initiateStars(StarsTimeCut, StarsV0, CoresTimeCut, NStars1, NStars2, CoresV0)

    # for t in range(N_timeSteps):
    #     for star in range(NStars):
    #         StarsX[star,:,t] = np.random.random(3)
    #
    #     for core in range(NCores):
    #         CoresX[core,:,t] = np.random.random(3)
    initiateFirstTwoStepsStars(StarsX, StarsTimeCut, StarsV0, dt)
    initiateFirstTwoStepsCores(CoresX, CoresTimeCut, CoresV0, dt)

    for t in range(1, N_timeSteps-1):
        moveStars(StarsX, CoresX, params,t)
        moveCores(CoresX, params,t)

    print('calculation Done')

    return StarsX, CoresX


def moveStars(StarsX, CoresX, params,t):
    m = 1
    for star in range(StarsX.shape[0]):
        X = StarsX[star, :, t]
        Xpre = StarsX[star, :, t - 1]
        acceleration = 0
        for core in range(CoresX.shape[0]):
            Xj = CoresX[core, :, t]
            r = Xj - X + 0.01
            acceleration += m*((r) / (np.linalg.norm(r)**3+0.005))

        XNew = acceleration * params['dt'] ** 2 + 2 * X - Xpre
        StarsX[star, :, t + 1] = XNew


def moveCores(CoresX, params,t):
    m=1
    for core_i in range(CoresX.shape[0]):
        X = CoresX[core_i, :, t]
        Xpre = CoresX[core_i, :, t - 1]
        acceleration = 0
        for core_j in range(CoresX.shape[0]):
            if core_i != core_j:
                Xj = CoresX[core_j, :, t]
                r = Xj - X + 0.01
                acceleration += m*((r) / (np.linalg.norm(r) ** 3+0.005))

        XNew = acceleration * params['dt'] ** 2 + 2 * X - Xpre
        CoresX[core_i, :, t + 1] = XNew





def initiateFirstTwoStepsStars(StarsX, StarsTimeCut, StarsV0,dt):
    for star in range(StarsX.shape[0]):
        StarsX[star,:,0] = StarsTimeCut[star,:]
        StarsX[star,:,1] = StarsX[star,:,0] + StarsV0[star]*dt

def initiateFirstTwoStepsCores(CoresX, CoresTimeCut, CoresV0, dt):
    for core in range(CoresX.shape[0]):
        CoresX[core, :, 0] = CoresTimeCut[core,:]
        CoresX[core,:,1] = CoresX[core, :,0] + CoresV0[core]*dt


## Once I had the idea to calculat the force matrix. But then I realized that
## using that technique in the simulation won't be good. Because the stars are
## not appling any force on the cores and that is the reason that the star-core
## force matrix is not symetric. So I chose to calculat the force and update the
## position of the elements on the fly.

#
# def calculateStarCoreMatrix(StarsTimeCut): #Calculate the force to stars fron Cores
#     pass
#
#
# def calculateCoreCoreMatrix(): # Calculate the force from cores to cores
