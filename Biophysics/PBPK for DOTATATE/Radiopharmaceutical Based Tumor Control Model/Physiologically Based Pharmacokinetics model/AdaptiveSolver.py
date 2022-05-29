import numpy as np
import matplotlib.pyplot as plt


class AdaptiveSolver:
    def __init__(self, encoder):
        self.SystemMat = encoder.SystemMat.copy()
        self.BigVect = encoder.BigVect.copy()
        self.organsObj = encoder.organsObj
        self.injectionProfile = self.organsObj.therapy.injectionProfile

        self.setSimConf()
        self.setInjection()

        self.BigVectList = np.zeros((self.BigVect.shape[0], self.dataPoints))
        self.inject(0)  ## Doing the very first Injection
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
        t_0 = 0
        self.dataPoints = 5000
        self.tList = np.zeros(self.dataPoints)
        self.h = 0.01
        self.e = 1e-7
        self.h_new = 0
        self.h_min = 0.01

    def F(self, X, i):
        SystemMat = self.getSystemMat(X, i)
        return np.matmul(SystemMat, X)

    def getSystemMat(self, X, i):
        SystemMat = self.SystemMat.copy()
        ## TODO: Kidney needs to be added as well
        for key in self.organsObj.organsDict["RecPos"].keys():  ## RecPos Organs: Tumor, Liver, Kidney, etc
            organ = self.organsObj.organsDict["RecPos"][key]
            BigVector_pre = self.BigVectList[:,i-1].copy()
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
        for j, t in enumerate(self.tList[:-1]):
            i = j+1
            self.inject(t)
            flag = 0
            while flag == 0:
                # y = self.BigVectList[:,i-1].copy()
                y = self.BigVect.copy()
                f0 = self.F(y,i)
                f1 = self.F(y + f0*self.h/4, i)
                f2 = self.F(y + 3*self.h/32*f0 + 9*self.h/32*f1, i)
                f3 = self.F(y + 1932*self.h/2197*f0 - 7200*self.h/2197*f1 + 7296*self.h/2197*f2, i)
                f4 = self.F(y + 439*self.h/216*f0 - 8*self.h*f1 + 3680*self.h/513*f2 - 845*self.h/4104*f3, i)
                f5 = self.F(y - 8*self.h/27*f0 + 2*self.h*f1 - 3544*self.h/2565*f2 + 1859*self.h/4104*f3 - 11*self.h/40*f4, i)

                # Err = np.linalg.norm(self.h * (1/360*f0 - 128/4275*f2 - 2197/75240*f3 + 1/50*f4 + 2/55*f5))
                Err = np.abs(np.max(self.h * (1/360*f0 - 128/4275*f2 - 2197/75240*f3 + 1/50*f4 + 2/55*f5)))
                MaxErr = np.abs(self.h * self.e)
                ratio = MaxErr / Err

                self.h_new = 0.9 * self.h * np.power(ratio, 1/4)
                # print( np.power(ratio, 1/4))

                # if self.h_new < self.h_min:
                #     self.h_new = self.h_min

                # if ratio < 1:
                if self.h_new < self.h:
                    if self.h_new < 0.5*self.h:
                        self.h_new = 0.5 * self.h
                    self.h = self.h_new
                else:
                    # print("Hely")
                    # if self.h_new > 4 * self.h:
                    #     self.h_new = 4 * self.h
                    flag = 1


                # if self.h_new < self.h:
                #     # if self.h_new < 0.1*self.h:
                #     #     print("hello")
                #     #     self.h_new = 0.1*self.h
                #     #     pass
                #     # else:
                #     #     self.h = self.h_new
                #     self.h = self.h_new
                # else:
                #     # if self.h_new > 100*self.h:
                #     #     self.h_new = 100*self.h
                #     #     pass
                #     # else:
                #     #     self.h = self.h_new
                #
                #     #self.h = self.h_new
                #     flag = 1

            # if self.h < self.h_min:
            #     self.h = self.h_min

            y += self.h * (16/135*f0 + 6656/12825*f2 + 28561/56430*f3 - 9/50*f4 + 2/55*f5)
            self.BigVect = y.copy()
            t_new = t + self.h
            self.BigVectList[:,i] = self.BigVect.copy()
            self.tList[i] = t_new
            self.SystemMat = self.getSystemMat(self.BigVect, i)
            self.h = self.h_new

            # print(j)
            if j%1000 == 0:
                print(j)





            # self.BigVect += 1/6 * (f0 + 2*f1 + 2*f2 + f3)
            # self.BigVect = self.BigVect + self.h/6 * (f0 + 2*f1 + 2*f2 + f3)
            # #self.SystemMat = self.getSystemMat(self.BigVect,i)
            # self.SystemMat = self.getSystemMat(self.BigVect,i)
            #
            # #self.BigVectList[:,i+1] = self.BigVect.copy()
            # self.BigVectList[:,i] = self.BigVect.copy()


        ####  Debugging
        # debugList = [9,11,13,15]
        # peptide = self.BigVectList[0,:]*0
        # for i in debugList:
        #     peptide += self.BigVectList[i,:]
        print("Hello")


    def inject(self, t):
        if self.injectionProfile["type"] == "constant":
            if t < self.injectionProfile["tf"]:
                self.BigVect[self.Vein_index_cold] += self.toInjectAtEachTimeStep_Cold
                self.BigVect[self.Vein_index_hot] += self.toInjectAtEachTimeStep_Hot
                self.totalHot += self.toInjectAtEachTimeStep_Hot
                self.totalCold += self.toInjectAtEachTimeStep_Cold

        if self.injectionProfile["type"] == "bolus":
            if t >= self.injectionProfile["t0"] and self.singleBolusFlag == 0:
                self.BigVect[self.Vein_index_cold] += self.injectionProfile["totalAmountCold"]
                self.BigVect[self.Vein_index_hot] += self.injectionProfile["totalAmountHot"]
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
                    self.BigVect[self.Vein_index_cold] += self.eachBolusCold
                    self.BigVect[self.Vein_index_hot] += self.eachBolusHot
                    self.totalCold += self.eachBolusCold
                    self.totalHot += self.eachBolusHot
                    self.multiBolusFlag += 1













