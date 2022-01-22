from ReceptorNegativeOrgans import *
from ReceptorPositiveOrgans import *
from ComplexOrgans import *
from MasterOrgans import *
from SimpleOrgans import *
from initiator.Organ_init import *
from Patient_info import Patient_info
import matplotlib.pyplot as plt
import numpy as np


## TODO
# Redifne the value of k_on in compartments because in the supp. of the article it ueses k_on_nonl (in the diagrams)


## TODO
## In the differential equation of the Vein, the fact that lungs carries peptide away from the veins compartment is not included.
## Also, you need to note that in the sum, you must not include in lungs

## TODO
## There is an inconsistency in the units of the values used in the tables and in the differential equations.
## For example k_i values (which are used to calculate PS values) are reported in ml units. But on the other hand the
## values for volume of the organs are in units of L. You need to change the values and make their units consistent


## TODO
## There is some thing wrong with the Vein compartment. First it gets negative and then it gets very close to 0
## and kind of freezes there


class Patient:

    def __init__(self, Patient_info):



        self.patient_info = Patient_info


        #self.lambda_phy = np.log(2)/(6.647 * 3600 *
        self.lambda_phy = 7.23 * 1e-5 * 5000

        self.k_on = 0.04/0.5
        self.k_off = 0.04


        if self.patient_info.gender == "male":
            self.V_p = 2.8 * (1-self.patient_info.H) * self.patient_info.BSA
        else:
            self.V_p = 2.4 * (1 - self.patient_info.H) * self.patient_info.BSA

        self.F = 1.23 * self.V_p



        self.initial_values = {"P_vascular_unlabeled": 0,
                               "P_interestitial_unlabeled": 0,
                               "P_internalized_unlabeled": 0,
                               "P_interacellular_unlabeled": 0,  ## for kidney
                               "P_unlabeled": 0,  ## for Art and Vein
                               "P_vascular_labeled": 0,
                               "P_interestitial_labeled": 0,
                               "P_internalized_labeled": 0,
                               "P_interacellular_labeled": 0,  ## for kidney
                               "P_labeled": 0,
                               "RP_labeled": 0,
                               "RP_unlabeled": 0,
                               "PPR_labeled": 0,
                               "PPR_unlabeled": 0,
                               "R": 0}  ## for Art and Vein

        self.setSimParameters()
        self.setOrganVariables()
        self.setOrganParameters()
        self.setOrgans()

    def setSimParameters(self):
        tmax = 50
        level = 13
        N_t = np.power(2, level)
        dt = tmax / (N_t-1)
        self.simParameters = {"tmax": tmax,
                              "level": level,
                              "N_t": N_t,
                              "dt": dt}
        self.tList = np.linspace(0,tmax,N_t)

    def setOrganVariables(self):
        self.Brain_var = self.initial_values.copy()
        self.Heart_var = self.initial_values.copy()
        self.Bone_var = self.initial_values.copy()
        self.Skin_var = self.initial_values.copy()
        self.Adipose_var = self.initial_values.copy()
        self.Lungs_var = self.initial_values.copy()

        self.Liver_var = self.initial_values.copy()
        self.Spleen_var = self.initial_values.copy()
        self.Tumor_var = self.initial_values.copy()
        self.RedMarrow_var = self.initial_values.copy()
        self.GI_var = self.initial_values.copy()
        self.Muscle_var = self.initial_values.copy()
        self.ProstateUterus_var = self.initial_values.copy()
        self.Adrenals_var = self.initial_values.copy()
        self.Rest_var = self.initial_values.copy()

        self.Kidney_var = self.initial_values.copy()

        self.Art_var = self.initial_values.copy()
        self.Vein_var = self.initial_values.copy()

        self.BloodProteinComplex_var = self.initial_values.copy()

    def setOrganParameters(self):

        ## Receptor Positive Organs
        self.Liver_param = None
        self.Tumor_param = None
        self.Spleen_param = None
        self.RedMarrow_param = None
        self.GI_param = None
        self.Muscle_param = None
        self.ProstateUterus_param = None
        self.Adrenal_param = None

        ### Receptor Negative Organs
        self.Brain_param = None
        self.Heart_param = None
        self.Bone_param = None
        self.Skin_param = None
        self.Adipose_param = None
        self.Lungs_param = None


        ### Complex Compartment Organs
        self.Kidney_param = None

        ### Master Compartment Organs
        self.Art_param = None
        self.Vein_param = None
        self.Rest_param = None

        ### Simple Compartment Organs
        self.BloodProteinComplex_param = None


    def setOrgans(self):

        Tumor_init(self)
        Liver_init(self)
        Spleen_init(self)
        Kidney_init(self)
        RedMarrow_init(self)
        GI_init(self)
        Muscle_init(self)
        ProstateUterus_init(self)
        BloodProteinComplex_init(self)


        #Brain_init(self)
        Heart_init(self)
        Bone_init(self)
        Skin_init(self)
        Adipose_init(self)
        Lungs_init(self)




        # self.Brain = Brain(self.Brain_param, self.Brain_var, self.simParameters)
        self.Heart = Heart(self.Heart_param, self.Heart_var, self.simParameters)
        self.Bone = Bone(self.Bone_param, self.Bone_var, self.simParameters)
        self.Skin = Skin(self.Skin_param, self.Skin_var, self.simParameters)
        self.Adipose = Adipose(self.Adipose_param, self.Adipose_var, self.simParameters)
        self.Lungs = Lungs(self.Lungs_param, self.Lungs_var, self.simParameters)
        #
        self.Liver = Liver(self.Liver_param, self.Liver_var, self.simParameters)
        self.Spleen = Spleen(self.Spleen_param, self.Spleen_var, self.simParameters)
        self.Tumor = Tumor(self.Tumor_param, self.Tumor_var, self.simParameters)
        self.RedMarrow = RedMarrow(self.RedMarrow_param, self.RedMarrow_var, self.simParameters)
        self.GI = GI(self.GI_param, self.GI_var, self.simParameters)
        self.Muscle = Muscle(self.Muscle_param, self.Muscle_var, self.simParameters)
        self.ProstateUterus = ProstateUterus(self.ProstateUterus_param, self.ProstateUterus_var, self.simParameters)
        self.Kidney = Kidney(self.Kidney_param, self.Kidney_var, self.simParameters)
        self.BloodProteinComplex = BloodProteinComplex(self.BloodProteinComplex_param, self.BloodProteinComplex_var, self.simParameters)



        # self.OrgansList = [self.Brain, self.Heart, self.Bone, self.Skin, self.Adipose,
        #                    self.Lungs, self.Liver, self.Spleen, self.Tumor, self.RedMarrow,
        #                    self.GI, self.ProstateUterus, self.Kidney, self.BloodProteinComplex]
        # self.OrgansList = [self.Lungs]

        self.OrgansList = [self.Heart, self.Bone, self.Skin, self.Adipose,
                           self.Lungs, self.Liver, self.Spleen, self.Tumor, self.RedMarrow,
                           self.GI, self.ProstateUterus, self.Kidney, self.BloodProteinComplex]

        Rest_init(self)
        self.Rest = Rest(self.Rest_param, self.Rest_var, self.simParameters)
        self.OrgansList.append(self.Rest)

        Vein_init(self)
        Art_init(self)
        self.Art = Art(self.Art_param, self.Art_var, self.simParameters, self.OrgansList)
        self.Vein = Vein(self.Vein_param, self.Vein_var, self.simParameters, self.OrgansList)


        for Organ in self.OrgansList:  ## Adding the Vein and Areterial information to Organs
            Organ.Set_ArtVein(self.Art, self.Vein)

        self.OrgansList.append(self.Vein)
        self.OrgansList.append(self.Art)

    def Run(self):


        for i, t in enumerate(self.tList):


            self.Lungs.Calculate(i)
            self.Art.Calculate(i)

            for organ in self.OrgansList:
                if organ.name == "Lungs" or organ.name == "Vein" or organ.name == "Art":
                    continue

                organ.Calculate(i)

            self.Vein.Calculate(i)


if __name__ == "__main__":
    patient = Patient(Patient_info)
    patient.Run()
    # plt.plot(patient.Vein.PList.P_unlabeled); plt.show()
    plt.plot(patient.Vein.PList.P_unlabeled);plt.show()
    print("Done")
