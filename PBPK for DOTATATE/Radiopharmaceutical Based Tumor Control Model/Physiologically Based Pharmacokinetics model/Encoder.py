import numpy as np
import matplotlib.pyplot as plt

### BigVector contains all of the variables
### V_Vector contains the volume of each variable (for example v_int for P_int and P*_int)
### SystemMat is the system matrix which includes all of the parameters and differential equations

class Encoder:

    def __init__(self, patient, therapy):
        self.organsObj = Organs(patient, therapy)
        self.bigVectEncoder = BigVectEncoder(self.organsObj)
        systemMatricEncoder = SystemMatrixEncoder(self.organsObj)


class Organs:

    def __init__(self, patientObj, therapyObj):
        self.patient = patientObj
        self.therapy = therapyObj
        self.typesList = ["ArtVein", "Lungs", "RecNeg", "RecPos"]

        self.defineLowLevelVariables()

        self.organsDict = {self.typesList[0]: self.ArtVeinDict,
                           self.typesList[1]: self.LungsDict,  ## This is for lungs which is a special kind of RecNeg
                           self.typesList[2]: self.RecNegDict,
                           self.typesList[3]: self.RecPosDict}

        self.initOrgansDict()

        self.N = 0  ## Length of BigVect. So the size of sysMat will be self.N*self.N
        for type in self.typesList:
            self.N += self.organsDict[type].__len__() * self.typeLengthDict[type]

    def initOrgansDict(self):
        pointer = 0
        for i, type in enumerate(self.typesList):  ## ArtVein, Lungs, RecNeg, RecPos
            length = self.typeLengthDict[type]
            stencil = self.stencil
            stencil["length"] = length

            for organ in self.therapy.Organs[type]:
                organDict = dict()
                organDict["stencil"] = stencil.copy()
                organDict["bigVectMap"] = self.typesMapDict_bigVect[type]
                organDict["V_vectorMap"] = self.typesMapDict_V_Vect[type]
                organDict["sysMatMap"] = self.typesMapDict_sysMat[type]
                organDict["stencil"]["base"] = pointer
                pointer += organDict["stencil"]["length"]
                self.organsDict[type][organ["name"]] = organDict
                organDict["name"] = organ["name"]
                organDict["type"] = type

    def defineLowLevelVariables(self):
        self.typeLengthDict = {self.typesList[0]: 2,
                               self.typesList[1]: 4,  ## This is the lungs which is a special kind of Recp Neg
                               self.typesList[2]: 4,
                               self.typesList[3]: 8}  ## This is the number of variable for each organ type
        ## For example lungs organ (which is RecNeg) has four variable: P_v, P*_v, P_int, P*_int

        self.ArtVeinDict = dict()
        self.LungsDict = dict()
        self.RecNegDict = dict()
        self.RecPosDict = dict()

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
        self.typesMapDict_bigVect = {self.typesList[0]: ArtVeinMap_bigVect,
                                     self.typesList[1]: RecNegMap_bigVect,
                                     ## This is for lungs which is a special kind of RecNeg
                                     self.typesList[2]: RecNegMap_bigVect,
                                     self.typesList[3]: RecPosMap_bigVect}

        ArtVeinMap_V_Vect = {"P": 0, "P*": 1}
        RecNegMap_V_Vect = {"P_v": 0, "P*_v": 1, "P_int": 2, "P*_int": 3}
        RecPosMap_V_Vect = {"P_v": 0, "P*_v": 1, "P_int": 2, "P*_int": 3, "RP": 4, "RP*": 5, "P_intern": 6,
                             "P*_intern": 7}
        self.typesMapDict_V_Vect = {self.typesList[0]: ArtVeinMap_V_Vect,
                                     self.typesList[1]: RecNegMap_V_Vect,
                                     ## This is for lungs which is a special kind of RecNeg
                                     self.typesList[2]: RecNegMap_V_Vect,
                                     self.typesList[3]: RecPosMap_V_Vect}


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

        self.typesMapDict_sysMat = {self.typesList[0]: ArtVeinMap_sysMat,
                             self.typesList[1]: RecNegMap_sysMat,  ## This is for lungs which is a special kind of RecNeg
                             self.typesList[2]: RecNegMap_sysMat,
                             self.typesList[3]: RecPosMap_sysMat}


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


    # def createV_Vect(self):
    #     self.V_Vect = np.zeros(self.organs.N)
    #     pointer = 0
    #     for type in self.organs.typesList:  ## ArtVein, Lungs, RecNeg, RecPos
    #         for organ in self.organs.therapy.Organs[type]:
    #             organDict = self.organs.organsDict[type][organ["name"]]
    #             for variableName in organDict["V_VectMap"].keys():
    #                 self.BigVect[pointer] = organ[variableName]
    #                 pointer += 1


class SystemMatrixEncoder:
    def __init__(self, organs):
        self.organs = organs
        self.createSysMat()

    def createSysMat(self):
        self.SystemMat = np.zeros((self.organs.N,self.organs.N))
        pointer = 0
        #debugList = [self.organs.typesList["RecPos"]]
        debugList = ["RecPos", "RecNeg", "Lungs"]
        for type in self.organs.typesList:  ## ArtVein, Lungs, RecNeg, RecPos
            for organ in self.organs.patient.Organs[type]:  ## [Art, Vein] | [Lungs] | [RecNeg1, RecNeg2, ...] | [RecPos1, ...]
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

                        subMat[pos[0], pos[1]] += sign*organ[paramName]

                x1 = subMat_initialPosition[0,0]
                y1 = x1
                x2 = x1 + L
                y2 = x2
                self.SystemMat[x1:x2, y1:y2] = subMat.copy()
                if type == "RecPos" or type ==  "RecNeg": ## The outer F insertion
                    self.SystemMat[x1, 0] = organ['F']
                    self.SystemMat[x1+1, 1] = organ['F']

                    self.SystemMat[2,x1] = organ['F']
                    self.SystemMat[3,x1+1] = organ['F']

                if type == "Lungs":
                    shift =2
                    self.SystemMat[x1,0+shift] = organ['F']
                    self.SystemMat[x1+1,1+shift] = organ['F']

                    self.SystemMat[0, x1] = organ['F']
                    self.SystemMat[1, x1+1] = organ['F']

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
