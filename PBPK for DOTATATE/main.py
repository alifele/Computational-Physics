from ReceptorNegativeOrgans import *
from ReceptorPositiveOrgans import *
from ComplexOrgans import *
from MasterOrgans import *
from SimpleOrgans import *

import numpy as np

#TODO Storing the values of variables in list in following compartments: Master
#TODO Adding the differential equations of Vein and Art (Master Compartment)


## TODO the amount of P and P* should first saved in an auxilary variable and then the origian vlaues get updated

class Main:

    def __init__(self):
        self.lambda_phy = 0
        self.initial_values = {"P_vascular_unlabeled": 0,
                               "P_interstitial_unlabeled": 0,
                               "P_internalized_unlabeled": 0,
                               "P_interacellular_unlabeled": 0,  ## for kidney
                               "P_unlabeled": 0,  ## for Art and Vein
                               "P_vascular_labeled": 0,
                               "P_interstitial_labeled": 0,
                               "P_internalized_labeled": 0,
                               "P_interacellular_labeled": 0,  ## for kidney
                               "P_labeled": 0,
                               "PPR_labeled": 0,
                               "PPR_unlabeled": 0}  ## for Art and Vein


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
        self.Brain_var = self.initial_values
        self.Heart_var = self.initial_values
        self.Bone_var = self.initial_values
        self.Skin_var = self.initial_values
        self.Adipose_var = self.initial_values
        self.Lungs_var = self.initial_values

        self.Liver_var = self.initial_values
        self.Spleen_var = self.initial_values
        self.Tumor_var = self.initial_values
        self.RedMarrow_var = self.initial_values
        self.GI_var = self.initial_values
        self.Muscle_var = self.initial_values
        self.ProstateUterus_var = self.initial_values
        self.Adrenals_var = self.initial_values
        self.Rest_var = self.initial_values

        self.Kidney_var = self.initial_values

        self.Art_var = self.initial_values
        self.Vein_var = self.initial_values

        self.BloodProteinComplex_var = self.initial_values

    def setOrganParameters(self):
        ### Receptor Negative Organs
        self.Brain_param = {"F": 0,
                           "V_v": 0,
                           "PS": 0,
                           "V_int": 0,
                           "lambda_phy": self.lambda_phy}
        #
        # self.Heart_param
        # self.Bone_param
        # self.Skin_param
        # self.Asipose_param
        # self.Lungs_param

        ### Receptor Positive Organs
        self.Liver_param = {"F": 0,
                            "V_v": 0,
                            "PS": 0,
                            "V_int": 0,
                            "k_on": 0,
                            "k_off": 0,
                            "lambda_int": 0,
                            "lambda_rel": 0,
                            "lambda_phy": self.lambda_phy}
        # self.Spleen_param
        # self.Tumor_param
        # self.RedMarrow_param
        # self.GI_param
        # self.Muscle_param
        # self.ProstateUterus_param
        # self.Adrenal_param
        # self.Rest_param

        ### Complex Compartment Organs
        self.Kidney_param = {"F": 0,
                             "V_v": 0,
                             "PS": 0,
                             "V_int": 0,
                             "k_on": 0,
                             "k_off": 0,
                             "lambda_int": 0,
                             "lambda_rel": 0,
                             "lambda_phy": self.lambda_phy,
                             "GFR": 0,
                             "theta": 0,
                             "f_ecx": 0}

        ### Master Compartment Organs
        self.Art_param = {"F": 0,
                          "V": 0}
        # self.Vein_param =


        ### Simple Compartment Organd
        self.BloodProteinComplex_par = {"K_pr":0}

    def setOrgans(self):
        self.Brain = Brain(self.Brain_param, self.Brain_var, self.simParameters)
        # self.Heart = 0
        # self.Bone = 0
        # self.Skin = 0
        # self.Adipose = 0
        # self.Lungs = 0

        self.Liver = Liver(self.Liver_param, self.Liver_var, self.simParameters)
        # self.Spleen = 0
        # self.Tumor = 0
        # self.RedMarrow = 0
        # self.GI = 0
        # self.Muscle = 0
        # self.ProstateUterus = 0
        # self.Rest = 0

        self.Kidney = Kidney(self.Kidney_param, self.Liver_var, self.simParameters)

        self.PlasmaProteinComplex = BloodPlasmaProteinComplex(self.Kidney_param, self.Liver_var, self.simParameters)


        self.OrgansList = [self.Brain, self.Heart, self.Bone, self.Skin, self.Adipose,
                           self.Lungs, self.Liver, self.Spleen, self.Tumor, self.RedMarrow,
                           self.GI, self.ProstateUterus, self.Rest, self.Kidney, self.PlasmaProtein]


        self.Art = Art(self.Art_param, self.Art_var, self.simParameters, self.OrgansList)
        # self.Vein = 0

        for Organ in self.OrgansList:  ## Adding the Vein and Areterial information to Organs
            Organ.Set_ArtVein(self.Art, self.Vein)


if __name__ == "__main__":
    PBPK_model = Main()
