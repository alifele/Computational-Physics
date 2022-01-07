from SimpleCompartment import SimpleCompartment


class BloodProteinComplex(SimpleCompartment):
    def __init__(self, RPC_parameters, variables, simParameters):
        super().__init__(RPC_parameters, variables, simParameters)
        self.name = "BloodProteinComplex"

