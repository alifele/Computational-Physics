import numpy as np



class Patient:

    def __init__(self):

        lambda_rel = 2
        lambda_phys = 1
        lambda_intern = 1

        self.org1 = {
            "name": "org1",
            "F": 1,
            "PS": 1,
            "V_total": 2,
            "V_v": 1,
            "V_int": 1,
            "k_on": 0,
            "k_off": 1,
            "lambda_intern": lambda_intern,
            "lambda_rel": lambda_rel,
            "lambda_phys": lambda_phys,
            "R0": 0,
            "K_on": 0, ## R*k_on
        }

        self.org2 = {
            "name": "org2",
            "F": 1,
            "PS": 1,
            "V_total": 2,
            "V_v": 1,
            "V_int": 1,
            "k_on": 0,
            "k_off": 1,
            "lambda_intern": lambda_intern,
            "lambda_rel": lambda_rel,
            "lambda_phys": lambda_phys,
            "R0": 0,
            "K_on": 0,  ## R*k_on
        }

        self.org3 = {
            "name": "org3",
            "F": 1,
            "PS": 0,
            "V_total": 2,
            "V_v": 1,
            "V_int": 1,
            "lambda_phys": lambda_phys,
        }

        self.Vein = {
            "name": "Vein",
            "F": 1,
            "V_v": 2,
            "lambda_phys": lambda_phys,
        }

        self.Art = {
            "name": "Art",
            "F": 2,
            "V_v": 3,
            "lambda_phys": lambda_phys,
        }

        self.Lungs = {
            "name": "Lungs",
            "F": 1,
            "PS": 1,
            "V_total": 3,
            "V_v": 2,
            "V_int": 1,
            "lambda_phys": lambda_phys,
        }

        self.receptorPositiveList = [self.org1, self.org2]
        self.receptorNegativeList = [self.org3]
        self.calculateTotalF()
        self.ArtVeinList = [self.Art, self.Vein]


        self.Organs = {
            "ArtVein": self.ArtVeinList,
            "Lungs": [self.Lungs],
            "RecNeg": self.receptorNegativeList,
            "RecPos": self.receptorPositiveList,
        }


    def calculateK_on(self):
        for elem in self.receptorPositiveList:
            elem["K_on"] = elem["k_on"] * elem["R0"]

    def calculateTotalF(self):
        F = 0.0
        for elem in self.receptorNegativeList:
            F += elem['F']
        for elem in self.receptorPositiveList:
            F += elem['F']

        self.Art['F'] = F
        self.Vein['F'] = F
        self.Lungs["F"] = F


class Therapy:  ## Note that this is a single therapy not the Therapy plan.

    ## This class will include the initial values of the H and C values in organs
    ## This will also include the time of injection and the profile of injection

    ## Profiles of Injection:
    ## 1. Bolus Injection
    ## 2. Exponential Injection (e^(-x))
    ## 3. Gaussian Injection
    ## 4. Multiple impulse injection (impulse train)

    ## Note that in each of these injection types, the solution that is getting injected is the same
    ## during the injection profile. But we can also have some other options like varying H-C during
    ## the injection.


    def __init__(self):
        self.injectionProfile = self.bolus ## possible options: bolus, exponential, gaussian, bolusTrain

        self.org1 = {
            "name": "org1",
            "P_v": 8,
            "P*_v": 9,
            "P_int": 0,
            "P*_int": 1,
            "RP": 2,
            "RP*": 3,
            "P_intern": 4,
            "P*_intern": 5
        }

        self.org2 = {
            "name": "org2",
            "P_v": 1,
            "P*_v": 1,
            "P_int": 1,
            "P*_int": 1,
            "RP": 1,
            "RP*": 1,
            "P_intern": 0,
            "P*_intern": 0
        }

        self.org3 = {
            "name": "org3",
            "P_v": 1,
            "P*_v": 2,
            "P_int": 3,
            "P*_int": 4
        }

        self.Art = {
            "name": "Art",
            "P": 0,
            "P*": 1,
        }

        self.Vein = {
            "name": "Vein",
            "P": 2,
            "P*": 3
        }

        self.Lungs = {
            "name": "Lungs",
            "P_v": 4,
            "P*_v": 5,
            "P_int": 6,
            "P*_int": 7,
        }

        self.receptorPositiveList = [self.org1, self.org2]
        self.ArtVeinList = [self.Art, self.Vein]
        self.receptorNegativeList = [self.org3]

        self.Organs = {
            "ArtVein": self.ArtVeinList,
            "Lungs": [self.Lungs],
            "RecNeg": self.receptorNegativeList,
            "RecPos": self.receptorPositiveList,
        }




    def bolus(self, t):
        if t == 0:
            return 10
        else:
            return 0


