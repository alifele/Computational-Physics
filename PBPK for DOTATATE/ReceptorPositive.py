from FreePeptideClass import FreePeptide, FreePeptideList
from ReceptorPeptideClass import *
import numpy as np
class ReceptorPositiveCompartment:
    def __init__(self, RPC_parameters, variables, simParameters, Art, Vein):
        self.parameters = RPC_parameters
        self.variables = variables # initial values of the variables


        self.P = FreePeptide()

        self.P.vascular_unlabeled = variables["P_vascular_unlabeled"]
        self.P.interstitial_unlabeled = variables["P_interstitial_unlabeled"]
        self.P.internalized_unlabeled = variables["P_internalized_unlabeled"]
        self.P.vascular_labeled = variables["P_vascular_labeled"]
        self.P.interstitial_labeled = variables["P_interstitial_labeled"]
        self.P.internalized_labeled = variables["P_internalized_labeled"]

        self.RP = ReceptorPeptide()
        self.RP.RP_labeled = variables["RP_labeled"]
        self.RP.RP_unlabeled = variables["RP_unlabeled"]
        self.RP.R = variables["R"]

        self.F = RPC_parameters['F']
        self.V_v = RPC_parameters['V_v']
        self.PS = RPC_parameters['PS']
        self.V_int = RPC_parameters['V_int']
        self.k_on = RPC_parameters['k_on']
        self.k_off = RPC_parameters['k_off']
        self.lambda_int = RPC_parameters['lambda_int']
        self.lambda_rel = RPC_parameters['lambda_rel']
        self.lambda_phy = RPC_parameters['lambda_phy']

        self.tmax = simParameters["tmax"]
        self.level = simParameters["level"]
        self.N_t = simParameters["N_t"]
        self.dt = simParameters["dt"]

        self.Art = Art
        self.Vein = Vein
        self.RPList = ReceptorPeptideList(self.N_t)




    def Calculate(self):

        self.P.vascular_unlabeled += (self.F * (self.Art.P / self.Art.V - self.P.vascular_unlabeled / self.V_v) +
                                      self.PS * (self.P.interestitial_unlabeled / self.V_int - self.P.vascular_unlabeled / self.V_v) +
                                      self.lambda_phy * self.P.vascular_labeled) * self.dt

        self.P.vascular_labeled += (self.F * (self.Art.P / self.Art.V - self.P.vascular_labeled / self.V_v) +
                                    self.PS * (self.P.interestitial_labeled / self.V_int - self.P.vascular_labeled / self.V_v) -
                                    self.lambda_phy * self.P.vascular_labeled) * self.dt

        self.P.interestitial_unlabeled += (self.PS*(self.P.vascular_unlabeled/self.V_v - self.P.interestitial_unlabeled/self.V_int) +
                                           self.k_off * self.RP.RP_unlabeled - self.k_on * self.RP.R * self.P.interestitial_unlabeled / self.V_int +
                                           self.lambda_phy*self.P.interestitial_labeled)*self.dt

        self.P.interestitial_labeled += (self.PS*(self.P.vascular_labeled/self.V_v - self.P.interestitial_labeled/self.V_int) +
                                         self.k_off * self.RP.RP_labeled - self.k_on * self.RP.R * self.P.interestitial_labeled / self.V_int +
                                         self.lambda_phy*self.P.interestitial_labeled)*self.dt


    def RUN(self):
        pass

