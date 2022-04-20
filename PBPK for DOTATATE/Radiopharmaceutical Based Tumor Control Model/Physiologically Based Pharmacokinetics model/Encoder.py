import numpy as np



class Encoder:

    def __init__(self, patient, therapy):
        self.organsObj = Organs(patient, therapy)
        self.bigVectEncoder = BigVectEncoder(self.organsObj)
        #systemMatricEncoder = SystemMatrixEncoder(self.organsObj)



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


    def initOrgansDict(self):
        pointer = 0
        for i, type in enumerate(self.typesList):  ## ArtVein, Lungs, RecNeg, RecPos
            length = self.typeLengthDict[type]
            stencil = self.stencil
            stencil["length"] = length

            for organ in self.therapy.Organs[type]:
                organDict = dict()
                organDict["name"] = organ["name"]
                organDict["stencil"] = stencil.copy()
                organDict["type"] = type
                organDict["map"] = self.typesMapDict[type]
                organDict["stencil"]["base"] = pointer
                pointer += organDict["stencil"]["length"]
                self.organsDict[type][organ["name"]] = organDict

    def defineLowLevelVariables(self):
        self.typeLengthDict = {self.typesList[0]: 2,
                               self.typesList[1]: 4,  ## This is the lungs which is a special kind of Recp Neg
                               self.typesList[2]: 4,
                               self.typesList[3]: 8}  ## This is the number of variable for each organ type
        ## For example lungs organ (which is RecNeg) has four variable: P_v, P*_v, P_int, P*_int

        self.stencil = {"base": 0, "length": 0}  ## This stencil will help to make the BigVector variable
        ## stencil contains the base and length. For example for organ_i base
        ## 15 means that BigVect[15] is the start of the variables for this
        ## Organ

        ## The following lists show the shift for each variable. For example for organ_i that is RecPos kind,
        ## RecPos["P*_intern"] = 6. So it means that in the BigVec, corresponding variable is located with 6 shift form
        ## the base of that organ (i.e. if the base is 56, then BigVec[56+6] is P*_intern for organ_i
        ArtVeinMap = {"P": 0, "P*": 1}
        RecNegMap = {"P_v": 0, "P*_v": 1, "P_int": 2, "P*_int": 3}
        RecPosMap = {"P_v": 0, "P*_v": 1, "P_int": 2, "P*_int": 3, "RP": 4, "RP*": 5, "P_intern": 6, "P*_intern": 7}
        self.typesMapDict = {self.typesList[0]: ArtVeinMap,
                             self.typesList[1]: RecNegMap,  ## This is for lungs which is a special kind of RecNeg
                             self.typesList[2]: RecNegMap,
                             self.typesList[3]: RecPosMap}

        self.ArtVeinDict = dict()
        self.LungsDict = dict()
        self.RecNegDict = dict()
        self.RecPosDict = dict()




