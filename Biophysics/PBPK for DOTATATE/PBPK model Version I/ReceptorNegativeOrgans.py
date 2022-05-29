from ReceptorNegativeCompartment import ReceptorNegativeCompartment


class Bone(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables, simParameters):
        super().__init__(RNC_parameters, variables, simParameters)
        self.name = "Bone"

class Heart(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables, simParameters):
        super().__init__(RNC_parameters, variables, simParameters)
        self.name = "Heart"


class Brain(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables, simParameters):
        super().__init__(RNC_parameters, variables, simParameters)
        self.name = "Brain"


class Lungs(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables, simParameters):
        super().__init__(RNC_parameters, variables, simParameters)
        self.name = "Lungs"


class Adipose(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables, simParameters):
        super().__init__(RNC_parameters, variables, simParameters)
        self.name = "Adipose"


class Skin(ReceptorNegativeCompartment):
    def __init__(self, RNC_parameters, variables, simParameters):
        super().__init__(RNC_parameters, variables, simParameters)
        self.name = "Skin"
