import numpy as np



##### Units for the simulation
##  Volume  --> L
##  Time    --> min
##  Mass    --> gr
##  Moles   --> nmol


class Patient:

    def __init__(self):

        lambda_intern = 0.001
        lambda_phys = 7.23 * 1e-5
        k_on = 0.04 / 0.5
        k_off = 0.04

        H = 0.1                                 ## Hematocrit [1]
        BW = 80                                 ## Body weight [kg]
        gender = "male"                         ## male of female
        BSA = 1.94                              ## Body Surface Area [m^2]

        V_body = BW * 1000                      ## Based on 1g==1ml assumption
        V_tu = 0.087                            ## litre
        V_L = 1.811                             ## litre
        V_S = 0.198                             ## litre
        V_K = 0.193                             ## litre

        R_tu_density = 15                       ## nmol/L
        R_L_density = 1.4                       ## nmol/L
        R_S_density = 8.7                       ## nmol/L
        R_K_density = 6.5                       ## nmol/L
        R_rest_density = 0.5                    ## nmol/L

        lambda_rel_NT = 0.7 * 1e-4              ## 1/min
        lambda_rel_TU = 1.1 * 1e-4              ## 1/min

        tumorType = "NET"                       # NET or MEN
        f_tu = 0.1                              # L/min/g
        k_pr = 4.7 * 1e-4                       # 1/min
        GFR = 0.11                              # L/mi


        ## Permeability surface area product
        k_mu = 0.02                                ## L/min/kg | for muscle | --> please see the important note bellow. In a nutshell, /kg is the right unit here

        ## Important Note: In the table of Frenco 2021 paper, the units of k_i are in ml/min/g which is in fact
        ## the permeability surface area product per unit mass of organ. In order to get the permeability of the
        ## organ we need to multipy k_i at the mass of organ (1gr = 1ml). So the calculated PS value will be:
        ## PS = 1000 * k * V  (Note that V is in Litre). So PS will have the units of ml/min. Now to get the standard
        ## units of (L/min) we need to multiply it at 0.001. So PS with standard units (L/min) will be: PS = k*V

        if gender == "male":
            V_p = 2.8 * (1 - H) * BSA           ## Volume of total body serum
        else:
            V_p = 2.4 * (1 - H) * BSA           ## Volume of total body serum

        F = 1.23 * V_p                          ## flow total serum



        ##
        ####
        ######
        ######## Tumor initialization

        if tumorType == "NET":
            v_tu_int = 0.3
            v_tu_v = 0.1
            k_tu = 0.2  ## for PS calculation ## L/min/Kg (See the comment in Data.py file under MuscleData
        else:
            v_tu_int = 0.23
            v_tu_v = 0.11
            k_tu = 0.31  ## for PS calculation  ## L/min/Kg (See the comment in Data.py file under MuscleData

        lambda_rel_tu = 1.5 * 1e-4
        lambda_intern_tu = 0.001


        self.Tumor = {
            "name": "Tumor",
            "F": f_tu*(1-H)* V_tu,
            "PS": k_tu*V_tu,
            "V_total": V_tu,
            "V_v": v_tu_v*(1-H)*V_tu,
            "V_int": v_tu_int * V_tu,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": lambda_intern_tu,
            "lambda_rel": lambda_rel_tu,
            "lambda_phys": lambda_phys,
            "R0": R_tu_density * V_tu,
            "K_on": 0, ## R*k_on
        }

        ##
        ####
        ######
        ######## Liver initialization
        self.Liver = {
            "name": "Liver",
            "F": 0.065*F,
            "PS": 100*k_mu*V_L,
            "V_total": V_L,
            "V_v": 0.085 * V_L,
            "V_int": 0.2 * V_L,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": 1.7*lambda_intern_tu,
            "lambda_rel": lambda_rel_NT,
            "lambda_phys": lambda_phys,
            "R0": R_L_density * V_L,
            "K_on": 0,  ## R*k_on
        }

        ##
        ####
        ######
        ######## Spleen initialization
        self.Spleen = {
            "name": "Spleen",
            "F": 0.03 * F,
            "PS": 100 * k_mu * V_S,
            "V_total": V_S,
            "V_v": 0.12 * V_S,
            "V_int": 0.2 * V_S,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": 1.7 * lambda_intern_tu,
            "lambda_rel": lambda_rel_NT,
            "lambda_phys": lambda_phys,
            "R0": R_S_density * V_S,
            "K_on": 0,  ## R*k_on
        }

        ##
        ####
        ######
        ######## Kidney initialization
        self.Kidney = {
            "name": "Kidney",
            "F": 0.19*F,
            "V_total": V_K,
            "V_v": 0.055*V_K,
            "V_int": 0.15*V_K,
            "V_intra": -1,   ## The actual value will be calculated after dict
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": 1.7 * lambda_intern_tu,
            "lambda_rel": lambda_rel_NT,
            "lambda_phys": lambda_phys,
            "R0": R_K_density * V_S,
            "K_on": 0,  ## R*k_on
            "phi": 1.1,
            "GFR":  GFR,
            "f_exc": 0.98,
            "F_fil": -1,     ## F_filtration = GFR * phi
            "F_R": -1,       ## F_Return = F_fill - F_exc = GFR * phi * (1-f_exc)
        }
        self.Kidney["F_fil"] = self.Kidney["GFR"] * self.Kidney["phi"]
        self.Kidney["F_R"] = self.Kidney["F_fil"] * (1-self.Kidney["f_exc"])
        self.Kidney["V_intra"] = (self.Kidney["V_total"] - (self.Kidney["V_int"]+self.Kidney["V_v"])) * 2/3

        ##
        ####
        ######
        ######## ProstateUterus initialization
        if gender == "male":  ## Prostate
            V_total_prostateUterus = 0.016 * BW / 71  # L
            V_v_prostateUterus = 0.04 * (1 - H) * V_total_prostateUterus  # L
            V_int_prostateUterus = 0.25 * V_total_prostateUterus  # L
            F_prostateUterus = 0.18 * (1 - H) * V_total_prostateUterus
            k_prostateUterus = 0.1
            R_density_prostateUterus = R_K_density * 0.26

        if gender == "female":  ##Uterus
            V_total_prostateUterus = 0.08 * BW / 71  # L
            V_v_prostateUterus = 0.07 * (1 - H) * V_total_prostateUterus  # L
            V_int_prostateUterus = 0.5 * V_total_prostateUterus  # L
            F_prostateUterus = 1 * (1 - H) * V_total_prostateUterus
            k_prostateUterus = 0.2
            R_density_prostateUterus = R_K_density * 0.092

        self.ProstateUterus = {
            "name": "ProstateUterus",
            "F": F_prostateUterus,
            "PS": k_prostateUterus*V_total_prostateUterus,
            "V_total": V_total_prostateUterus,
            "V_v": V_v_prostateUterus,
            "V_int": V_int_prostateUterus,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": 1.7 * lambda_intern_tu,
            "lambda_rel": lambda_rel_NT,
            "lambda_phys": lambda_phys,
            "R0": R_density_prostateUterus * V_total_prostateUterus,
            "K_on": 0,  ## R*k_on
        }

        ##
        ####
        ######
        ######## Adrenal initialization
        V_total_adrenal = 0.014 * BW / 71  # L
        V_v_adrenal = 0.03 * (1 - H) * V_total_adrenal  # L
        V_int_adrenal = 0.24 * V_total_adrenal  # L
        f_adrenal = 6
        F_adrenal = f_adrenal * (1 - H) * V_total_adrenal
        k_adrenal = k_mu * 100
        R_density_adrenal = R_K_density * 1.65
        self.Adrenals = {
            "name": "Adrenals",
            "F": F_adrenal,
            "PS": k_adrenal * V_total_adrenal,
            "V_total": V_total_adrenal,
            "V_v": V_v_adrenal,
            "V_int": V_int_adrenal,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": 1.7 * lambda_intern_tu,
            "lambda_rel": lambda_rel_NT,
            "lambda_phys": lambda_phys,
            "R0": R_density_adrenal * V_total_adrenal,
            "K_on": 0,  ## R*k_on
        }

        ##
        ####
        ######
        ######## GI initialization
        V_total_GI = (0.385 + 0.548 + 0.104 + 0.15) * BW / 71  # L
        V_v_GI = 0.076 * V_p  # L
        alpha_GI = 8.8  ## interestitial to vascular ratio
        V_int_GI = alpha_GI * V_v_GI  # L
        F_GI = 0.16 * F
        k_GI = k_mu
        R_density_GI = R_K_density * 0.16
        self.GI = {
            "name": "GI",
            "F": F_GI,
            "PS": k_GI * V_total_GI,
            "V_total": V_total_GI,
            "V_v": V_v_GI,
            "V_int": V_int_GI,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": 1.7 * lambda_intern_tu,
            "lambda_rel": lambda_rel_NT,
            "lambda_phys": lambda_phys,
            "R0": R_density_GI * V_total_GI,
            "K_on": 0,  ## R*k_on
        }

        ##
        ####
        ######
        ######## RedMarrow initialization
        V_total_RedMarrow = 1.1 * BW / 71  # L
        V_v_RedMarrow = 0.04 * V_p  # L
        alpha_RedMarrow = 3.7  ## interestitial to vascular ratio
        V_int_RedMarrow = alpha_RedMarrow * V_v_RedMarrow  # L
        F_RedMarrow = 0.03 * F
        k_RedMarrow = k_mu*100
        R_density_RedMarrow = R_K_density * 0.028
        self.RedMarrow = {
            "name": "RedMarrow",
            "F": F_RedMarrow,
            "PS": k_RedMarrow * V_total_RedMarrow,
            "V_total": V_total_RedMarrow,
            "V_v": V_v_RedMarrow,
            "V_int": V_int_RedMarrow,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": 1.7 * lambda_intern_tu,
            "lambda_rel": lambda_rel_NT,
            "lambda_phys": lambda_phys,
            "R0": R_density_RedMarrow * V_total_RedMarrow,
            "K_on": 0,  ## R*k_on
        }

        ##
        ####
        ######
        ######## Muscle initialization
        V_total_Muscle = 30.078 * BW / 71  # L
        V_v_Muscle = 0.14 * V_p # L
        alpha_Muscle = 5.9  ## interestitial to vascular ratio
        V_int_Muscle = alpha_Muscle * V_v_Muscle  # L
        F_Muscle = 0.17 * F
        k_Muscle = k_mu
        R_density_Muscle = R_K_density * 0.0056
        self.Muscle = {
            "name": "Muscle",
            "F": F_Muscle,
            "PS": k_Muscle * V_total_Muscle,
            "V_total": V_total_Muscle,
            "V_v": V_v_Muscle,
            "V_int": V_int_Muscle,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": 1.7 * lambda_intern_tu,
            "lambda_rel": lambda_rel_NT,
            "lambda_phys": lambda_phys,
            "R0": R_density_Muscle * V_total_Muscle,
            "K_on": 0,  ## R*k_on
        }

        ##
        ####
        ######
        ######## Lungs initialization
        V_total_Lungs = 1 * BW / 71  # L
        V_v_Lungs = 0.105 * V_p  # L
        alpha_Lungs = 5.5  ## interestitial to vascular ratio
        V_int_Lungs = V_v_Lungs * alpha_Lungs  # L
        F_Lungs = F
        k_Lungs = 100 * k_mu
        self.Lungs = {
            "name": "Lungs",
            "F": F_Lungs,  # The real value will be calculated once we have the
            ## the flow of each organ. The Vein and Art flow is the sum of all flows
            "PS": k_Lungs*V_total_Lungs,
            "V_total": V_total_Lungs,
            "V_v": V_v_Lungs,
            "V_int": V_int_Lungs,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Skin initialization
        V_total_Skin = 3.408 * BW / 71  # L
        V_v_Skin = 0.03 * V_p  # L
        alpha_Skin = 8.9  ## interestitial to vascular ratio
        V_int_Skin = alpha_Skin * V_v_Skin  # L
        F_Skin = 0.05 * F
        k_Skin = k_mu
        self.Skin = {
            "name": "Skin",
            "F": F_Skin,  # The real value will be calculated once we have the
            ## the flow of each organ. The Vein and Art flow is the sum of all flows
            "PS": k_Skin * V_total_Skin,
            "V_total": V_total_Skin,
            "V_v": V_v_Skin,
            "V_int": V_int_Skin,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Adipose initialization
        V_total_Adipose = 13.465 * BW / 71  # L
        V_v_Adipose = 0.05 * V_p  # L
        alpha_Adipose = 15.5  ## interestitial to vascular ratio
        V_int_Adipose = alpha_Adipose * V_v_Adipose  # L
        F_Adipose = 0.05 * F
        k_Adipose = k_mu
        self.Adipose = {
            "name": "Adipose",
            "F": F_Adipose,  # The real value will be calculated once we have the
            ## the flow of each organ. The Vein and Art flow is the sum of all flows
            "PS": k_Adipose * V_total_Adipose,
            "V_total": V_total_Adipose,
            "V_v": V_v_Adipose,
            "V_int": V_int_Adipose,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Brain initialization
        V_total_Brain = 1.45 * BW / 71  # L
        V_v_Brain = 0.012 * V_p  # L
        alpha_Brain = 1  ## interestitial to vascular ratio
        ## Note that PS is zero for brain. To avoid division by zero I
        ## have intentionally put alpha_Brain to be 1 (so V_int is not zero)
        V_int_Brain = alpha_Brain * V_v_Brain  # L
        F_Brain = 0.04 * F
        k_Brain = 0
        self.Brain = {
            "name": "Brain",
            "F": F_Brain,  # The real value will be calculated once we have the
            ## the flow of each organ. The Vein and Art flow is the sum of all flows
            "PS": k_Brain * V_total_Brain,
            "V_total": V_total_Brain,
            "V_v": V_v_Brain,
            "V_int": V_int_Brain,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Heart initialization
        V_total_Heart = 0.341 * BW / 71  # L
        V_v_Heart = 0.01 * V_p  # L
        alpha_Heart = 3.7  ## interestitial to vascular ratio
        V_int_Heart = alpha_Heart * V_v_Heart  # L
        F_Heart = 0.04 * F
        k_Heart = k_mu
        self.Heart = {
            "name": "Heart",
            "F": F_Heart,  # The real value will be calculated once we have the
            ## the flow of each organ. The Vein and Art flow is the sum of all flows
            "PS": k_Heart * V_total_Heart,
            "V_total": V_total_Heart,
            "V_v": V_v_Heart,
            "V_int": V_int_Heart,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Bone initialization
        V_total_Bone = 10.165 * BW / 71 - self.RedMarrow['V_total']  # L
        V_v_Bone = 0.07 * V_p - self.RedMarrow["V_v"]  # L
        alpha_Bone = 9.3  ## interestitial to vascular ratio
        V_int_Bone = alpha_Bone * V_v_Bone  # L
        F_Bone = 0.05 * F
        k_Bone = k_mu
        self.Bone = {
            "name": "Bone",
            "F": F_Bone,  # The real value will be calculated once we have the
            ## the flow of each organ. The Vein and Art flow is the sum of all flows
            "PS": k_Bone * V_total_Bone,
            "V_total": V_total_Bone,
            "V_v": V_v_Bone,
            "V_int": V_int_Bone,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Vein initialization
        V_total_Vein = (0.18 + 0.045) * V_p
        F_Vein = F
        self.Vein = {
            "name": "Vein",
            "F": F_Vein,  ## The real value will be calculated once we have the
            ## the flow of each organ. The Vein and Art flow is the sum of all
            ## flows
            "V_v": V_total_Vein,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Art initialization
        V_total_Art = (0.06 + 0.045) * V_p  # L
        F_Art = F
        self.Art = {
            "name": "Art",
            "F": F_Art,  ## The real value will be calculated once we have the
            ## the flow of each organ. The Vein and Art flow is the sum of all flows
            "V_v": V_total_Art,
            "lambda_phys": lambda_phys,
        }

        ##
        ####
        ######
        ######## Rest initialization
        self.Rest = {
            "name": "Rest",
            "F": F_Muscle,
            "PS": k_Muscle * V_total_Muscle,
            "V_total": V_v_Muscle,
            "V_v": V_v_Muscle,
            "V_int": V_int_Muscle,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": 1.7 * lambda_intern_tu,
            "lambda_rel": lambda_rel_NT,
            "lambda_phys": lambda_phys,
            "R0": R_density_Muscle * V_total_Muscle,
            "K_on": 0,  ## R*k_on
        }




        self.receptorPositiveList = [self.Tumor, self.Liver, self.Spleen, self.RedMarrow, self.GI,
                                     self.Muscle, self.ProstateUterus, self.Adrenals]
        self.KidneyList = [self.Kidney]
        self.LungsList = [self.Lungs]
        self.receptorNegativeList = [self.Skin, self.Adipose, self.Brain, self.Heart, self.Bone]
        self.ArtVeinList = [self.Art, self.Vein]

        self.calculateK_on()    ## Will calculate K_on = k_on * R0 for RecPos and Kidney

        self.Organs = {
            "ArtVein": self.ArtVeinList,
            "Lungs": self.LungsList,
            "RecNeg": self.receptorNegativeList,
            "RecPos": self.receptorPositiveList,
            "Kidney": self.KidneyList,
        }

        self.addRestOrgan(BW, F, V_p, k_mu, R_rest_density, k_on, k_off, lambda_intern_tu, lambda_rel_NT, lambda_phys)


    def calculateK_on(self):
        # for elem in self.receptorPositiveList:
        #     elem["K_on"] = elem["k_on"] * elem["R0"]
        # for elem in self.KidneyList:
        #     elem["K_on"] = elem["k_on"] * elem["R0"]
        #
        for elem in self.receptorPositiveList:
            elem["K_on"] = 0
        for elem in self.KidneyList:
            elem["K_on"] = 0



    def addRestOrgan(self, BW, F, V_p, k_mu, R_rest_density, k_on, k_off, lambda_intern_tu, lambda_rel_NT, lambda_phys):
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

        ## TODO: I think we can add the contribution on the V_total and V_v_total from
        ## TODO: ---> Vein, Art, and Lungs. I need to figure this out carefuly later
        V_total_rest = BW - V_total_allOrgans   ## 1kg = 1lit, ##L
        F_rest = F - F_allOrgans
        V_v_rest = V_p - V_v_allOrgans

        alpha_rest = 3.7
        V_int_rest = alpha_rest * V_v_rest
        k_rest = k_mu
        self.Rest = {
            "name": "Rest",
            "F": F_rest,
            "PS": k_rest * V_total_rest,
            "V_total": V_v_rest,
            "V_v": V_v_rest,
            "V_int": V_int_rest,
            "k_on": k_on,
            "k_off": k_off,
            "lambda_intern": 1.7 * lambda_intern_tu,
            "lambda_rel": lambda_rel_NT,
            "lambda_phys": lambda_phys,
            "R0": R_rest_density * V_total_rest,
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
