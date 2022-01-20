import numpy as np
from FreePeptideClass import FreePeptide, FreePeptideList
class ReceptorNegativeCompartment:
    def __init__(self, RNC_parameters, variables, simParameters):

        self.interestitial_unlabeled_aux = None
        self.name = ""
        self.P = FreePeptide()

        self.P.vascular_unlabeled = variables["P_vascular_unlabeled"]
        self.P.interestitial_unlabeled = variables["P_interestitial_unlabeled"]
        self.P.vascular_labeled = variables["P_vascular_labeled"]
        self.P.interestitial_labeled = variables["P_interestitial_labeled"]

        self.P_vascular_unlabeled_aux = self.P.vascular_unlabeled
        self.P_interestitial_unlabeled_aux = self.P.interestitial_unlabeled
        self.P_vascular_labeled_aux = self.P.vascular_labeled
        self.P_interestitial_labeled_aux = self.P.interestitial_labeled

        self.parameters = RNC_parameters
        self.F = RNC_parameters['F']
        self.V_v = RNC_parameters['V_v']
        self.PS = RNC_parameters['PS']
        self.V_int = RNC_parameters['V_int']
        self.lambda_phy = RNC_parameters['lambda_phy']

        self.tmax = simParameters["tmax"]
        self.level = simParameters["level"]
        self.N_t = simParameters["N_t"]
        self.dt = simParameters["dt"]


        self.PList = FreePeptideList(self.N_t)

    def Set_ArtVein(self, Art, Vein):
        self.Art = Art
        self.Vein = Vein

    def Calculate(self,t):  #definint the differential equations

        if self.name != "Lungs":
            self.P_vascular_unlabeled_aux += (self.F*(self.Art.P.P_unlabeled/self.Art.V - self.P.vascular_unlabeled/self.V_v) +
                                          self.PS*(self.P.interestitial_unlabeled/self.V_int - self.P.vascular_unlabeled/self.V_v) +
                                          self.lambda_phy*self.P.vascular_labeled)*self.dt

            self.P_vascular_labeled_aux += (self.F*(self.Art.P.P_labeled/self.Art.V - self.P.vascular_labeled/self.V_v) +
                                          self.PS*(self.P.interestitial_labeled/self.V_int - self.P.vascular_labeled/self.V_v) -
                                          self.lambda_phy*self.P.vascular_labeled)*self.dt

            self.P_interestitial_unlabeled_aux += (self.PS*(self.P.vascular_unlabeled/self.V_v - self.P.interestitial_unlabeled/self.V_int) +
                                              self.lambda_phy*self.P.interestitial_labeled)*self.dt

            self.P_interestitial_labeled_aux += (self.PS*(self.P.vascular_labeled/self.V_v - self.P.interestitial_labeled/self.V_int) -
                                              self.lambda_phy*self.P.interestitial_labeled)*self.dt

        else:
            self.P_vascular_unlabeled_aux += (self.Art.F * (self.Vein.P.P_labeled / self.Vein.V - self.P.vascular_unlabeled / self.V_v) +
                                          self.PS * (self.P.interestitial_unlabeled / self.V_int - self.P.vascular_unlabeled / self.V_v) +
                                          self.lambda_phy * self.P.vascular_labeled) * self.dt

            self.P_vascular_labeled_aux += (self.Art.F * ( self.Vein.P.P_labeled / self.Vein.V - self.P.vascular_labeled / self.V_v) +
                                          self.PS * (self.P.interestitial_labeled / self.V_int - self.P.vascular_labeled / self.V_v) -
                                          self.lambda_phy * self.P.vascular_labeled) * self.dt

            self.P_interestitial_unlabeled_aux += (self.PS * (self.P.vascular_unlabeled / self.V_v - self.P.interestitial_unlabeled / self.V_int) +
                                               self.lambda_phy * self.P.interestitial_labeled) * self.dt

            self.P_interestitial_labeled_aux += (self.PS * (self.P.vascular_labeled / self.V_v - self.P.interestitial_labeled / self.V_int) -
                                             self.lambda_phy * self.P.interestitial_labeled) * self.dt


        self.P.vascular_unlabeled = self.P_vascular_unlabeled_aux
        self.P.interestitial_unlabeled = self.P_interestitial_unlabeled_aux
        self.P.vascular_labeled = self.P_vascular_labeled_aux
        self.P.interestitial_labeled = self.P_interestitial_labeled_aux


        self.PList.vascular_unlabeled[t] = self.P.vascular_unlabeled
        self.PList.vascular_labeled[t] = self.P.vascular_labeled
        self.PList.interestitial_unlabeled[t] = self.P.interestitial_unlabeled
        self.PList.interestitial_labeled[t] = self.P.interestitial_labeled


    def RUN(self):
        pass

