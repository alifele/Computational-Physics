from ReceptorNegativeCompartment import ReceptorNegativeCompartment


class Bone(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables):
        super().__init__(RNC_parameters, variables)
        self.name = "Bone"
        self.F = 0
        self.V_v = 0
        self.PS = 0
        self.V_int = 0
        self.lambda_phy = 0


class Heart(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables):
        super().__init__(RNC_parameters, variables)
        self.name = "Heart"


class Brain(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables):
        super().__init__(RNC_parameters, variables)
        self.name = "Brain"


class Lungs(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables):
        super().__init__(RNC_parameters, variables)
        self.name = "Lungs"


class Adipose(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables):
        super().__init__(RNC_parameters, variables)
        self.name = "Adipose"


class Skin(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables):
        super().__init__(RNC_parameters, variables)
        self.name = "Skin"
