form FreePeptideClass import FreePeptide

class MasterCompartments:
    def __init__(self, parameters, variables):
        self.parameters = parameters
        self.variables = variables # initial values of the variables

        self.P = FreePeptide()
        self.P.P = variables["P"]
        self.F = parameters["F"]
        self.V = parameters["V"]


    def RUN(self):
        pass

