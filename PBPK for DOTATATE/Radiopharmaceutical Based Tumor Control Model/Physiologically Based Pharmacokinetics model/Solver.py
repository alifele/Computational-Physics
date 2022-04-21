import numpy as np



class Solver:
    def __init__(self, encoder):
        self.SystemMat = encoder.SystemMat
        self.BigVect = encoder.BigVect
        self.organsObj = encoder.organsObj


        t_0 = 0
        t_f = 10
        l = 12
        self.tList = np.arange(t_0, t_f, 2**(-l))
        self.h = self.tList[1] - self.tList[0]


        self.BigVectList = np.zeros((self.BigVect.shape[0], self.tList.shape[0]))
        self.BigVectList[:,-1] = self.BigVect




    def F(self, X):
        SystemMat = self.getSystemMat(X)
        return np.matmul(SystemMat, X)

    def getSystemMat(self, X):
        SystemMat = self.SystemMat.copy()
        for key in self.organsObj.organsDict["RecPos"].keys():
            organ = self.organsObj.organsDict["RecPos"][key]
            BigVector_pre = self.BigVectList[:,-1]
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
        for t in self.tList[:-1]:

            f0 = self.F(self.BigVect)
            f1 = self.F(self.BigVect+f0*self.h/2)
            f2 = self.F(self.BigVect+f1*self.h/2)
            f3 = self.F(self.BigVect+f2*self.h)

            self.BigVect += 1/6 * (f0 + 2*f1 + 2*f2 + f3)
            self.SystemMat = self.getSystemMat(self.BigVect)

            self.BigVectList[:,-1] = self.BigVect.copy()

        print("Hello")









