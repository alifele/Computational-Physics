import numpy as np


def initiateCores(CoresTimeCut, CoresV0):
    CoresTimeCut[0] = np.array([-1,1.6,0], dtype='float')
    CoresV0[0] = np.array([0.25,0,0], dtype='float')

    CoresTimeCut[1] = np.array([1, -1.6, 0], dtype='float')
    CoresV0[1] = np.array([-0.25, 0, 0], dtype='float')

    