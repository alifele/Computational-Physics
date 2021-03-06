

class Therapy2:  ## Note that this is a single therapy not the Therapy plan.

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


    def __init__(self, i):
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

        self.Rest = {
            "name": "Rest",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0,
            "RP": 0,
            "RP*": 0,
            "P_intern": 0,
            "P*_intern": 0
        }


        self.Bone = {
            "name": "Bone",
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

        self.receptorPositiveList = [self.Tumor, self.Rest]
        self.KidneyList = []
        self.receptorNegativeList = [self.Bone]
        self.ArtVeinList = [self.Art, self.Vein]

        self.Organs = {
            "ArtVein": self.ArtVeinList,
            "Lungs": [self.Lungs],
            "RecNeg": self.receptorNegativeList,
            "RecPos": self.receptorPositiveList,
            "Kidney": self.KidneyList,
        }



        constantInjection60 = {
            "type": "constant",    ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "t0": 0,
            "tf": 60,
            "totalAmountHot": 10,
            "totalAmountCold": 90
        }

        constantInjection120 = {
            "type": "constant",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "t0": 0,
            "tf": 120,
            "totalAmountHot": 10,
            "totalAmountCold": 90
        }

        constantInjection180 = {
            "type": "constant",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "t0": 0,
            "tf": 180,
            "totalAmountHot": 10,
            "totalAmountCold": 90
        }

        constantInjection240 = {
            "type": "constant",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "t0": 0,
            "tf": 240,
            "totalAmountHot": 10,
            "totalAmountCold": 90
        }

        constantInjection300 = {
            "type": "constant",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "t0": 0,
            "tf": 300,
            "totalAmountHot": 10,
            "totalAmountCold": 90
        }

        constantInjection360 = {
            "type": "constant",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "t0": 0,
            "tf": 360,
            "totalAmountHot": 10,
            "totalAmountCold": 90
        }

        bolusInjection = {
            "type": "bolus",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "t0": 0,
            "totalAmountHot": 1000,   ## nmol
            "totalAmountCold": 900   ## nmol
        }

        bolusTrainInjection2 = {
            "type": "bolusTrain",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "N": 2,
            "t": [0,360],
            "totalAmountHot": 10,
            "totalAmountCold": 90
        }

        bolusTrainInjection3 = {
            "type": "bolusTrain",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "N": 3,
            "t": [0, 180, 360],
            "totalAmountHot": 10,
            "totalAmountCold": 90
        }

        bolusTrainInjection4 = {
            "type": "bolusTrain",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "N": 4,
            "t": [0, 120, 240, 360],
            "totalAmountHot": 10,
            "totalAmountCold": 90
        }

        bolusTrainInjection5 = {
            "type": "bolusTrain",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "N": 5,
            "t": [0, 90, 180, 270, 360],
            "totalAmountHot": 10,
            "totalAmountCold": 90
        }

        bolusTrainInjection6 = {
            "type": "bolusTrain",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "N": 6,
            "t": [0, 72, 144, 216, 288, 360],
            "totalAmountHot": 10,
            "totalAmountCold": 90
        }

        bolusTrainInjection7 = {
            "type": "bolusTrain",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "N": 7,
            "t": [0, 10, 20, 30, 40, 3000, 3600],
            "totalAmountHot": 1000,
            "totalAmountCold": 900
        }

        injectionProfileList = [constantInjection60, constantInjection120, constantInjection180, constantInjection240,
                                constantInjection300, constantInjection360, bolusInjection, bolusTrainInjection2, bolusTrainInjection3,
                                bolusTrainInjection4, bolusTrainInjection5, bolusTrainInjection6, bolusTrainInjection7]

        # self.injectionProfile = injectionProfileList[i]
        self.injectionProfile = bolusInjection


