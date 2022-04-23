import numpy as np
import matplotlib.pyplot as plt


class Solver:
    def __init__(self, encoder):
        self.SystemMat = encoder.SystemMat.copy()
        self.BigVect = encoder.BigVect.copy()
        self.organsObj = encoder.organsObj

        self.injectionProfile = self.organsObj.therapy.injectionProfile



        t_0 = 0
        t_f = 50
        l = 11
        self.tList = np.linspace(t_0, t_f, 2**(l))
        self.h = self.tList[1] - self.tList[0]


        self.BigVectList = np.zeros((self.BigVect.shape[0], self.tList.shape[0]))
        self.BigVectList[:,0] = self.BigVect.copy()

        if self.injectionProfile["type"] == "constant":
            t0 = self.injectionProfile["t0"]
            tf = self.injectionProfile["tf"]
            self.toInjectAtEachTimeStep_Hot = self.injectionProfile["totalAmountHot"]/(self.h * (tf - t0))    ## injection amount at each time step
            self.toInjectAtEachTimeStep_Cold = self.injectionProfile["totalAmountCold"]/(self.h * (tf - t0))    ## injection amount at each time step





    def F(self, X, i):
        SystemMat = self.getSystemMat(X, i)
        return np.matmul(SystemMat, X)

    def getSystemMat(self, X, i):
        SystemMat = self.SystemMat.copy()
        for key in self.organsObj.organsDict["RecPos"].keys():  ## RecPos Organs: Tumor, Liver, Kidney, etc
            organ = self.organsObj.organsDict["RecPos"][key]
            BigVector_pre = self.BigVectList[:,i].copy()
            RP_index = organ["stencil"]["base"] + organ["bigVectMap"]["RP"]
            RP_unlabeled_index = organ["stencil"]["base"] + organ["bigVectMap"]["RP*"]
            K_on_pre = (organ["R0"] - (BigVector_pre[RP_index] + BigVector_pre[RP_unlabeled_index])) * organ["k_on"]
            K_on = (organ["R0"] - (X[RP_index] + X[RP_unlabeled_index])) * organ["k_on"]
            for elem in organ["sysMatMap"]["K_on"]:
                sign = elem[-1]
                pos = np.array(elem[:-1]) + organ["stencil"]["base"]
                SystemMat[pos[0], pos[1]] += sign*(K_on - K_on_pre)

        return SystemMat


    def solve(self):
        for i, t in enumerate(self.tList[:-1]):

            self.inject(t)


            f0 = self.F(self.BigVect, i)
            f1 = self.F(self.BigVect+f0*self.h/2, i)
            f2 = self.F(self.BigVect+f1*self.h/2, i)
            f3 = self.F(self.BigVect+f2*self.h, i)

            # self.BigVect += 1/6 * (f0 + 2*f1 + 2*f2 + f3)
            self.BigVect = self.BigVect + self.h/6 * (f0 + 2*f1 + 2*f2 + f3)
            #self.SystemMat = self.getSystemMat(self.BigVect,i)
            self.SystemMat = self.getSystemMat(self.BigVect,i)

            #self.BigVectList[:,i+1] = self.BigVect.copy()
            self.BigVectList[:,i+1] = self.BigVect.copy()
        print("Hello")


    def inject(self, t):
        self.BigVect[2] += 0.1*self.h
        self.BigVect[3] += 0.1*self.h
        if self.injectionProfile["type"] == "constant":
            if t < self.injectionProfile["tf"]:
                Vein_dict = self.organsObj.organsDict["ArtVein"]["Vein"]
                Vein_index_cold = Vein_dict["stencil"]["base"] + Vein_dict["bigVectMap"]["P"]   ## the place of P_vein in the BigVect
                Vein_index_hot = Vein_dict["stencil"]["base"] + Vein_dict["bigVectMap"]["P*"]   ## the place of P_vein in the BigVect
                self.BigVect[Vein_index_cold] += self.toInjectAtEachTimeStep_Cold
                self.BigVect[Vein_index_hot] += self.toInjectAtEachTimeStep_Hot










