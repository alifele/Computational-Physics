from FreePeptideClass import FreePeptide, FreePeptideList
from ReceptorPeptideClass import *


class ComplexCompartment:
    def __init__(self, CC_parameters, variables, simParameters):

        self.name = ""
        self.P = FreePeptide()

        self.P.vascular_unlabeled = variables["P_vascular_unlabeled"]
        self.P.interstitial_unlabeled = variables["P_interstitial_unlabeled"]
        self.P.internalized_unlabeled = variables["P_internalized_unlabeled"]
        self.P.interacellular_unlabeled = variables["P_interacellular_unlabeled"]

        self.P.vascular_labeled = variables["P_vascular_labeled"]
        self.P.interstitial_labeled = variables["P_interstitial_labeled"]
        self.P.internalized_labeled = variables["P_internalized_labeled"]
        self.P.interacellular_labeled = variables["P_interacellular_labeled"]

        self.RP = ReceptorPeptide()
        self.RP.RP_labeled = variables["RP_labeled"]
        self.RP.RP_unlabeled = variables["RP_unlabeled"]
        self.RP.R = variables["R"]

        self.F = CC_parameters['F']
        self.V_v = CC_parameters['V_v']
        self.PS = CC_parameters['PS']
        self.V_int = CC_parameters['V_int']
        self.V_intera = CC_parameters["V_int"]
        self.k_on = CC_parameters['k_on']
        self.k_off = CC_parameters['k_off']
        self.lambda_int = CC_parameters['lambda_int']
        self.lambda_rel = CC_parameters['lambda_rel']
        self.lambda_phy = CC_parameters['lambda_phy']
        self.GFR = CC_parameters['GFR']
        self.theta = CC_parameters['theta']
        self.f_exc = CC_parameters['f_exc']


        self.F_fil = 0
        self.F_exc = 0

        self.tmax = simParameters["tmax"]
        self.level = simParameters["level"]
        self.N_t = simParameters["N_t"]
        self.dt = simParameters["dt"]

        self.RPList = ReceptorPeptideList(self.N_t)


    def Set_ArtVein(self, Art, Vein):
        self.Art = Art
        self.Vein = Vein

    def Calculate(self):

        ## Vascular Volume
        self.P.vascular_unlabeled += (-self.P.vascular_unlabeled/self.V_v*(self.F_fil+self.F) + self.F*self.Art.P.P_unlabeld/self.Art.V +
                                      self.P.interacellular_unlabeled/self.V_intera*(self.F_fil - self.F_exc) +
                                      self.lambda_phy*self.P.vascular_labeled)*self.dt

        self.P.vascular_labeled += (-self.P.vascular_labeled/self.V_v*(self.F_fil+self.F) + self.F*self.Art.P.P_labeld/self.Art.V -
                                      self.P.interacellular_labeled/self.V_intera*(self.F_fil - self.F_exc) -
                                      self.lambda_phy*self.P.vascular_labeled)*self.dt



        ## Interacellular Volume
        self.P.interacellular_unlabeled += (self.P.interestitial_unlabeled/self.V_int*(self.F_fil-self.F_exc) -
                                            self.P.interacellular_unlabeled/self.V_intera*(self.F_fil-self.F_exc) +
                                            self.lambda_phy*self.P.interacellular_labeled)*self.dt

        self.P.interacellular_labeled += (self.P.interestitial_labeled/self.V_int*(self.F_fil-self.F_exc) -
                                            self.P.interacellular_labeled/self.V_intera*(self.F_fil-self.F_exc) -
                                            self.lambda_phy*self.P.interacellular_labeled)*self.dt


        ## Interestitial Volume
        self.P.interestitial_unlabeled += (self.F_fil*(self.P.vascular_unlabeled/self.V_v - self.P.interestitial_unlabeled/self.V_int) -
                                           self.k_on*self.P.interestitial_unlabeled/self.V_int*self.RP.R +
                                           self.k_off*self.RP.RP_unlabeled +
                                           self.lambda_phy*self.P.interestitial_labeled)*self.dt

        self.P.interestitial_labeled += (self.F_fil*(self.P.vascular_labeled/self.V_v - self.P.interestitial_labeled/self.V_int) -
                                           self.k_on*self.P.interestitial_labeled/self.V_int*self.RP.R +
                                           self.k_off*self.RP.RP_labeled -
                                         self.lambda_phy*self.P.interestitial_labeled)*self.dt


        ## Receptor-Peptide complex Volume
        self.RP.RP_unlabeled += (self.k_on*self.P.interestitial_unlabeled/self.V_int*self.RP.R -
                                 self.RP.RP_unlabeled*(self.k_on+self.lambda_int) +
                                 self.lambda_phy*self.RP.RP_labeled)*self.dt

        self.RP.RP_labeled += (self.k_on * self.P.interestitial_labeled / self.V_int * self.RP.R -
                                 self.RP.RP_labeled * (self.k_on + self.lambda_int) -
                                 self.lambda_phy * self.RP.RP_labeled) * self.dt


        ## Internalized Volume
        self.P.internalized_unlabeled += (self.lambda_int*self.RP.RP_unlabeled - self.lambda_rel*self.P.internalized_unlabeled +
                                          self.lambda_phy*self.P.internalized_labeled)*self.dt

        self.P.internalized_labeled += (self.lambda_int * self.RP.RP_labeled - self.lambda_rel * self.P.internalized_labeled -
                                          self.lambda_phy * self.P.internalized_labeled) * self.dt




    def RUN(self):
        pass