class BigVectEncoder:
    """
    #### To see the important note about this class go to the end of this file
    """
    # def __init__(self, patientObj, therapyObj):
    #     self.patient = patientObj
    #     self.therapy = therapyObj
    #     self.typesList = ["ArtVein", "Lungs", "RecNeg", "RecPos"]
    #
    #
    #     self.defineLowLevelVariables()
    #
    #     self.organsDict = {self.typesList[0]: self.ArtVeinDict,
    #                      self.typesList[1]: self.LungsDict,  ## This is for lungs which is a special kind of RecNeg
    #                      self.typesList[2]: self.RecNegDict,
    #                      self.typesList[3]: self.RecPosDict}
    #
    #
    # def encode(self):
    #
    #     self.initOrgansDict()   ## These dictionaries will help in making the BigVect variable
    #     ## Also these dictionaries will be useful in accessing the variables of each organ
    #     self.createBigVect()

    def __init__(self, organs):
        self.organs = organs
        self.createBigVect()



    def createBigVect(self):
        ## BigVect is the biggest vector in the world that contains all of the variables of the model
        ## P_Art, P*_Art, P_Vein, P*_Vein, P_v_Lungs, P*_v_Lungs, etc
        ## First we should calculate the N. N is the length of BigVect
        self.N = 0
        for type in self.organs.typesList:
            self.N += self.organs.organsDict[type].__len__() * self.organs.typeLengthDict[type]

        self.BigVect = np.zeros(self.N)
        pointer = 0
        for type in self.organs.typesList: ## ArtVein, Lungs, RecNeg, RecPos
            for organ in self.organs.therapy.Organs[type]:
                organDict = self.organs.organsDict[type][organ["name"]]
                for variableName in organDict["map"].keys():
                    self.BigVect[pointer] = organ[variableName]
                    pointer += 1




    #
    # def initOrgansDict(self):
    #     pointer = 0
    #     for i, type in enumerate(self.typesList): ## ArtVein, Lungs, RecNeg, RecPos
    #         length = self.typeLengthDict[type]
    #         stencil = self.stencil
    #         stencil["length"] = length
    #
    #         for organ in self.therapy.Organs[type]:
    #             organDict = dict()
    #             organDict["name"] = organ["name"]
    #             organDict["stencil"] = stencil.copy()
    #             organDict["type"] = type
    #             organDict["map"] = self.typesMapDict[type]
    #             organDict["stencil"]["base"] = pointer
    #             pointer += organDict["stencil"]["length"]
    #             self.organsDict[type][organ["name"]] = organDict
    #
    #
    # def defineLowLevelVariables(self):
    #     self.typeLengthDict = {self.typesList[0]: 2,
    #                            self.typesList[1]: 4,  ## This is the lungs which is a special kind of Recp Neg
    #                            self.typesList[2]: 4,
    #                            self.typesList[3]: 8}  ## This is the number of variable for each organ type
    #     ## For example lungs organ (which is RecNeg) has four variable: P_v, P*_v, P_int, P*_int
    #
    #     self.stencil = {"base": 0, "length": 0}  ## This stencil will help to make the BigVector variable
    #     ## stencil contains the base and length. For example for organ_i base
    #     ## 15 means that BigVect[15] is the start of the variables for this
    #     ## Organ
    #
    #     ## The following lists show the shift for each variable. For example for organ_i that is RecPos kind,
    #     ## RecPos["P*_intern"] = 6. So it means that in the BigVec, corresponding variable is located with 6 shift form
    #     ## the base of that organ (i.e. if the base is 56, then BigVec[56+6] is P*_intern for organ_i
    #     ArtVeinMap = {"P": 0, "P*": 1}
    #     RecNegMap = {"P_v": 0, "P*_v": 1, "P_int": 2, "P*_int": 3}
    #     RecPosMap = {"P_v": 0, "P*_v": 1, "P_int": 2, "P*_int": 3, "RP": 4, "RP*": 5, "P_intern": 6, "P*_intern": 7}
    #     self.typesMapDict = {self.typesList[0]: ArtVeinMap,
    #                          self.typesList[1]: RecNegMap,  ## This is for lungs which is a special kind of RecNeg
    #                          self.typesList[2]: RecNegMap,
    #                          self.typesList[3]: RecPosMap}
    #
    #     self.ArtVeinDict = dict()
    #     self.LungsDict = dict()
    #     self.RecNegDict = dict()
    #     self.RecPosDict = dict()
    #



