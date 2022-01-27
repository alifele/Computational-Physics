import numpy as np
import matplotlib.pyplot as plt


class SA_Experiment:
    def __init__(self, Patient, Patient_info):
        self.Patient = Patient
        self.Patient_info = Patient_info




    def Explore(self):

        #self.P_labeled_baseline = 7.4 * 1e9 / (self.Patient.lambda_phy / 60) / (6.022 * 1e23) * 1e4
        self.P_labeled_baseline = 1e-3
        self.HotColdList = np.arange(0.01,0.2,0.02)
        self.InjectedCoeff = np.array([0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.5])

        self.P_labeledList = np.zeros(len(self.InjectedCoeff))
        self.AUCMat_Kidney = np.zeros((len(self.P_labeledList), self.HotColdList.shape[0]))
        self.AUCMat_Spleen = np.zeros((len(self.P_labeledList), self.HotColdList.shape[0]))
        self.AUCMat_Liver = np.zeros((len(self.P_labeledList), self.HotColdList.shape[0]))
        self.AUCMat_RedMarrow = np.zeros((len(self.P_labeledList), self.HotColdList.shape[0]))
        self.AUCMat_Tumor = np.zeros((len(self.P_labeledList), self.HotColdList.shape[0]))

        for i, InjectedCoeff in enumerate(self.InjectedCoeff):

            P_labeled = self.P_labeled_baseline * InjectedCoeff

            for j, HotColdRatio in enumerate(self.HotColdList):


                P_unlabeled = P_labeled / HotColdRatio
                #P_unlabeled = self.P_labeled_baseline / HotColdRatio

                self.Patient_info.Vein_P_labeled_injected = P_labeled
                self.Patient_info.Vein_P_unlabeled_injected = P_unlabeled

                self.patient = self.Patient(self.Patient_info)


                self.patient.Run()


                KidneyData = self.patient.Kidney
                LiverData = self.patient.Liver
                SpleenData = self.patient.Spleen
                RedMarrowData = self.patient.RedMarrow
                TumorData = self.patient.Tumor

                dt = self.patient.simParameters['dt']
                AUC_Kidney = self.Integrate(KidneyData.RPList.RP_labeled, dt)
                AUC_Spleen = self.Integrate(SpleenData.RPList.RP_labeled, dt)
                AUC_Liver = self.Integrate(LiverData.RPList.RP_labeled, dt)
                AUC_RedMarrow = self.Integrate(RedMarrowData.RPList.RP_labeled, dt)
                AUC_Tumor = self.Integrate(TumorData.RPList.RP_labeled, dt)

                self.AUCMat_Kidney[i,j] = AUC_Kidney
                self.AUCMat_Spleen[i,j] = AUC_Spleen
                self.AUCMat_Liver[i,j] = AUC_Liver
                self.AUCMat_RedMarrow[i,j] = AUC_RedMarrow
                self.AUCMat_Tumor[i,j] = AUC_Tumor
                print(i,j)





    def Plot(self):
        plt.plot(self.patient.Kidney.PList.vascular_labeled)

    def Integrate(self, array, dt):
        array_shift = np.roll(array, -1)
        Integral = ((array[:-1] + array_shift[:-1]) / 2).sum() * dt
        return Integral