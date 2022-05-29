import numpy as np



class Patient2:

    def __init__(self):

        F = 1
        k_on = 0.5
        k_off = 0.5
        lambda_phys = 0.1
        lambda_rel = 0.001
        lambda_intern = 10

        self.Tumor = {
            "name": "Tumor",
            "F": 0.45*F,
            "PS": 1,
            "V_total": 1,
            "V_v": 0.1,
            "V_int": 0.2,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": lambda_intern,
            "lambda_rel": lambda_rel,
            "lambda_phys": lambda_phys,
            "R0": 2,
            "K_on": 0, ## R*k_on
        }

        ##
        ####
        ######
        ######## Bone initialization
        self.Bone = {
            "name": "Bone",
            "F": 0.3*F,
            "PS": 1,
            "V_total": 1,
            "V_v": 0.2,
            "V_int": 0.3,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Lungs initialization

        self.Lungs = {
            "name": "Lungs",
            "F": F,  # The real value will be calculated once we have the
            ## the flow of each organ. The Vein and Art flow is the sum of all flows
            "PS": 1,
            "V_total": 2,
            "V_v": 1,
            "V_int": 0.5,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Vein initialization
        F_Vein = F
        self.Vein = {
            "name": "Vein",
            "F": F_Vein,  ## The real value will be calculated once we have the
            ## the flow of each organ. The Vein and Art flow is the sum of all
            ## flows
            "V_v": 1,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Art initialization
        F_Art = F
        self.Art = {
            "name": "Art",
            "F": F_Art,  ## The real value will be calculated once we have the
            ## the flow of each organ. The Vein and Art flow is the sum of all flows
            "V_v": 1,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Rest initialization
        self.Rest = {
            "name": "Rest",
            "F": 0,
            "PS": 1,
            "V_total": 1,
            "V_v": 0.4,
            "V_int": 0.1,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": lambda_intern,
            "lambda_rel": lambda_rel,
            "lambda_phys": lambda_phys,
            "R0": 1.5,
            "K_on": 0,  ## R*k_on
        }




        self.receptorPositiveList = [self.Tumor]
        self.KidneyList = []
        self.LungsList = [self.Lungs]
        self.receptorNegativeList = [self.Bone]
        self.ArtVeinList = [self.Art, self.Vein]

        self.calculateK_on()    ## Will calculate K_on = k_on * R0 for RecPos and Kidney

        self.Organs = {
            "ArtVein": self.ArtVeinList,
            "Lungs": self.LungsList,
            "RecNeg": self.receptorNegativeList,
            "RecPos": self.receptorPositiveList,
            "Kidney": self.KidneyList,
        }

        self.addRestOrgan(F, k_on, k_off, lambda_phys, lambda_rel,lambda_intern)


    def calculateK_on(self):
        for elem in self.receptorPositiveList:
            elem["K_on"] = 0
        for elem in self.KidneyList:
            elem["K_on"] = 0


    def addRestOrgan(self, F, k_on, k_off, lambda_phys, lambda_rel,lambda_intern):
        typeList = ["RecNeg", "RecPos", "Kidney"]
        F_allOrgans = 0
        V_total_allOrgans = 0
        V_v_allOrgans = 0
        for type in typeList:
            organsList = self.Organs[type]
            for organ in organsList:
                F_allOrgans += organ["F"]
                V_total_allOrgans += organ["V_total"]
                V_v_allOrgans += organ["V_v"]

        F_rest = F - F_allOrgans

        self.Rest = {
            "name": "Rest",
            "F": F_rest,
            "PS": 1,
            "V_total": 2,
            "V_v": 0.1,
            "V_int": 0.8,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": lambda_intern,
            "lambda_rel": lambda_rel,
            "lambda_phys": lambda_phys,
            "R0": 2,
            "K_on": 0,  ## R*k_on
        }
        self.receptorPositiveList.append(self.Rest)




    def calculateTotalF(self):
        F = 0.0
        for elem in self.receptorNegativeList:
            F += elem['F']
        for elem in self.receptorPositiveList:
            F += elem['F']
        for elem in self.KidneyList:
            F += elem["F"]

        self.Art['F'] = F
        self.Vein['F'] = F
        self.Lungs["F"] = F
