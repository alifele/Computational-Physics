
# organList = ["Tumor", "Kidney", "RedMarrow", "Liver"]
# TIAList = []
#
# for organ in organList:
#     P_labeled = dataProcessing.results.BigVectList[0,:]*0
#
#
#     if organ == "Kidney":
#         indexList = [1, 3, 5, 7, 9]
#         base = dataProcessing.encoder.organsObj.organsDict["Kidney"][organ]["stencil"]["base"]
#         P_labeled += dataProcessing.results.BigVectList[base + i, :]
#     else:
#         base = dataProcessing.encoder.organsObj.organsDict["RecPos"][organ]["stencil"]["base"]
#         indexList = [1,3,5,7]
#         for i in indexList:
#             P_labeled += dataProcessing.results.BigVectList[base+i,:]
#
#
#
#
#     TIA = dataProcessing.results.h/2*(P_labeled + np.roll(P_labeled,-1))[:-1].sum()
#     TIAList.append(TIA)
#
#
# # ## Calculating TIA for Liver
# #
# # dataProcessing.encoder.organsObj.organsDict["RecPos"]["Liver"]["stencil"]["base"]
# #
# #
# # ## Calculating TIA for Kindey
# #
# # dataProcessing.encoder.organsObj.organsDict["RecPos"]["Kidney"]["stencil"]["base"]

import numpy as np
tList = dataProcessing.results.tList

d = (np.roll(tList, -1) - tList)[:-1]

plt.plot(tList[1:], d)

########## Bolus injection
## [180.98269607829818, 157.1768151934822, 121.32095749381637, 755.0527416481743]


########## 240 min constant injection
## [163.57671696563816, 153.81172576440167, 116.28048612947926, 707.8280064772118]

########## 360 min constant injection
## [154.4316221526142, 151.6024770749637, 113.51291143122012, 681.496670324132]

########## 120 min constant injection
## [172.44595939055893, 155.6619941824753, 118.77201277008213, 731.8974202829712]


########## MultiBolus 3
## [153.81691766748528, 150.9522560544815, 113.93642992609044, 684.9601438286072]


########## MultiBolus 4
## [153.9821064993068, 151.13959680984524, 113.85790004243675, 684.5613183874694]

########## MultiBolus 6
## [154.18072446798803, 151.35198226230554, 113.71310638518958, 683.4698949260772]



