class ComplexCompartment:
    def __init__(self, parameters, variables):
        self.parameters = parameters
        self.variables = variables # initial values of the variables

        self.P = variables["P"]
        self.RP = variables["RP"]
        self.R = variables["R"]
        self.F = parameters['F']
        self.V_v = parameters['V_v']
        self.PS = parameters['PS']
        self.V_int = parameters['V_int']
        self.k_on = parameters['k_on']
        self.k_off = parameters['k_off']
        self.lambda_int = parameters['lambda_int']
        self.lambda_rel = parameters['lambda_rel']
        self.lambda_phy = parameters['lambda_phy']
        self.GFR = parameters['GFR']
        self.theta = parameters['theta']
        self.f_exc = parameters['f_exc']

    def RUN(self):
        pass

