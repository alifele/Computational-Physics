import numpy as np



class Patient:

    org1 = {
        "F": 0,
        "PS": 0,
        "V_total": 0,
        "V_v": 0,
        "V_int": 0,
        "V_intra": 0,
        "k_on": 0,
        "K_off": 0,
        "lambda_int": 0,
        "lambda_rel": 0,
        "R": 0
    }

    Vein = {
        "F": 0,
        "V_total": 0,
    }

    Art = {
        "F": 0,
        "V_total": 0
    }

    Lungs = {
        "F": 0,
        "PS": 0,
        "V_total": 0,
        "V_v": 0,
        "V_int": 0,
    }


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
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0,
            "RP": 0,
            "RP*": 0,
            "P_inter": 0,
            "P*_inter": 0
        }

        # self.org2 = {
        #     "name": "org2",
        #     "P_v": 0,
        #     "P*_v": 0,
        #     "P_int": 0,
        #     "P*_int": 0,
        #     "RP": 0,
        #     "RP*": 0,
        #     "P_inter": 0,
        #     "P*_inter": 0
        # }

        self.Art = {
            "name": "Art",
            "P": 0,
            "P*": 0,
        }

        self.Vein = {
            "name": "Vein",
            "P": 0,
            "P*": 0
        }

        self.Lungs = {
            "name": "Lungs",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0,
        }

        self.receptorPositiveList = [self.org1]
        self.ArtVeinList = [self.Art, self.Vein]
        self.receptorNegativeList = []

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


