from FreePeptideClass import FreePeptide, FreePeptideList
from ReceptorPeptideClass import *


class ComplexCompartment:
    def __init__(self, CC_parameters, variables, simParameters):


        self.name = ""
        self.P = FreePeptide()

        self.P.vascular_unlabeled = variables["P_vascular_unlabeled"]
        self.P.interestitial_unlabeled = variables["P_interestitial_unlabeled"]
        self.P.internalized_unlabeled = variables["P_internalized_unlabeled"]
        self.P.interacellular_unlabeled = variables["P_interacellular_unlabeled"]

        self.P.vascular_labeled = variables["P_vascular_labeled"]
        self.P.interestitial_labeled = variables["P_interestitial_labeled"]
        self.P.internalized_labeled = variables["P_internalized_labeled"]
        self.P.interacellular_labeled = variables["P_interacellular_labeled"]

        self.P_vascular_unlabeled_aux = self.P.vascular_unlabeled
        self.P_interestitial_unlabeled_aux = self.P.interestitial_unlabeled
        self.P_internalized_unlabeled_aux = self.P.internalized_unlabeled
        self.P_interacellular_unlabeled_aux = self.P.interacellular_unlabeled

        self.P_vascular_labeled_aux = self.P.vascular_labeled
        self.P_interestitial_labeled_aux = self.P.interestitial_labeled
        self.P_internalized_labeled_aux = self.P.internalized_labeled
        self.P_interacellular_labeled_aux = self.P.interacellular_labeled

        self.RP = ReceptorPeptide()
        self.RP.RP_labeled = variables["RP_labeled"]
        self.RP.RP_unlabeled = variables["RP_unlabeled"]
        self.RP.R = variables["R"]

        self.RP_labeled_aux = self.RP.RP_labeled
        self.RP_unlabeled_aux = self.RP.RP_unlabeled
        self.R_aux = self.RP.R

        self.parameters = CC_parameters
        self.F = CC_parameters['F']
        self.V_v = CC_parameters['V_v']
        self.V_int = CC_parameters['V_int']
        self.V_intera = CC_parameters["V_int"]
        self.k_on = CC_parameters['k_on']
        self.k_off = CC_parameters['k_off']
        self.lambda_int = CC_parameters['lambda_int']
        self.lambda_rel = CC_parameters['lambda_rel']
        self.lambda_phy = CC_parameters['lambda_phy']
        self.GFR = CC_parameters['GFR']
        self.phi = CC_parameters['phi']
        self.f_exc = CC_parameters['f_exc']


        self.F_fil = self.GFR * self.phi*1
        self.F_exc = self.F_fil * self.f_exc

        self.tmax = simParameters["tmax"]
        self.level = simParameters["level"]
        self.N_t = simParameters["N_t"]
        self.dt = simParameters["dt"]

        self.RPList = ReceptorPeptideList(self.N_t)
        self.PList = FreePeptideList(self.N_t)


    def Set_ArtVein(self, Art, Vein):
        self.Art = Art
        self.Vein = Vein

    def Calculate(self,t):

        ## Vascular Volume
        self.P_vascular_unlabeled_aux += (-self.P.vascular_unlabeled/self.V_v *(self.F_fil+self.F) + self.F*self.Art.P.P_unlabeled/self.Art.V +
                                      self.P.interacellular_unlabeled/self.V_intera*(self.F_fil - self.F_exc) +
                                      self.lambda_phy*self.P.vascular_labeled)*self.dt

        self.P_vascular_labeled_aux += (-self.P.vascular_labeled/self.V_v*(self.F_fil+self.F) + self.F*self.Art.P.P_labeled/self.Art.V +
                                      self.P.interacellular_labeled/self.V_intera*(self.F_fil - self.F_exc) -
                                      self.lambda_phy*self.P.vascular_labeled)*self.dt



        ## Interacellular Volume
        self.P_interacellular_unlabeled_aux += (self.P.interestitial_unlabeled/self.V_int*(self.F_fil-self.F_exc) -
                                            self.P.interacellular_unlabeled/self.V_intera*(self.F_fil-self.F_exc) +
                                            self.lambda_phy*self.P.interacellular_labeled)*self.dt

        self.P_interacellular_labeled_aux += (self.P.interestitial_labeled/self.V_int*(self.F_fil-self.F_exc) -
                                            self.P.interacellular_labeled/self.V_intera*(self.F_fil-self.F_exc) -
                                            self.lambda_phy*self.P.interacellular_labeled)*self.dt


        ## Interestitial Volume
        self.P_interestitial_unlabeled_aux += (self.F_fil*(self.P.vascular_unlabeled/self.V_v - self.P.interestitial_unlabeled/self.V_int) -
                                           self.k_on*self.P.interestitial_unlabeled/self.V_int*self.RP.R +
                                           self.k_off*self.RP.RP_unlabeled +
                                           self.lambda_phy*self.P.interestitial_labeled)*self.dt

        self.P_interestitial_labeled_aux += (self.F_fil*(self.P.vascular_labeled/self.V_v - self.P.interestitial_labeled/self.V_int) -
                                           self.k_on*self.P.interestitial_labeled/self.V_int*self.RP.R +
                                           self.k_off*self.RP.RP_labeled -
                                         self.lambda_phy*self.P.interestitial_labeled)*self.dt


        ## Receptor-Peptide complex Volume
        self.RP_unlabeled_aux += (self.k_on*self.P.interestitial_unlabeled/self.V_int*self.RP.R -
                                 self.RP.RP_unlabeled*(self.k_off+self.lambda_int) +
                                 self.lambda_phy*self.RP.RP_labeled)*self.dt

        self.RP_labeled_aux += (self.k_on * self.P.interestitial_labeled / self.V_int * self.RP.R -
                                 self.RP.RP_labeled * (self.k_off + self.lambda_int) -
                                 self.lambda_phy * self.RP.RP_labeled) * self.dt


        ## Internalized Volume
        self.P_internalized_unlabeled_aux += (self.lambda_int*self.RP.RP_unlabeled - self.lambda_rel*self.P.internalized_unlabeled +
                                          self.lambda_phy*self.P.internalized_labeled)*self.dt

        self.P_internalized_labeled_aux += (self.lambda_int * self.RP.RP_labeled - self.lambda_rel * self.P.internalized_labeled -
                                          self.lambda_phy * self.P.internalized_labeled) * self.dt




        ### Saving aux values in the premenant variables

        self.P.vascular_unlabeled = self.P_vascular_unlabeled_aux
        self.P.interestitial_unlabeled = self.P_interestitial_unlabeled_aux
        self.P.internalized_unlabeled = self.P_internalized_unlabeled_aux
        self.P.interacellular_unlabeled = self.P_interacellular_unlabeled_aux

        self.P.vascular_labeled = self.P_vascular_labeled_aux
        self.P.interestitial_labeled = self.P_interestitial_labeled_aux
        self.P.internalized_labeled = self.P_internalized_labeled_aux
        self.P.interacellular_labeled = self.P_interacellular_labeled_aux
        self.RP.RP_unlabeled = self.RP_unlabeled_aux
        self.RP.RP_labeled = self.RP_labeled_aux

        self.RP.R += (-self.RP.RP_unlabeled - self.RP.RP_labeled)




        ## Storing the values in the list
        self.PList.vascular_unlabeled[t] = self.P.vascular_unlabeled
        self.PList.vascular_labeled[t] = self.P.vascular_labeled

        self.PList.interestitial_unlabeled[t] = self.P.interestitial_unlabeled
        self.PList.interestitial_labeled[t] = self.P.interestitial_labeled

        self.PList.interacellular_unlabeled[t] = self.P.interacellular_unlabeled
        self.PList.interacellular_labeled[t] = self.P.interacellular_labeled

        self.PList.internalized_unlabeled[t] = self.P.internalized_unlabeled
        self.PList.internalized_labeled[t] = self.P.internalized_labeled

        self.RPList.RP_unlabeled[t] = self.RP.RP_unlabeled
        self.RPList.RP_labeled[t] = self.RP.RP_labeled
        self.RPList.R[t] = self.RP.R

    def RUN(self):
        pass

