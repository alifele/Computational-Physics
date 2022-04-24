

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

        self.Spleen = {
            "name": "Spleen",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0,
            "RP": 0,
            "RP*": 0,
            "P_intern": 0,
            "P*_intern": 0
        }

        self.Liver = {
            "name": "Liver",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0,
            "RP": 0,
            "RP*": 0,
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

        self.RedMarrow = {
            "name": "RedMarrow",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0,
            "RP": 0,
            "RP*": 0,
            "P_intern": 0,
            "P*_intern": 0
        }

        self.GI = {
            "name": "GI",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0,
            "RP": 0,
            "RP*": 0,
            "P_intern": 0,
            "P*_intern": 0
        }

        self.Muscle = {
            "name": "Muscle",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0,
            "RP": 0,
            "RP*": 0,
            "P_intern": 0,
            "P*_intern": 0
        }

        self.ProstateUterus = {
            "name": "ProstateUterus",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0,
            "RP": 0,
            "RP*": 0,
            "P_intern": 0,
            "P*_intern": 0
        }

        self.Adrenals = {
            "name": "Adrenals",
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

        self.Skin = {
            "name": "Skin",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0
        }

        self.Heart = {
            "name": "Heart",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0
        }

        self.Bone = {
            "name": "Bone",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0
        }

        self.Brain = {
            "name": "Brain",
            "P_v": 0,
            "P*_v": 0,
            "P_int": 0,
            "P*_int": 0
        }

        self.Adipose = {
            "name": "Adipose",
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

        self.receptorPositiveList = [self.Tumor, self.Liver, self.Spleen, self.RedMarrow, self.GI,
                                     self.Muscle, self.ProstateUterus, self.Adrenals, self.Rest]
        self.KidneyList = [self.Kidney]
        self.receptorNegativeList = [self.Skin, self.Adipose, self.Brain, self.Heart, self.Bone]
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
            "tf": 20,
            "totalAmountHot": 0.5* 1e-7,
            "totalAmountCold": 0.5* 1e-7
        }

        bolusInjection = {
            "type": "bolus",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "t0": 0,
            "totalAmountHot": 0.5* 1e-7,
            "totalAmountCold": 0.5* 1e-7
        }

        bolusTrainInjection = {
            "type": "bolusTrain",  ## "bolus"  ## possible options: bolus, exponential, gaussian, bolusTrain, constant
            "N": 2,
            "t": [0, 10],
            "totalAmountHot": 5,
            "totalAmountCold": 10
        }

        self.injectionProfile = constantInjection



