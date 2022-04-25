import numpy as np
import matplotlib.pyplot as plt



class DataProcessing:
    def __init__(self, patientObj, therapyObj, encoderObj, solverObj):
        self.patient = patientObj
        self.therapy = therapyObj
        self.encoder = encoderObj
        self.results = solverObj


    def plotter(self):
        for i in range(1, 110, 2):
            plt.plot(self.results.tList, self.results.BigVectList[i, :])


        print("Hello")