class SystemMatrixEncoder:
    def __init__(self, patientObj, therapyObj):
        self.patient = patientObj
        self.therapy = therapyObj
        self.typesList = ["ArtVein", "Lungs", "RecNeg", "RecPos"]

        self.defineLowLevelVariables()
        self.initOrgansDict()


    def encode(self):
        pass


    def initOrgansDict(self):
        pointer = np.array([0,0])
        self.typesList = ["RecPos"] ## This is for debug purpose only. I want to first build systems matrix for RecPos
        for i, type in enumerate(self.typesList):  ## ArtVein, Lungs, RecNeg, RecPos
            length = self.typeLengthDict[type]
            stencil = self.stencil
            stencil["length"] = length

            for organ in self.therapy.Organs[type]:
                organDict = dict()
                organDict["name"] = organ["name"]
                organDict["stencil"] = stencil.copy()
                organDict["type"] = type
                organDict["map"] = self.typesMapDict[type]
                organDict["stencil"]["base"] = pointer
                pointer += organDict["stencil"]["length"]
                self.organsDict[type][organ["name"]] = organDict



    def defineLowLevelVariables(self):
        self.typeLengthDict = {self.typesList[0]: np.array([2,2]),
                               self.typesList[1]: np.array([4,4]),  ## This is the lungs which is a special kind of Recp Neg
                               self.typesList[2]: np.array([4,4]),
                               self.typesList[3]: np.array([8,8])}  ## This is the number of variable for each organ type
        ## For example lungs organ (which is RecNeg) has four variable: P_v, P*_v, P_int, P*_int

        self.stencil = {"base": np.array([0,0]), "length": np.array([0,0])}  ## This stencil will help to make the BigVector variable
        ## stencil contains the base and length. For example for organ_i base
        ## 15 means that BigVect[15] is the start of the variables for this
        ## Organ

        ## The following lists show the shift for each variable. For example for organ_i that is RecPos kind,
        ## RecPos["P*_intern"] = 6. So it means that in the BigVec, corresponding variable is located with 6 shift form
        ## the base of that organ (i.e. if the base is 56, then BigVec[56+6] is P*_intern for organ_i
        ArtVeinMap = {"P": 0, "P*": 1}
        RecNegMap = {"P_v": 0, "P*_v": 1, "P_int": 2, "P*_int": 3}
        ## ToDO: I should somehow include the signs of variables as well.
        ## The third number in each [] shows the sign. i.e. [0,0,-1] means -1 sign on [0,0] position
        RecPosMap = {"F": [[0,0,-1], [1,1,-1]],
                     "PS": [[0,0,-1], [0,2,+1], [1,1-1], [1,3,+1], [2,0,+1], [2,2,-1], [3,1,+1], [3,3,-1]],
                     "K_on": [[2,2,-1], [3,3,-1], [4,2,+1], [5,3,+1]],
                     "k_off": [[2,4,+1], [3,5,+1], [4,4,-1], [5,5,-1]],
                     "lambda_intern": [[4,4,-1], [5,5,-1], [6,4,+1], [7,5,+1]],
                     "lambda_rel": [[6,6,-1], [7,7,-1]],
                     "lambda_phys": [[0,1,+1], [1,1,-1], [2,3,+1], [3,3,-1], [4,5,+1], [5,5,-1], [6,7,+1], [7,7,-1]]}
        self.typesMapDict = {self.typesList[0]: ArtVeinMap,
                             self.typesList[1]: RecNegMap,  ## This is for lungs which is a special kind of RecNeg
                             self.typesList[2]: RecNegMap,
                             self.typesList[3]: RecPosMap}

        self.ArtVeinDict = dict()
        self.LungsDict = dict()
        self.RecNegDict = dict()
        self.RecPosDict = dict()




""" #### Some notes about the BigVectEncoder class:

This class encodes the patient data to the BigVect format (i.e. the vector that contians all of the variables). 
Lots of low level classes are defined to do this conversion in a convenient way.

self.organsDict = {"ArtVein": ArtVeinDict, "Lungs": LungsDict, "RecNeg": RecNegOrgansDict, "RecPos": RecPosOrgansDict}
Note that each elements of this dictionary is itself a dictionary. For example:
RecNegOrgansDict = {"Skin": skinDict, "Bone": boneDict}
And each of the element of this dict is also a dict:
skinDict: = {"stencil": {"length": 2, "base": 41}, "type": "RecNeg", "map": map}


"""

