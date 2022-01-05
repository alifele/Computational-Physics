import numpy as np


class FreePeptide:
    def __init__(self):
        self.vascular_unlabeled = 0
        self.interestitial_unlabeled = 0
        self.internalized_unlabeled = 0
        self.interacellular_unlabeled = 0

        self.vascular_labeled = 0
        self.interestitial_labeled = 0
        self.internalized_labeled = 0
        self.interacellular_labeled = 0

        self.P_labeled = 0  ## This will be used for element of the master compartment (Arteries and Veins)
                              ## the reason that I defined it separately is that the Arteries and Veins do not have
                              ## separate internal sub compartments (intracellular, interstitial, vascular. SSTR2, etc)
        self.P_unlabeled = 0

class FreePeptideList:
    def __init__(self, N):
        self.vascular_unlabeled = np.zeros(N, dtype='float')
        self.interestitial_unlabeled = np.zeros(N, dtype='float')
        self.internalized_unlabeled = np.zeros(N, dtype='float')
        self.interacellular_unlabeled = np.zeros(N, dtype='float')

        self.vascular_labeled = np.zeros(N, dtype='float')
        self.interestitial_labeled = np.zeros(N, dtype='float')
        self.internalized_labeled = np.zeros(N, dtype='float')
        self.interacellular_labeled = np.zeros(N, dtype='float')


        self.P_labeled = np.zeros(N, dtype='float')
        self.P_unlabeled = np.zeros(N, dtype='float')
