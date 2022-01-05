from FreePeptideClass import FreePeptide, FreePeptideList


class MasterCompartment:

    def __init__(self, MC_parameters, variables, simParameters, Art, Vein):

        self.name = ""
        self.P = FreePeptide()

        self.P.P_unlabeled = variables["P_unlabeled"]
        self.P.P_labeled = variables["P_labeled"]

        self.F = MC_parameters["F"]
        self.V = MC_parameters["V"]

        self.tmax = simParameters["tmax"]
        self.level = simParameters["level"]
        self.N_t = simParameters["N_t"]
        self.dt = simParameters["dt"]

    def Calculate(self):
        if self.name == "Art":
            pass

        if self.name == "Vein":
            pass

