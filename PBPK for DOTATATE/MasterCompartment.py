from FreePeptideClass import FreePeptide, FreePeptideList


class MasterCompartment:

    def __init__(self, MC_parameters, variables, simParameters, OrgansList):

        self.name = ""
        self.P = FreePeptide()

        self.P.P_unlabeled = variables["P_unlabeled"]
        self.P.P_labeled = variables["P_labeled"]


        ## Note that we do not need aux variables for this compartment (because of the way we implement the equations)
        # self.P_unlabeled_aux= self.P.P_unlabeled
        # self.P_labeled_aux= self.P.P_labeled
        self.parameters = MC_parameters
        self.F = MC_parameters["F"]
        self.V = MC_parameters["V_total"]
        self.lambda_phy = MC_parameters["lambda_phy"]

        self.tmax = simParameters["tmax"]
        self.level = simParameters["level"]
        self.N_t = simParameters["N_t"]
        self.dt = simParameters["dt"]

        self.OrgansList = OrgansList

        self.PList = FreePeptideList(self.N_t)


        for i,organ in enumerate(self.OrgansList):
            if type(organ).__name__ == "GI":
                self.GI_ID = i
                continue  ## This has the same effect of subtracting

            if type(organ).__name__ == "Spleen":
                self.Spleen_ID = i
                continue  ## This has the same effect of subtracting

            if type(organ).__name__ == "Liver":
                self.Liver_ID = i

            if type(organ).__name__ == "BloodProteinComplex":
                self.PPC_ID = i  ## I need this because I need the value of
                ## K_pr for following calculations which is
                ## stored inside the PlasmaProteinComplex

            if type(organ).__name__ == "Vein":
                self.Vein_ID = i  ## I need this because I need the value of
                ## Vein.P for following calculations which is
                ## stored inside the Vein

            if type(organ).__name__ == "Lungs":
                self.Lungs_ID = i ## I need this to update the Art differential equations


    def Calculate(self,t):
        if self.name == "Art":
            ResultofSum_unlabeled = 0.0
            ResultofSum_labeled = 0.0
            for i, organ in enumerate(self.OrgansList):
                if organ.name == "BloodProteinComplex" or organ.name == "Vein" or organ.name == "Art":
                    continue

                ResultofSum_unlabeled += (-organ.F / self.V * self.P.P_labeled) * self.dt
                ResultofSum_labeled += (-organ.F / self.V * self.P.P_unlabeled) * self.dt


            ResultofSum_unlabeled += (self.F/self.OrgansList[self.Lungs_ID].V_v * self.OrgansList[self.Lungs_ID].P.vascular_unlabeled +
                                    self.lambda_phy*self.P.P_labeled)*self.dt
            ResultofSum_labeled += (self.F / self.OrgansList[self.Lungs_ID].V_v * self.OrgansList[self.Lungs_ID].P.vascular_labeled -
                                      self.lambda_phy * self.P.P_labeled) * self.dt

            self.P.P_unlabeled = ResultofSum_unlabeled
            self.P.P_labeled = ResultofSum_labeled

        if self.name == "Vein":
            ResultofSum_unlabeled = 0.0
            ResultofSum_labeled = 0.0
            for i,organ in enumerate(self.OrgansList):
                if organ.name == "BloodProteinComplex" or organ.name == "Vein" or organ.name == "Art":
                    continue

                ResultofSum_unlabeled += (organ.F/organ.V_v * organ.P.vascular_unlabeled)*self.dt
                ResultofSum_labeled += (organ.F/organ.V_v * organ.P.vascular_labeled)*self.dt



            ResultofSum_unlabeled += (-self.OrgansList[self.PPC_ID].K_pr * self.P.P_unlabeled +
                                      (self.OrgansList[self.Spleen_ID].F + self.OrgansList[self.GI_ID].F) /
                                      (self.OrgansList[self.Liver_ID].V_v) * self.OrgansList[self.Liver_ID].P.vascular_unlabeled +
                                      self.lambda_phy*self.P.P_labeled)*self.dt

            ResultofSum_labeled += (-self.OrgansList[self.PPC_ID].K_pr * self.P.P_labeled +
                                      (self.OrgansList[self.Spleen_ID].F + self.OrgansList[self.GI_ID].F) /
                                      (self.OrgansList[self.Liver_ID].V_v) * self.OrgansList[self.Liver_ID].P.vascular_labeled -
                                      self.lambda_phy * self.P.P_labeled) * self.dt

            self.P.P_unlabeled = ResultofSum_unlabeled
            self.P.P_labeled = ResultofSum_labeled






        self.PList.P_labeled[t] = self.P.P_labeled
        self.PList.P_unlabeled[t] = self.P.P_unlabeled


