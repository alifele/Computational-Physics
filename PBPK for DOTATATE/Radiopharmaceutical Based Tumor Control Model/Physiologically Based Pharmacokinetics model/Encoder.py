import numpy as np
import matplotlib.pyplot as plt

### BigVector contains all of the variables
### SystemMat is the system matrix which includes all of the parameters and differential equations

class Encoder:

    def __init__(self, patient, therapy):
        self.organsObj = Organs(patient, therapy)
        self.bigVectEncoder = BigVectEncoder(self.organsObj)
        self.systemMatricEncoder = SystemMatrixEncoder(self.organsObj)
        self.BigVect = self.bigVectEncoder.BigVect
        self.SystemMat = self.systemMatricEncoder.SystemMat


class Organs:

    def __init__(self, patientObj, therapyObj):
        self.patient = patientObj
        self.therapy = therapyObj
        self.typesList = ["ArtVein", "Lungs", "RecNeg", "RecPos", "Kidney", "BloodProtein"]

        self.defineLowLevelVariables()

        self.organsDict = {self.typesList[0]: self.ArtVeinDict,
                           self.typesList[1]: self.LungsDict,  ## This is for lungs which is a special kind of RecNeg
                           self.typesList[2]: self.RecNegDict,
                           self.typesList[3]: self.RecPosDict,
                           self.typesList[4]: self.KidneyDict,
                           self.typesList[5]: self.BloodProteinDict}

        self.initOrgansDict()

        self.N = 0  ## Length of BigVect. So the size of sysMat will be self.N*self.N
        for type in self.typesList:
            self.N += self.organsDict[type].__len__() * self.typeLengthDict[type]

    def initOrgansDict(self):
        pointer = 0
        for i, type in enumerate(self.typesList):  ## ArtVein, Lungs, RecNeg, RecPos, Kidney
            length = self.typeLengthDict[type]
            stencil = self.stencil
            stencil["length"] = length

            for organ in self.patient.Organs[type]:
                organDict = dict()
                organDict["stencil"] = stencil.copy()
                organDict["bigVectMap"] = self.typesMapDict_bigVect[type]
                organDict["volumeMap"] = self.volumeMap
                organDict["sysMatMap"] = self.typesMapDict_sysMat[type]
                organDict["stencil"]["base"] = pointer
                pointer += organDict["stencil"]["length"]
                self.organsDict[type][organ["name"]] = organDict
                organDict["name"] = organ["name"]
                organDict["type"] = type

                if type in ["RecPos", "Kidney"]:
                    organDict["R0"] = organ["R0"]
                    organDict["k_on"] = organ["k_on"]


    def defineLowLevelVariables(self):
        self.typeLengthDict = {self.typesList[0]: 2,
                               self.typesList[1]: 4,  ## This is the lungs which is a special kind of Recp Neg
                               self.typesList[2]: 4,
                               self.typesList[3]: 8,
                               self.typesList[4]: 10,
                               self.typesList[5]: 2}  ## This is the number of variable for each organ type
        ## For example lungs organ (which is RecNeg) has four variable: P_v, P*_v, P_int, P*_int

        self.ArtVeinDict = dict()
        self.LungsDict = dict()
        self.RecNegDict = dict()
        self.RecPosDict = dict()
        self.KidneyDict = dict()
        self.BloodProteinDict = dict()

        self.stencil = {"base": 0, "length": 0}  ## This stencil will help to make the BigVector variable
        ## stencil contains the base and length. For example for organ_i base
        ## 15 means that BigVect[15] is the start of the variables for this
        ## Organ

        ## The following lists show the shift for each variable. For example for organ_i that is RecPos kind,
        ## RecPos["P*_intern"] = 6. So it means that in the BigVec, corresponding variable is located with 6 shift form
        ## the base of that organ (i.e. if the base is 56, then BigVec[56+6] is P*_intern for organ_i
        ArtVeinMap_bigVect = {"P": 0, "P*": 1}
        RecNegMap_bigVect = {"P_v": 0, "P*_v": 1, "P_int": 2, "P*_int": 3}
        RecPosMap_bigVect = {"P_v": 0, "P*_v": 1, "P_int": 2, "P*_int": 3, "RP": 4, "RP*": 5, "P_intern": 6,
                             "P*_intern": 7}

        KidneyMap_bigVect = {"P_v": 0, "P*_v": 1, "P_intra": 2, "P*_intra": 3, "P_int": 4, "P*_int": 5, "RP": 6,
                             "RP*": 7, "P_intern": 8, "P*_intern": 9}

        BloodProteinMap_bigVect = {"PPR":0, "PPR*":1}
        self.typesMapDict_bigVect = {self.typesList[0]: ArtVeinMap_bigVect,
                                     self.typesList[1]: RecNegMap_bigVect,
                                     self.typesList[2]: RecNegMap_bigVect, ## This is for lungs which is a special kind of RecNeg
                                     self.typesList[3]: RecPosMap_bigVect,
                                     self.typesList[4]: KidneyMap_bigVect,  ## This is for Kidney
                                     self.typesList[5]: BloodProteinMap_bigVect
                                     }


        self.volumeMap = ["V_v", "V_v", "V_int", "V_int"]


        ArtVeinMap_sysMat = {"F": [[0, 0, -1], [1, 1, -1]],
                            "lambda_phys": [[0, 1, +1], [1, 1, -1]]}

        RecNegMap_sysMat = {"F": [[0, 0, -1], [1, 1, -1]],
                            "PS": [[0, 0, -1], [0, 2, +1], [1, 1, - 1], [1, 3, +1], [2, 0, +1], [2, 2, -1], [3, 1, +1],
                                   [3, 3, -1]],
                            "lambda_phys": [[0, 1, +1], [1, 1, -1], [2, 3, +1], [3, 3, -1]]}

        RecPosMap_sysMat = {"F": [[0, 0, -1], [1, 1, -1]],
                            "PS": [[0, 0, -1], [0, 2, +1], [1, 1, - 1], [1, 3, +1], [2, 0, +1], [2, 2, -1], [3, 1, +1],
                                   [3, 3, -1]],
                            "K_on": [[2, 2, -1], [3, 3, -1], [4, 2, +1], [5, 3, +1]],
                            "k_off": [[2, 4, +1], [3, 5, +1], [4, 4, -1], [5, 5, -1]],
                            "lambda_intern": [[4, 4, -1], [5, 5, -1], [6, 4, +1], [7, 5, +1]],
                            "lambda_rel": [[6, 6, -1], [7, 7, -1]],
                            "lambda_phys": [[0, 1, +1], [1, 1, -1], [2, 3, +1], [3, 3, -1], [4, 5, +1], [5, 5, -1],
                                            [6, 7, +1],
                                            [7, 7, -1]]}

        KidneyMap_sysMat = {"F": [[0, 0, -1], [1, 1, -1]],
                            "F_fil": [[0, 0, -1], [1, 1, - 1], [4, 0, 1], [4, 4, -1], [5, 1, 1], [5, 5, -1]],
                            "F_R": [[0, 2, 1], [1, 3, 1], [2, 2, -1], [2, 4, 1], [3, 3, -1], [3, 5, 1]],
                            "K_on": [[4, 4, -1], [5, 5, -1], [6, 4, +1], [7, 5, +1]],
                            "k_off": [[4, 6, +1], [5, 7, +1], [6, 6, -1], [7, 7, -1]],
                            "lambda_intern": [[6, 6, -1], [7, 7, -1], [8, 6, +1], [9, 7, +1]],
                            "lambda_rel": [[8, 8, -1], [9, 9, -1]],
                            "lambda_phys": [[0, 1, +1], [1, 1, -1], [2, 3, +1], [3, 3, -1], [4, 5, +1], [5, 5, -1],
                                            [6, 7, +1], [7, 7, -1], [8, 9, +1], [9, 9, -1]]}

        BloodProteinMap_sysMat = {"lambda_phys":[[0,1,1],[1,1,-1]]}

        self.typesMapDict_sysMat = {self.typesList[0]: ArtVeinMap_sysMat,
                                     self.typesList[1]: RecNegMap_sysMat,  ## This is for lungs which is a special kind of RecNeg
                                     self.typesList[2]: RecNegMap_sysMat,
                                     self.typesList[3]: RecPosMap_sysMat,
                                     self.typesList[4]: KidneyMap_sysMat,
                                    self.typesList[5]: BloodProteinMap_sysMat
                                    }


