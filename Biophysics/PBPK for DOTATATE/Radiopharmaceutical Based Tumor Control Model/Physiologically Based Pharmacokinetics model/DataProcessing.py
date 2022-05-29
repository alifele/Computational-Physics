import numpy as np
import matplotlib.pyplot as plt



class DataProcessing:
    def __init__(self, patientObj, therapyObj, encoderObj, solverObj):
        self.patient = patientObj
        self.therapy = therapyObj
        self.encoder = encoderObj
        self.results = solverObj

        self.data = self.results.solution


    def plotter(self):

        summedDataDict = dict()
        organsDict = self.results.organsObj.organsDict

        typesList = ["RecPos", "Kidney", "RecNeg", "Lungs", "ArtVein", "BloodProtein"]

        for type in typesList:
            if type in ["RecPos", "Kidney"]:
                linestyle = '--'
            else:
                linestyle = "-"
            for key in organsDict[type].keys():
                sumOfAll = self.data.t * 0.0
                name = organsDict[type][key]["name"]
                base = organsDict[type][key]["stencil"]["base"]
                length = organsDict[type][key]["stencil"]["length"]
                for i in range(1, length, 2):
                    sumOfAll += self.data.y[base+i, :]

                summedDataDict[name] = dict()
                summedDataDict[name]["data"] = sumOfAll
                summedDataDict[name]["LineStyle"] = linestyle



        # for i in range(4, 110):##110
        #     # plt.plot(self.results.tList, self.results.BigVectList[i, :])
        #     # # plt.plot(self.results.tList, self.results.BigVectList[i, :], 'o', 'red')
        #     plt.plot(np.log(self.data.t+1), self.data.y[i,:], label=i)
        #     # plt.plot(self.results.tList, self.results.BigVectList[i, :], label = i)

        dashed_flag = 0
        solid_flag = 0

        for key in summedDataDict.keys():
            organData = summedDataDict[key]["data"]
            ls = summedDataDict[key]["LineStyle"]


            if ls == "--" and dashed_flag == 0:
                key = "organs with receptor"
                plt.plot((self.data.t + 1), organData + 0.00001, label=key, ls=ls, lw=2)
                dashed_flag += 1
            if ls == "-" and solid_flag == 0:
                key = "organs without receptor"
                plt.plot((self.data.t + 1), organData + 0.00001, label=key, ls=ls, lw=2)
                solid_flag += 1

            if dashed_flag == 1 or solid_flag == 1:
                plt.plot((self.data.t+1), organData+0.00001, ls=ls, lw=2)
            plt.yscale("log")
            plt.xscale("log")

        # plt.plot((self.data.t+1), np.log(summedDataDict["GI"]["data"]+0.00001), 'r')


        # plt.legend()
        print("Hello")


        self.connectivity = self.results.SystemMat.copy()
        self.connectivity[self.connectivity!=0] = 1
