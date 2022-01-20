## Should be similar to ReceptorNegativeOrgans

## The organs that I will put here are:

# Liver
# Spleen
# Tumor
# Red Marrow
# GI
# Muscle
# Prostate/Uterus
# Adrenals
# Rest

## These Organs has SSTR2 Receptors and ligands can bind to it. Also the ligands can
## get internalized



from ReceptorPositiveCompartment import ReceptorPositiveCompartment


class Liver(ReceptorPositiveCompartment):
    def __init__(self, RPC_parameters, variables, simParameters):
        super().__init__(RPC_parameters, variables, simParameters)
        self.name = "Liver"


class Spleen(ReceptorPositiveCompartment):
    def __init__(self, RPC_parameters, variables, simParameters):
        super().__init__(RPC_parameters, variables, simParameters)
        self.name = "Spleen"


class Tumor(ReceptorPositiveCompartment):
    def __init__(self, RPC_parameters, variables, simParameters):
        super().__init__(RPC_parameters, variables, simParameters)
        self.name = "Tumor"


class RedMarrow(ReceptorPositiveCompartment):
    def __init__(self, RPC_parameters, variables, simParameters):
        super().__init__(RPC_parameters, variables, simParameters)
        self.name = "RedMarrow"


class GI(ReceptorPositiveCompartment):
    def __init__(self, RPC_parameters, variables, simParameters):
        super().__init__(RPC_parameters, variables, simParameters)
        self.name = "GI"


class Muscle(ReceptorPositiveCompartment):
    def __init__(self, RPC_parameters, variables, simParameters):
        super().__init__(RPC_parameters, variables, simParameters)
        self.name = "Muscle"
        
class ProstateUterus(ReceptorPositiveCompartment):
    def __init__(self, RPC_parameters, variables, simParameters):
        super().__init__(RPC_parameters, variables, simParameters)
        self.name = "Prostate_Uterus"
        
class Adrenals(ReceptorPositiveCompartment):
    def __init__(self, RPC_parameters, variables, simParameters):
        super().__init__(RPC_parameters, variables, simParameters)
        self.name = "Adrenals"
        
        
class Rest(ReceptorPositiveCompartment):
    def __init__(self, RPC_parameters, variables, simParameters):
        super().__init__(RPC_parameters, variables, simParameters)
        self.name = "Rest"
