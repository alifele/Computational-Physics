from MasterCompartment import MasterCompartment


class Art(MasterCompartment):
    def __init__(self, MC_parameters, variables, simParameters, OrgansList):
        super().__init__(MC_parameters, variables, simParameters, OrgansList)
        self.name = "Art"

class Vein(MasterCompartment):
    def __init__(self, MC_parameters, variables, simParameters, OrgansList):
        super().__init__(MC_parameters, variables, simParameters, OrgansList)
        self.name = "Vein"