import numpy as np
from FreePeptideClass import FreePeptide, FreePeptideList
class ReceptorNegativeCompartment:
    def __init__(self, RNC_parameters, variables, simParameters, Art, Vein):
        self.parameters = RNC_parameters
        self.variables = variables # initial values of the variables


        self.name = ""
        self.P = FreePeptide()

        self.P.vascular_unlabeled = variables["P_vascular_unlabeled"]
        self.P.interstitial_unlabeled = variables["P_interstitial_unlabeled"]
        self.P.vascular_labeled = variables["P_vascular_labeled"]
        self.P.interstitial_labeled = variables["P_interstitial_labeled"]

        self.F = RNC_parameters['F']
        self.V_v = RNC_parameters['V_v']
        self.PS = RNC_parameters['PS']
        self.V_int = RNC_parameters['V_int']
        self.lambda_phy = RNC_parameters['lambda_phy']
        self.F_ART = RNC_parameters['F_ART']

        self.tmax = simParameters["tmax"]
        self.level = simParameters["level"]
        self.N_t = simParameters["N_t"]
        self.dt = simParameters["dt"]

        self.Art = Art
        self.Vein  = Vein

        self.PList = FreePeptideList(self.N_t)

    def Calculate(self,t):  #definint the differential equations

        if self.name != "lungs":
            self.P.vascular_unlabeled += (self.F*(self.Art.P/self.Art.V - self.P.vascular_unlabeled/self.V_v) +
                                          self.PS*(self.P.interestitial_unlabeled/self.V_int - self.P.vascular_unlabeled/self.V_v) +
                                          self.lambda_phy*self.P.vascular_labeled)*self.dt

            self.P.vascular_labeled += (self.F*(self.Art.P/self.Art.V - self.P.vascular_labeled/self.V_v) +
                                          self.PS*(self.P.interestitial_labeled/self.V_int - self.P.vascular_labeled/self.V_v) -
                                          self.lambda_phy*self.P.vascular_labeled)*self.dt

            self.P.interestitial_unlabeled += (self.PS*(self.P.vascular_unlabeled/self.V_v - self.P.interestitial_unlabeled/self.V_int) +
                                              self.lambda_phy*self.P.interestitial_labeled)*self.dt

            self.P.interestitial_labeled += (self.PS*(self.P.vascular_labeled/self.V_v - self.P.interestitial_labeled/self.V_int) -
                                              self.lambda_phy*self.P.interestitial_labeled)*self.dt

        else:
            self.P.vascular_unlabeled += (self.Art.F * (self.Vein.P / self.Vein.V - self.P.vascular_unlabeled / self.V_v) +
                                          self.PS * (self.P.interestitial_unlabeled / self.V_int - self.P.vascular_unlabeled / self.V_v) +
                                          self.lambda_phy * self.P.vascular_labeled) * self.dt

            self.P.vascular_labeled += (self.Art.F * ( self.Vein.P / self.Vein.V - self.P.vascular_labeled / self.V_v) +
                                          self.PS * (self.P.interestitial_labeled / self.V_int - self.P.vascular_labeled / self.V_v) -
                                          self.lambda_phy * self.P.vascular_labeled) * self.dt

            self.P.interestitial_unlabeled += (self.PS * (self.P.vascular_unlabeled / self.V_v - self.P.interestitial_unlabeled / self.V_int) +
                                               self.lambda_phy * self.P.interestitial_labeled) * self.dt

            self.P.interestitial_labeled += (self.PS * (self.P.vascular_labeled / self.V_v - self.P.interestitial_labeled / self.V_int) -
                                             self.lambda_phy * self.P.interestitial_labeled) * self.dt


        self.PList.vascular_unlabeled[t] = self.P.vascular_unlabeled
        self.PList.vascular_labeled[t] = self.P.vascular_labeled
        self.PList.interestitial_unlabeled[t] = self.P.interestitial_unlabeled
        self.PList.interestitial_labeled[t] = self.P.interestitial_labeled


    def RUN(self):
        pass