class BigVectEncoder:
    """
    #### To see the important note about this class go to the end of this file
    """
    def __init__(self, organs):
        self.organs = organs
        self.createBigVect()

    def createBigVect(self):
        ## BigVect is the biggest vector in the world that contains all of the variables of the model
        ## P_Art, P*_Art, P_Vein, P*_Vein, P_v_Lungs, P*_v_Lungs, etc
        ## First we should calculate the N. N is the length of BigVect
        self.BigVect = np.zeros(self.organs.N)
        pointer = 0
        for type in self.organs.typesList:  ## ArtVein, Lungs, RecNeg, RecPos
            for organ in self.organs.therapy.Organs[type]:
                organDict = self.organs.organsDict[type][organ["name"]]
                for variableName in organDict["bigVectMap"].keys():
                    self.BigVect[pointer] = organ[variableName]
                    pointer += 1

class SystemMatrixEncoder:
    def __init__(self, organs):
        self.organs = organs
        self.LiverDict = self.organs.organsDict["RecPos"]["Liver"]

        self.createSysMat()


    def createSysMat(self):
        self.SystemMat = np.zeros((self.organs.N,self.organs.N))
        pointer = 0
        #debugList = [self.organs.typesList["RecPos"]]
        for type in self.organs.typesList:  ## ArtVein, Lungs, RecNeg, RecPos, Kidney
            for organ in self.organs.patient.Organs[type]:  ## [Art, Vein] | [Lungs] | [RecNeg1, RecNeg2, ...] | [RecPos1, ...] | [Kidney]
                organDict = self.organs.organsDict[type][organ["name"]]
                subMat_initialPosition = np.array([ [organDict["stencil"]["base"], organDict["stencil"]["base"]] ]) ## [8,8]
                L = organDict["stencil"]["length"]  ## Length of sub matrix
                subMat = np.zeros((L,L))
                ## Contents of organDict:
                ## - stencil
                ## - bigVectMap
                ## - sysMatMap
                ## - name
                ## - type       ## ArtVein - Lungs - RecNeg - RecPos

                ## Contents of sysMatMap (for example for a RecPos organ)
                ## F: [list]
                ## PS: [list]
                ## K_on = k_on*R: [list]
                ## k_off: [list]
                ## lambda_intern: [list]
                ## lambda_rel: [list]
                ## lambda_phys: [list]
                ##
                ## the corresponding value to each of these keys is a list. The elements of this list shows the coordinates
                ## of the variable in the sub matrix. For example for the case of F for a RecPos organ we have:
                ## "F": [[0, 0, -1], [1, 1, -1]]. Note that the last number shows the sign of parameter in that location
                ## and the first two numbers are the location of the parameter in the sub matrix. For example the values
                ## in the example says that F is in the [0,0] position and the [1,1] position of tha matrix with negative
                ## sign.
                for paramName in organDict["sysMatMap"].keys(): ## For RecPos: F, PS, K_on, k_off, lambda_intern, etc
                    for elem in organDict["sysMatMap"][paramName]: ## [[0,0,-1],[1,1,-1],...]
                        sign = elem[-1]
                        pos = np.array(elem[:-1])


                        if paramName in ["F", "PS", "K_on", "F_fil", "F_R"]:    ## Normalizing with Volume
                            if organDict["name"] == "Kidney":       ## For Kidney that has a different volumeMap
                                volumeMap = ["V_v", "V_v", "V_intra", "V_intra", "V_int", "V_int"]
                                subMat[pos[0], pos[1]] += sign * organ[paramName] / organ[volumeMap[pos[1]]]
                            else:
                                # print(organDict["name"])
                                # print(paramName)
                                subMat[pos[0], pos[1]] += sign*organ[paramName]/organ[organDict["volumeMap"][pos[1]]]
                                ### Contents of organ[organDict["volumeMap"] is this list: ["V_v", "V_v", "V_int", "V_int"]
                                ### That is because F,PS, and K_on parameters must be normalized by the volume corresponding
                                ### to the column. Since in the sub matrix, column 0,1 are for the vascular compartment,
                                ### and column 2,3 are for the interestitial compartments, I am using pos[1] to get the
                                ### number of column and then by using the volume map list I can get the appropriate key
                                ### and go and get the value from the patient object
                        else:
                            # if (organ["name"] == "Adipose"):
                            #     print("H")
                            subMat[pos[0], pos[1]] += sign * organ[paramName]

                x1 = subMat_initialPosition[0,0]
                y1 = x1
                x2 = x1 + L
                y2 = x2
                print(organ)
                self.SystemMat[x1:x2, y1:y2] = subMat.copy()

                if type in ["RecPos", "RecNeg", "Kidney"]  : ## The outer F insertion
                    if organ["name"] in ["GI","Spleen"]:
                        thisOrganStencil = self.organs.organsDict[type][organ["name"]]["stencil"]
                        col = thisOrganStencil["base"]
                        row = self.LiverDict["stencil"]["base"]
                        self.SystemMat[row, col] = organ["F"]/organ["V_v"]
                        self.SystemMat[row+1, col+1] = organ["F"]/organ["V_v"]

                        self.SystemMat[x1, 0] = organ['F'] / self.organs.patient.Art["V_v"]
                        self.SystemMat[x1 + 1, 1] = organ['F'] / self.organs.patient.Art["V_v"]
                    else:
                        self.SystemMat[2,x1] = organ['F']/organ["V_v"]
                        self.SystemMat[3,x1+1] = organ['F']/organ["V_v"]

                        self.SystemMat[x1, 0] = organ['F'] / self.organs.patient.Art["V_v"]
                        self.SystemMat[x1 + 1, 1] = organ['F'] / self.organs.patient.Art["V_v"]

                if type == "Lungs":
                    shift = self.organs.organsDict["ArtVein"]["Vein"]["stencil"]["base"]    ## 2
                    self.SystemMat[x1,0+shift] = organ['F']/self.organs.patient.Vein["V_v"]
                    self.SystemMat[x1+1,1+shift] = organ['F']/self.organs.patient.Vein["V_v"]

                    self.SystemMat[0, x1] = organ['F']/organ["V_v"]
                    self.SystemMat[1, x1+1] = organ['F']/organ["V_v"]


                if type == "BloodProtein":
                    shift = self.organs.organsDict["ArtVein"]["Vein"]["stencil"]["base"]
                    self.SystemMat[x1,0+shift] = organ["k_pr"]
                    self.SystemMat[x1+1,1+shift] = organ["k_pr"]

        print("Hello")













""" #### Some notes about the BigVectEncoder class:

This class encodes the patient data to the BigVect format (i.e. the vector that contians all of the variables). 
Lots of low level classes are defined to do this conversion in a convenient way.

self.organsDict = {"ArtVein": ArtVeinDict, "Lungs": LungsDict, "RecNeg": RecNegOrgansDict, "RecPos": RecPosOrgansDict}
Note that each elements of this dictionary is itself a dictionary. For example:
RecNegOrgansDict = {"Skin": skinDict, "Bone": boneDict}
And each of the element of this dict is also a dict:
skinDict: = {"stencil": {"length": 2, "base": 41}, "type": "RecNeg", "map": map}


"""
