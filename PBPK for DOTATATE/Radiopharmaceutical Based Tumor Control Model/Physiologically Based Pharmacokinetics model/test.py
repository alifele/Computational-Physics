
organList = ["Tumor", "Kidney", "RedMarrow", "Liver"]
TIAList = []

for organ in organList:
    P_labeled = dataProcessing.results.BigVectList[0,:]*0


    if organ == "Kidney":
        indexList = [1, 3, 5, 7, 9]
        base = dataProcessing.encoder.organsObj.organsDict["Kidney"][organ]["stencil"]["base"]
        P_labeled += dataProcessing.results.BigVectList[base + i, :]
    else:
        base = dataProcessing.encoder.organsObj.organsDict["RecPos"][organ]["stencil"]["base"]
        indexList = [1,3,5,7]
        for i in indexList:
            P_labeled += dataProcessing.results.BigVectList[base+i,:]




    TIA = dataProcessing.results.h/2*(P_labeled + np.roll(P_labeled,-1))[:-1].sum()
    TIAList.append(TIA)


# ## Calculating TIA for Liver
#
# dataProcessing.encoder.organsObj.organsDict["RecPos"]["Liver"]["stencil"]["base"]
#
#
# ## Calculating TIA for Kindey
#
# dataProcessing.encoder.organsObj.organsDict["RecPos"]["Kidney"]["stencil"]["base"]

