from SimpleCompartment import SimpleCompartment


class BloodPlasmaProteinComplex(SimpleCompartment):
    def __init__(self, RPC_parameters, variables, simParameters):
        super().__init__(RPC_parameters, variables, simParameters)
        self.name = "Art"

