import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def fmt(x, pos):
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)


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







    ### heat maps

    # unlabeled = experiment.P_labeled_baseline/experiment.HotColdList
    # labeled = experiment.InjectedCoeff*experiment.P_labeled_baseline
    #
    # myplot = plt.contourf(unlabeled, labeled, (experiment.AUCMat),
    #              levels = 30, cmap = "copper")
    # plt.xlabel("Unlabeled (nmol)", fontsize=15)
    #
    # plt.ylabel("Radiolabeled (nmol)", fontsize=15)
    # plt.title("Radiolabeled vs Unlabeled")
    #
    # plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    # plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
    #
    # # cbar = plt.colorbar(myplot, format=ticker.FuncFormatter(fmt))
    # cbar = plt.colorbar(myplot, format='%.0e')
    # cbar.set_label('TIAC\n(nmol.min)', rotation=0, fontsize=10, y=1.1, labelpad=-40)
    #
    # SA = np.arange(0,0.1,0.01)
    #
    # cold = experiment.P_labeled_baseline/experiment.HotColdList
    # for sa in SA:
    #     plt.plot(cold, cold*((sa)/(1-sa)), "--", color = "0.4", lw = 1)
    #
    #
    #
    # ylim = experiment.InjectedCoeff*experiment.P_labeled_baseline
    # plt.ylim(ylim[0], ylim[-1])
    # plt.show()




    ###
    labeled = experiment.InjectedCoeff*experiment.P_labeled_baseline
    HC_ratio = experiment.HotColdList ## Hot Cold ratio
    #SA = HC_ratio/(HC_ratio+1)

    coeff = 6.022 * 1e15 * experiment.patient.lambda_phy / 60 / 1e6
    Activity = coeff * labeled  ## in MBq


    SA = coeff*HC_ratio/((1+HC_ratio)*1612*1e-9)   ### I suppose molar mass of lu177 DOTATATE is 1612  ### SA is in Bq/gr
    SA = SA / 1e6  ## Converting Bq/gr to MBq/qr


    myplot = plt.contourf(SA, Activity, (experiment.AUCMat),
                 levels = 30, cmap = "copper")
    # myplot = plt.contourf(SA, Activity, (experiment.AUCMat),
    #                     levels = 30, cmap = "copper")

    plt.xlabel("Specific Activity (MBq/g)", fontsize=15)

    plt.ylabel("Injected Activity (MBq)", fontsize=15)
    plt.title("Injected Activity Vs. Specific Activity")

    plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))

    # cbar = plt.colorbar(myplot, format=ticker.FuncFormatter(fmt))
    cbar = plt.colorbar(myplot, format='%.0e')
    cbar.set_label('time integrated activity\n(Bq.min)', rotation=0, fontsize=10, y=1.1, labelpad=-40)

    # SA = np.arange(0,0.1,0.01)
    #
    # cold = experiment.P_labeled/experiment.HotColdList
    # for sa in SA:
    #     plt.plot(cold, cold*((sa)/(1-sa)), "--", color = "0.4", lw = 1)



    # ylim = experiment.InjectedCoeff*experiment.P_labeled_baseline
    # plt.ylim(ylim[0], ylim[-1])
    plt.show()




    ####
    # labeled = experiment.InjectedCoeff*experiment.P_labeled_baseline
    # HC_ratio = experiment.HotColdList ## Hot Cold ratio
    #
    # # myplot = plt.contourf(HC_ratio/(HC_ratio+1), labeled, (experiment.AUCMat),
    # #              levels = 30, cmap = "copper")
    # for index in [5,6,7,8]:
    #
    #     plt.plot(HC_ratio/(HC_ratio+1), experiment.AUCMat[index,:], label = "Radiolabeled = {:.2e} nmol".format(labeled [index]) )
    #
    # plt.xlabel("Specific Activity", fontsize=15)
    # plt.ylabel("TIAC", fontsize=15)
    # plt.title("TIAC vs. Specific Activity")
    #
    # plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    # plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
    #
    # # cbar = plt.colorbar(myplot, format=ticker.FuncFormatter(fmt))
    # # cbar = plt.colorbar(myplot, format='%.0e')
    # # cbar.set_label('TIAC\n(nmol.min)', rotation=0, fontsize=10, y=1.1, labelpad=-40)
    #
    # # SA = np.arange(0,0.1,0.01)
    # #
    # # cold = experiment.P_labeled/experiment.HotColdList
    # # for sa in SA:
    # #     plt.plot(cold, cold*((sa)/(1-sa)), "--", color = "0.4", lw = 1)
    # #ylim = experiment.InjectedCoeff*experiment.P_labeled
    # # plt.ylim(ylim[0], ylim[-1])
    # plt.legend()
    # plt.show()




    ####
    #
    # labeled = experiment.InjectedCoeff * experiment.P_labeled_baseline
    # HC_ratio = experiment.HotColdList  ## Hot Cold ratio
    #
    # # myplot = plt.contourf(HC_ratio/(HC_ratio+1), labeled, (experiment.AUCMat),
    # #              levels = 30, cmap = "copper")
    # for index in [5, 6, 7, 8]:
    #     plt.plot(labeled, experiment.AUCMat[:,index],
    #              label="Specific Activity = {:.2e} nmol".format((HC_ratio/(HC_ratio+1))[index]))
    #
    # plt.xlabel("Radiolabeled", fontsize=15)
    # plt.ylabel("TIAC", fontsize=15)
    # plt.title("TIAC vs. Radiolabeled")
    #
    # plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    # plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
    #
    # # cbar = plt.colorbar(myplot, format=ticker.FuncFormatter(fmt))
    # # cbar = plt.colorbar(myplot, format='%.0e')
    # # cbar.set_label('TIAC\n(nmol.min)', rotation=0, fontsize=10, y=1.1, labelpad=-40)
    #
    # # SA = np.arange(0,0.1,0.01)
    # #
    # # cold = experiment.P_labeled/experiment.HotColdList
    # # for sa in SA:
    # #     plt.plot(cold, cold*((sa)/(1-sa)), "--", color = "0.4", lw = 1)
    # # ylim = experiment.InjectedCoeff*experiment.P_labeled
    # # plt.ylim(ylim[0], ylim[-1])
    # plt.legend()
    # plt.show()