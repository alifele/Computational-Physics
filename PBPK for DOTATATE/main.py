<<<<<<< HEAD
from ReceptorNegativeOrgans import *
import numpy as np


class Main:

    def __init__(self):
        self.lambda_phy = 0
        self.initial_values = {"P_vascular_unlabeled": 0,
                               "P_interstitial_unlabeled": 0,
                               "P_internalized_unlabeled": 0,
                               "P_interacellular_unlabeled": 0,
                               "P_vascular_labeled": 0,
                               "P_interstitial_labeled": 0,
                               "P_internalized_labeled": 0,
                               "P_interacellular_labeled": 0}

        self.tmax = simParameters["tmax"]
        self.level = simParameters["level"]
        self.N_t = simParameters["N_t"]
        self.N_t = np.power(2, self.level)
        self.dt = self.tmax / self.N_t
        self.simParameters = {"tmax": 0,
                              "level": 0}

        self.setOrganParameters()
        self.setOrganVariables()
        self.setSimParameters()
        self.setOrgans()

    def setSimParameters(self):
        tmax = 0
        level = 0
        N_t = np.power(2, level)
        dt = tmax / N_t
        self.simParameters = {"tmax": tmax,
                              "level": level,
                              "N_t": N_t,
                              "dt": dt}

    def setOrganVariables(self):
        self.BrainVariables = self.initial_values
        self.HeartVariables = self.initial_values
        self.BoneVariables = self.initial_values
        self.SkinVariables = self.initial_values
        self.AdiposeVariables = self.initial_values
        self.LungsVariables = self.initial_values

    def setOrganParameters(self):
        self.Bone_param = {"F": 0,
                           "V_v": 0,
                           "PS": 0,
                           "V_int": 0,
                           "lambda_phy": self.lambda_phy,
                           "F_ART": 0}

        self.Heart_param = {"F": 0,
                            "V_v": 0,
                            "PS": 0,
                            "V_int": 0,
                            "lambda_phy": self.lambda_phy,
                            "F_ART": 0}

        self.Brain_param = {"F": 0,
                            "V_v": 0,
                            "PS": 0,
                            "V_int": 0,
                            "lambda_phy": self.lambda_phy,
                            "F_ART": 0}

        self.Skin_param = {"F": 0,
                           "V_v": 0,
                           "PS": 0,
                           "V_int": 0,
                           "lambda_phy": self.lambda_phy,
                           "F_ART": 0}

        self.Asipose_param = {"F": 0,
                              "V_v": 0,
                              "PS": 0,
                              "V_int": 0,
                              "lambda_phy": self.lambda_phy,
                              "F_ART": 0}

        self.Lungs_param = {"F": 0,
                            "V_v": 0,
                            "PS": 0,
                            "V_int": 0,
                            "lambda_phy": self.lambda_phy,
                            "F_ART": 0}

    def setOrgans(self):
        self.Brain = Brain(self.Brain_param, self.BrainVariables)


if __name__ == "__main__":
    PBPK_model = Main()
=======
import numpy as np
import matplotlib.pyplot as plt
>>>>>>> c09c847e7d5b5beb328c1bccdad0495350f7e63f
