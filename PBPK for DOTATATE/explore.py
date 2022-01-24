import numpy as np
import matplotlib.pyplot as plt





if __name__ == "__main__":

    # x = np.arange(0,2,0.01)
    # y = x ** 2
    #
    # fig = plt.figure()
    # for i in range(4):
    #     ax = fig.add_subplot(2,2,i+1)
    #     ax.plot(x,y**2)
    #
    #
    #
    # plt.show()

    # j = 0
    # fig = plt.figure(figsize=(18,12))
    #
    # for i, organ in enumerate(patient.OrgansList):
    #     if organ.name == "BloodProteinComplex" or organ.name in patient.ReceptorNegative:
    #         continue
    #
    #     ax = fig.add_subplot(4, 2, j + 1, title=organ.name + "--internalized_labeled")
    #     ax.plot(patient.tList, organ.PList.internalized_labeled)
    #     j += 1

    # plt.plot(patient.tList, patient.Kidney.PList.interacellular_unlabeled)
    # plt.title("Kidney -- interacellular_unlabeled")
    #
    # # plt.plot(patient.tList, patient.Vein.PList.P_unlabeled);plt.show()
    # plt.tight_layout()
    # plt.show()

    plt.plot(experiment.patient.Tumor.RPList.RP_unlabeled)

