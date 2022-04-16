class BigVectEncoder:
    def __init__(self, patientObj, therapyObj):
        self.patient = patientObj
        self.therapy = therapyObj
        self.typesList = ["ArtVein", "Lungs", "RecNeg", "RecPos"]
        self.typeLengthDict = {self.typesList[0]: 2,
                               self.typesList[1]: 4,    ## This is the lungs which is a special kind of Recp Neg
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
        ArtVeinMap = ["P", "P*"]
        RecNegMap = ["P_v", "P*_v", "P_int", "P*_int"]
        RecPosMap = ["P_v", "P*_v", "P_int", "P*_int", "RP", "RP*", "P_intern", "P*_intern"]
        self.typesMaps = {self.typesList[0]: ArtVeinMap,
                     self.typesList[1]: RecNegMap,  ## This is for lungs which is a special kind of RecNeg
                     self.typesList[2]: RecNegMap,
                     self.typesList[3]: RecPosMap}

        self.ArtVeinDict = dict()
        self.LungsDict = dict()
        self.RecNegDict = dict()
        self.RecPosDict = dict()
        self.organsDict = {self.typesList[0]: self.ArtVeinDict,
                         self.typesList[1]: self.LungsDict,  ## This is for lungs which is a special kind of RecNeg
                         self.typesList[2]: self.RecNegDict,
                         self.typesList[3]: self.RecPosDict}


        self.initOrgansDict()   ## These dictionaries will help in making the BigVect variable
        ## Also these dictionaries will be useful in accessing the variables of each organ



    def initOrgansDict(self):
        pointer = 0
        for i, type in enumerate(self.typesList): ## ArtVein, Lungs, RecNeg, RecPos
            length = self.typeLengthDict[type]
            stencil = self.stencil
            stencil["length"] = length

            for organ in self.therapy.Organs[type]:
                organDict = dict()
                organDict["stencil"] = stencil.copy()
                organDict["type"] = type
                organDict["stencil"]["base"] = pointer
                pointer += organDict["stencil"]["length"]
                self.organsDict[type][organ["name"]] = organDict






class SystemMatrixEncoder:
    pass
