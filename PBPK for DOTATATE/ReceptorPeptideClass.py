import numpy as np


class ReceptorPeptide:
    def __init__(self):
        self.RP_labeled = 0
        self.RP_unlabeled = 0
        self.R = 0

        ## for blood protein peptide complex
        self.PPR_labeled = 0
        self.PPR_unlabeled = 0


class ReceptorPeptideList:
    def __init__(self,N):
        self.RP_labeled = np.zeros(N, dtype="float")
        self.RP_unlabeled = np.zeros(N, dtype='float')
        self.R = np.zeros(N, dtype='float')

        self.PPR_labeled = np.zeros(N, dtype="float")
        self.PPR_labeled = np.zeros(N, dtype="float")