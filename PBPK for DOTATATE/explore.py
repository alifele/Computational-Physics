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

    # plt.plot(experiment.patient.Kidney.RPList.RP_labeled, label="RP_labeled")
    # plt.plot(experiment.patient.Kidney.RPList.RP_unlabeled, label="RP_unlabeled")
    # plt.ylim([2*1e-4])
    # plt.legend()

    # plt.plot(experiment.HotColdList,experiment.AUCList)
    # plt.plot(experiment.HotColdList,experiment.AUCList,"o")
    # plt.title("Fixed Injected Activity")
    # plt.xlabel("Hot/Cold ratio")
    # plt.ylabel("AUC for Kidney")

    plt.contourf(experiment.P_labeled/experiment.HotColdList , experiment.InjectedCoeff*experiment.P_labeled, (experiment.AUCMat),
                 levels = 30)
    #plt.imshow(experiment.AUCMat)
    plt.xlabel("unlabeled")
    plt.ylabel("labeled")
    cbar = plt.colorbar()
    cbar.set_label('AUC', rotation=270)
    # plt.imshow(experiment.AUCMat)