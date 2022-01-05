from ComplexCompartment import ComplexCompartment


class Kidney(ComplexCompartment):
    def __init__(self, CC_parameters, variables, simParameters):
        super().__init__(CC_parameters, variables, simParameters)
        self.name = "Kidney"