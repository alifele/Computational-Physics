import numpy as np
import matplotlib.pyplot as plt


class SA_Experiment:
    def __init__(self, Patient, Patient_info):
        self.Patient = Patient
        self.Patient_info = Patient_info




    def Explore(self):


        P_labeled = 1e-4
        P_unlabeled = 1e-4

        self.Patient_info.Vein_P_labeled_injected = P_labeled
        self.Patient_info.Vein_P_unlabeled_injected = P_unlabeled


        self.patient = self.Patient(self.Patient_info)
        self.patient.Run()

        plt.plot(self.patient.Kidney.PList.vascular_labeled)


    def Plot(self):
        pass