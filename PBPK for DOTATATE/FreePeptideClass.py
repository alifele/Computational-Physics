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