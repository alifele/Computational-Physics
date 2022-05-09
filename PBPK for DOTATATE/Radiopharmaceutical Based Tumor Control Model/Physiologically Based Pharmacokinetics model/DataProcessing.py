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
        for i in range(4, 110):##110
            # plt.plot(self.results.tList, self.results.BigVectList[i, :])
            # # plt.plot(self.results.tList, self.results.BigVectList[i, :], 'o', 'red')
            plt.plot(self.data.t, self.data.y[i,:], label=i)
            # plt.plot(self.results.tList, self.results.BigVectList[i, :], label = i)

        # plt.legend()
        print("Hello")
