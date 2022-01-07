from ReceptorPeptideClass import *


class SimpleCompartment:

    def __init__(self, SC_parameters, variables, simParameters):

        self.name = ""
        self.PPR = ReceptorPeptide()

        self.PPR.PPR_labeled = variables["PPR_labeled"]
        self.PPR.PPR_unlabeled = variables["PPR_unlabeled"]


        ### We do not need the aux equations for this compartment
        self.parameters = SC_parameters
        self.K_pr = SC_parameters["K_pr"]
        self.lambda_phys = SC_parameters["lambda_phy"]

        self.tmax = simParameters["tmax"]
        self.level = simParameters["level"]
        self.N_t = simParameters["N_t"]
        self.dt = simParameters["dt"]

        self.PPRList = ReceptorPeptideList(self.N_t)

    def Set_ArtVein(self, Art, Vein):
        self.Art = Art
        self.Vein = Vein

    def Calculate(self,t):
        self.PPR.PPR_unlabeled += (self.K_pr * self.Vein.P.P_unlabeled +
                                   self.lambda_phys*self.PPR.PPR_labeled)*self.dt

        self.PPR.PPR_labeled += (self.K_pr * self.Vein.P.P_labeled -
                                   self.lambda_phys * self.PPR.PPR_labeled) * self.dt



        ### Storing the values in the corresponding list
        self.PPRList.PPR_unlabeled[t] = self.PPR.PPR_unlabeled
        self.PPRList.PPR_labeled[t] = self.PPR.PPR_labeled


