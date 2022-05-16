import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


class StiffSolver:
    def __init__(self, encoder):
        self.SystemMat = encoder.SystemMat.copy()
        self.BigVect = encoder.BigVect.copy()
        self.organsObj = encoder.organsObj
        self.injectionProfile = self.organsObj.therapy.injectionProfile

        self.setSimConf()
        self.setInjection()

        self.BigVectList = np.zeros((self.BigVect.shape[0], self.tList.shape[0]))
        self.BigVect = self.inject(0, self.BigVect)  ## Doing the very first Injection
        self.BigVectList[:,0] = self.BigVect.copy()




    def setInjection(self):
        self.totalHot = 0.0
        self.totalCold = 0.0
        Vein_dict = self.organsObj.organsDict["ArtVein"]["Vein"]
        self.Vein_index_cold = Vein_dict["stencil"]["base"] + Vein_dict["bigVectMap"]["P"]  ## the place of P_vein in the BigVect
        self.Vein_index_hot = Vein_dict["stencil"]["base"] + Vein_dict["bigVectMap"]["P*"]  ## the place of P_vein in the BigVect
        if self.injectionProfile["type"] == "constant":
            t0 = self.injectionProfile["t0"]
            tf = self.injectionProfile["tf"]
            self.toInjectAtEachTimeStep_Hot = self.injectionProfile["totalAmountHot"]*self.h / (tf - t0)    ## injection amount at each time step
            self.toInjectAtEachTimeStep_Cold = self.injectionProfile["totalAmountCold"]*self.h / (tf - t0)    ## injection amount at each time step

        if self.injectionProfile["type"] == "bolus":
            self.singleBolusFlag = 0    ## This will help us to make sure that just one bolus will be injected

        if self.injectionProfile["type"] == "bolusTrain":
            self.multiBolusFlag = 0     ## This will help us to inject exactly N boluses
            self.eachBolusCold = self.injectionProfile["totalAmountCold"] / self.injectionProfile["N"]
            self.eachBolusHot = self.injectionProfile["totalAmountHot"] / self.injectionProfile["N"]



    def setSimConf(self):
        # t_0 = 0
        # t_f = 1200        ## 75 for l=16 works best. So increase l by one if you do t_f = 150
        # l = 20

        t_0 = 0
        t_f = 35        ## 75 for l=16 works best. So increase l by one if you do t_f = 150
        l = 15
        self.tList = np.linspace(t_0, t_f, 2 ** (l))
        self.h = self.tList[1] - self.tList[0]

    def F(self, t, X):
        X = self.inject(t, X)
        B = self.getBFunction(X)
        return np.matmul(self.SystemMat, X) + B

    def getBFunction(self, X):
        B = np.zeros(X.shape)
        organTypes = ["Kidney", "RecPos"]
        for type in organTypes:

            for organ in self.organsObj.patient.Organs[type]:  ## Tumor, Kidney, etc
                organDict = self.organsObj.organsDict[type][organ["name"]]

                RP_index_labeled = organDict["stencil"]["base"] + organDict["bigVectMap"]["RP*"]
                RP_unlabeled_index = organDict["stencil"]["base"] + organDict["bigVectMap"]["RP"]

                P_int_labeled = organDict["stencil"]["base"] + organDict["bigVectMap"]["P*_int"]
                P_int_unlabaled = organDict["stencil"]["base"] + organDict["bigVectMap"]["P_int"]

                binded = X[RP_index_labeled] + X[RP_unlabeled_index]

                B[RP_index_labeled] = organDict["k_on"] * X[P_int_labeled] * (organDict["R0"] - binded) / organ["V_int"]
                B[RP_unlabeled_index] = organDict["k_on"] * X[P_int_unlabaled] * (organDict["R0"] - binded) / organ["V_int"]

                B[P_int_labeled] = -organDict["k_on"] * X[P_int_labeled] * (organDict["R0"] - binded) / organ["V_int"]
                B[P_int_unlabaled] = -organDict["k_on"] * X[P_int_unlabaled] * (organDict["R0"] - binded) / organ["V_int"]

        return B

    # def getSystemMat(self, X, i):
    #     SystemMat = self.SystemMat.copy()
    #     for key in self.organsObj.organsDict["RecPos"].keys():  ## RecPos Organs: Tumor, Liver, Kidney, etc
    #         organ = self.organsObj.organsDict["RecPos"][key]
    #         BigVector_pre = self.BigVectList[:,i-1].copy()
    #         RP_index = organ["stencil"]["base"] + organ["bigVectMap"]["RP"]
    #         RP_unlabeled_index = organ["stencil"]["base"] + organ["bigVectMap"]["RP*"]
    #         K_on_pre = (organ["R0"] - (BigVector_pre[RP_index] + BigVector_pre[RP_unlabeled_index])) * organ["k_on"]
    #         K_on = (organ["R0"] - (X[RP_index] + X[RP_unlabeled_index])) * organ["k_on"]
    #         for elem in organ["sysMatMap"]["K_on"]:
    #             sign = elem[-1]
    #             pos = np.array(elem[:-1]) + organ["stencil"]["base"]
    #             SystemMat[pos[0], pos[1]] += sign*(K_on - K_on_pre)
    #
    #     return SystemMat


    def solve(self):
        # for j, t in enumerate(self.tList[1:]):
        #     i = j+1 ## Note that the enumerate does not show the index of element.
        #     self.inject(t)
        #
        #
        #     f0 = self.F(self.BigVect, i)
        #     f1 = self.F(self.BigVect+f0*self.h/2, i)
        #     f2 = self.F(self.BigVect+f1*self.h/2, i)
        #     f3 = self.F(self.BigVect+f2*self.h, i)
        #
        #     # self.BigVect += 1/6 * (f0 + 2*f1 + 2*f2 + f3)
        #     self.BigVect = self.BigVect + self.h/6 * (f0 + 2*f1 + 2*f2 + f3)
        #     #self.SystemMat = self.getSystemMat(self.BigVect,i)
        #     self.SystemMat = self.getSystemMat(self.BigVect,i)
        #
        #     #self.BigVectList[:,i+1] = self.BigVect.copy()
        #     self.BigVectList[:,i] = self.BigVect.copy()
        #
        #     if j%1000 == 0:
        #         print(j)
        #
        #
        # ####  Debugging
        # # debugList = [9,11,13,15]
        # # peptide = self.BigVectList[0,:]*0
        # # for i in debugList:
        # #     peptide += self.BigVectList[i,:]
        # print("Hello")
        self.solution = solve_ivp(self.F, [0,100000], self.BigVect, method="BDF")
        print("hello")



    def inject(self, t, X):

        if self.injectionProfile["type"] == "constant":
            if t < self.injectionProfile["tf"]:
                X[self.Vein_index_cold] += self.toInjectAtEachTimeStep_Cold
                X[self.Vein_index_hot] += self.toInjectAtEachTimeStep_Hot
                self.totalHot += self.toInjectAtEachTimeStep_Hot
                self.totalCold += self.toInjectAtEachTimeStep_Cold

        if self.injectionProfile["type"] == "bolus":
            if t >= self.injectionProfile["t0"] and self.singleBolusFlag == 0:
                X[self.Vein_index_cold] += self.injectionProfile["totalAmountCold"]
                X[self.Vein_index_hot] += self.injectionProfile["totalAmountHot"]
                self.totalCold += self.injectionProfile["totalAmountCold"]
                self.totalHot += self.injectionProfile["totalAmountHot"]
                self.singleBolusFlag = 1

        ## TODO: I think I need to fix something. when I only have
        ## RecNeg organ, with 5 bolus trains and total amount of 10,
        ## instead of 10*2 total peptide in body (cold + disintegerated hot), I get
        ## 5 * (10*2). There must be something wrong
        if self.injectionProfile["type"] == "bolusTrain":

            if self.multiBolusFlag != self.injectionProfile["N"]:
                if t >= self.injectionProfile["t"][self.multiBolusFlag]:
                    X[self.Vein_index_cold] += self.eachBolusCold
                    X[self.Vein_index_hot] += self.eachBolusHot
                    self.totalCold += self.eachBolusCold
                    self.totalHot += self.eachBolusHot
                    self.multiBolusFlag += 1

        return X













