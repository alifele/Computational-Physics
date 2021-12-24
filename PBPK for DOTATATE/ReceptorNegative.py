import numpy as np
from FreePeptideClass import FreePeptide, FreePeptideList
class ReceptorNegative:
    def __init__(self, parameters, variables, simParameters, Art, Vein):
        self.parameters = parameters
        self.variables = variables # initial values of the variables


        self.name = ""
        self.P = FreePeptide()
        self.P.vascular_unlabeled = variables["P_vascular_unlabeled"]
        self.P.interstitial_unlabeled = variables["P_interstitial_unlabeled"]
        self.P.vascular_labeled = variables["P_vascular_labeled"]
        self.P.interstitial_labeled = variables["P_interstitial_labeled"]

        self.F = parameters['F']
        self.V_v = parameters['V_v']
        self.PS = parameters['PS']
        self.V_int = parameters['V_int']
        self.lambda_phy = parameters['lambda_phy']
        self.F_ART = parameters['ART']

        self.tmax = simParameters["tmax"]
        self.level = simParameters["level"]
        self.N_t = np.power(2,self.level)
        self.dt = self.tmax / self.N_t

        self.Art = Art
        self.Vein  = Vein

        self.PList = FreePeptideList(self.N_t)

    def Calculate(self,t):  #definint the differential equations

        if self.name != "lung":
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

            self.P.vascular_unlabeled += (self.Art.F * ( self.Vein.P / self.Vein.V - self.P.vascular_labeled / self.V_v) +
                                          self.PS * (self.P.interestitial_unlabeled / self.V_int - self.P.vascular_unlabeled / self.V_v) +
                                          self.lambda_phy * self.P.vascular_labeled) * self.dt

            self.P.interestitial_unlabeled += (self.PS * (
                        self.P.vascular_unlabeled / self.V_v - self.P.interestitial_unlabeled / self.V_int) +
                                               self.lambda_phy * self.P.interestitial_labeled) * self.dt

            self.P.interestitial_labeled += (self.PS * (
                        self.P.vascular_labeled / self.V_v - self.P.interestitial_labeled / self.V_int) -
                                             self.lambda_phy * self.P.interestitial_labeled) * self.dt


        self.PList.vascular_unlabeled[t] = self.P.vascular_unlabeled
        self.PList.vascular_labeled[t] = self.P.vascular_labeled
        self.PList.interestitial_unlabeled[t] = self.P.interestitial_unlabeled
        self.PList.interestitial_labeled[t] = self.P.interestitial_labeled


    def RUN(self):
        pass

