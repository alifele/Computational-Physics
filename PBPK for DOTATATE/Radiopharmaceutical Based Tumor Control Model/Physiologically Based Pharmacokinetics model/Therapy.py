

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


        self.Tumor = {
            "name": "Tumor",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0,
            "RP": 0,
            "RP*": 0,
            "P_intern": 0,
            "P*_intern": 0
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

        self.Kidney = {
            "name": "Kidney",
            "P_v": 0,
            "P*_v": 0,
            "P_intra": 0,
            "P*_intra": 0,
            "P_int": 0,
            "P*_int": 0,
            "RP": 0,
            "RP*": 0,
            "P_intern": 0,
            "P*_intern": 0
        }

        self.Skin = {
            "name": "Skin",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0
        }

        self.Art = {
            "name": "Art",
            "P": 0,
            "P*": 0,
        }

        # self.Vein = {
        #     "name": "Vein",
        #     "P": 0.5* 1e-5,             ## nmol
        #     "P*": 0.5* 1e-5             ## nmol
        # }

        self.Vein = {
            "name": "Vein",
            "P": 0,  ## nmol
            "P*": 0  ## nmol
        }

        self.Lungs = {
            "name": "Lungs",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0,
        }

        self.receptorPositiveList = [self.Tumor]
        self.KidneyList = [self.Kidney]
        self.receptorNegativeList = [self.Skin]
        self.ArtVeinList = [self.Art, self.Vein]

        self.Organs = {
            "ArtVein": self.ArtVeinList,
            "Lungs": [self.Lungs],
            "RecNeg": self.receptorNegativeList,
            "RecPos": self.receptorPositiveList,
            "Kidney": self.KidneyList,

        }

        constantInjection = {
            "type": "constant",    ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "t0": 0,
            "tf": 10,
            "totalAmountHot": 10,
            "totalAmountCold": 10
        }

        bolusInjection = {
            "type": "bolus",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "t0": 5,
            "totalAmountHot": 10,
            "totalAmountCold": 10
        }

        bolusTrainInjection = {
            "type": "bolusTrain",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "N": 2,
            "t": [0, 10],
            "totalAmountHot": 5,
            "totalAmountCold": 10
        }

        self.injectionProfile = constantInjection



