from ReceptorPeptideClass import *


class SimpleCompartment:

    def __init__(self, SC_parameters, variables, simParameters):

        self.name = ""
        self.PPR = ReceptorPeptide()

        self.PPR.PPR_labeled = variables["PPR_labeled"]
        self.PPR.PPR_unlabeled = variables["PPR_unlabeled"]

        self.K_pr = SC_parameters["K_pr"]

        self.tmax = simParameters["tmax"]
        self.level = simParameters["level"]
        self.N_t = simParameters["N_t"]
        self.dt = simParameters["dt"]

    def Set_ArtVein(self, Art, Vein):
        self.Art = Art
        self.Vein = Vein

    def Calculate(self):
        if self.name == "Art":
            pass

        if self.name == "Vein":
            pass
