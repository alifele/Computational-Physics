class SimpleCompartment:
    def __init__(self, parameters, variables):
        self.parameters = parameters
        self.variables = variables # initial values of the variables

        self.PPR = variables["PPR"]
        self.k_PR = parameters["k_PR"]


    def RUN(self):
        pass

