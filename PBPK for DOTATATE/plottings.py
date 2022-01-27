import matplotlib.pyplot as plt



labeled = experiment.InjectedCoeff*experiment.P_labeled_baseline
HC_ratio = experiment.HotColdList ## Hot Cold ratio
#SA = HC_ratio/(HC_ratio+1)

coeff = 6.022 * 1e15 * experiment.patient.lambda_phy / 60 / 1e6
Activity = coeff * labeled  ## in MBq


SA = coeff*HC_ratio/((1+HC_ratio)*1612*1e-9)   ### I suppose molar mass of lu177 DOTATATE is 1612  ### SA is in Bq/gr
SA = SA / 1e6  ## Converting Bq/gr to MBq/qr
SA = SA / 1e6  ## Converting Bq/gr to MBq/uq

# myplot = plt.contourf(SA, Activity, (experiment.AUCMat_Kidney),
#              levels = 30, cmap = "copper")
# plt.title("Injected Activity Vs. Specific Activity (Kidney)")
# plt.scatter([0.0004140],[16.9314],marker="o", color="red")
# plt.scatter([0.0006773],[2.61077],marker="o", color="red")

# plt.text(10**(-4), 3.1, "1",color='white', fontsize=15)
# plt.text(10**(-4), 10.5, "2",color='white', fontsize=15)
# plt.text(2.6e-4, 6, "3",color='white', fontsize=15)
# plt.text(6.6e-4, 6, "4",color='0.9', fontsize=15)
# plt.axhline(y=3, ls="--", alpha=0.8, color='0.5')
# plt.axhline(y=10, ls="--", alpha=0.8, color='0.5')
# plt.axvline(x=2.5e-4, ls="--", alpha=0.8, color='0.5')
# plt.axvline(x=6.5e-4, ls="--", alpha=0.8, color='0.5')




### Heatmap
# myplot = plt.contourf(SA, Activity, (experiment.AUCMat_Tumor),
#              levels = 30, cmap = "copper")
# plt.title("Injected Activity vs. Specific Activity (Kidney)")
# plt.scatter([0.0004327],[16.9314],marker="o", color="red")
# plt.scatter([0.0006773],[2.45669],marker="o", color="red")
# #
# # myplot = plt.contourf(SA, Activity, (experiment.AUCMat_Kidney),
# #              levels = 30, cmap = "copper")
# # plt.title("Injected Activity vs. Specific Activity (Tumor)")
# # plt.scatter([0.0004157],[16.9314],marker="o", color="red")
# # plt.scatter([0.0006773],[2.58444],marker="o", color="red")
#
# plt.xlabel("Specific Activity (MBq/μg)", fontsize=15)
# plt.ylabel("Injected Activity (MBq)", fontsize=15)
# plt.yscale("log")
#
# # plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
# plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
#
# cbar = plt.colorbar(myplot, format='%.0e')
# cbar.set_label('time integrated activity\n(Bq.min)', rotation=0, fontsize=10, y=1.1, labelpad=-40)
#
# plt.show()



### AUC vs. Activity

## Tumor

x_id = [4,9]
plt.plot(Activity, experiment.AUCMat_Tumor[:, x_id[0]], lw=5, label="specific activity = {:2.2e} MBq/μg".format(SA[x_id[0]]))
plt.plot(Activity, experiment.AUCMat_Tumor[:, x_id[1]], lw=5, label="specific activity = {:2.2e} MBq/μg".format(SA[x_id[1]]))


plt.plot(Activity, experiment.AUCMat_Tumor[:, x_id[0]], "o", color = '0.5', ms=7)
plt.plot(Activity, experiment.AUCMat_Tumor[:, x_id[1]], "o", color = '0.5', ms=7)

plt.xlabel("Injected Activity (MBq)", fontsize=15)
plt.ylabel("Time Integrated Activity (Bq.min)", fontsize=15)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
plt.title("TIA vs. Injected Activity (Kidney)")

plt.legend()

# Kidney
# x_id = [4,9]
# plt.plot(Activity, experiment.AUCMat_Kidney[:, x_id[0]], lw=5, label="specific activity = {:2.2e} MBq/μg".format(SA[x_id[0]]))
# plt.plot(Activity, experiment.AUCMat_Kidney[:, x_id[1]], lw=5, label="specific activity = {:2.2e} MBq/μg".format(SA[x_id[1]]))
#
#
# plt.plot(Activity, experiment.AUCMat_Kidney[:, x_id[0]], "o", color = '0.5', ms=7)
# plt.plot(Activity, experiment.AUCMat_Kidney[:, x_id[1]], "o", color = '0.5', ms=7)
#
# plt.xlabel("Injected Activity (MBq)", fontsize=15)
# plt.ylabel("Time Integrated Activity (Bq.min)", fontsize=15)
# plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
# plt.title("TIA vs. Injected Activity (Tumor)")

plt.legend()



#### AUC vs. Specific activity

# ###Tumor
# y_id = [0,8]
# plt.plot(SA, experiment.AUCMat_Tumor[y_id[0], :], lw=5, label="injected activity = {:2.2e} MBq".format(Activity[y_id[0]]))
# plt.plot(SA, experiment.AUCMat_Tumor[y_id[1], :], lw=5, label="injected activity = {:2.2e} MBq".format(Activity[y_id[1]]))
#
#
# plt.plot(SA, experiment.AUCMat_Tumor[y_id[0], :], "o", color = '0.5', ms=7)
# plt.plot(SA, experiment.AUCMat_Tumor[y_id[1], :], "o", color = '0.5', ms=7)
#
# plt.xlabel("Specific Activity (MBq/μg)", fontsize=15)
# plt.ylabel("Time Integrated Activity (Bq.min)", fontsize=15)
# plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
# plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
# plt.title("TIA vs. Specific Activity (Kidney)")
# plt.legend()


## Kidney
# y_id = [0,8]
# plt.plot(SA, experiment.AUCMat_Kidney[y_id[0], :], lw=5, label="injected activity = {:2.2e} MBq".format(Activity[y_id[0]]))
# plt.plot(SA, experiment.AUCMat_Kidney[y_id[1], :], lw=5, label="injected activity = {:2.2e} MBq".format(Activity[y_id[1]]))
#
#
# plt.plot(SA, experiment.AUCMat_Kidney[y_id[0], :], "o", color = '0.5', ms=7)
# plt.plot(SA, experiment.AUCMat_Kidney[y_id[1], :], "o", color = '0.5', ms=7)
#
# plt.xlabel("Specific Activity (MBq/μg)", fontsize=15)
# plt.ylabel("Time Integrated Activity (Bq.min)", fontsize=15)
# plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
# plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
# plt.title("TIA vs. Specific Activity (Tumor)")
# plt.legend()
#
#




