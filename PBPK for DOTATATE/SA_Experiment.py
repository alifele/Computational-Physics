import numpy as np
import matplotlib.pyplot as plt


class SA_Experiment:
    def __init__(self, Patient, Patient_info):
        self.Patient = Patient
        self.Patient_info = Patient_info




    def Explore(self):


        self.HotColdList = np.arange(0.01,0.2,0.02)
        self.InjectedCoeff = np.array([0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.5])

        self.P_labeled = 1e-4
        self.P_labeledList = np.zeros(len(self.InjectedCoeff))

        self.AUCMat = np.zeros((len(self.P_labeledList), self.HotColdList.shape[0]))

        for i, InjectedCoeff in enumerate(self.InjectedCoeff):
            P_labeled = self.P_labeled * InjectedCoeff

            for j, HotColdRatio in enumerate(self.HotColdList):

                P_unlabeled = P_labeled / HotColdRatio
                self.Patient_info.Vein_P_labeled_injected = P_labeled
                self.Patient_info.Vein_P_unlabeled_injected = P_unlabeled


                self.patient = self.Patient(self.Patient_info)
                self.patient.Run()


                KidneyData = self.patient.Kidney
                dt = self.patient.simParameters['dt']
                AUC = self.Integrate(KidneyData.RPList.RP_labeled, dt)
                self.AUCMat[i,j] = AUC
                print(i,j)





    def Plot(self):
        plt.plot(self.patient.Kidney.PList.vascular_labeled)

    def Integrate(self, array, dt):
        array_shift = np.roll(array, -1)
        Integral = ((array[:-1] + array_shift[:-1]) / 2).sum() * dt
        return Integral