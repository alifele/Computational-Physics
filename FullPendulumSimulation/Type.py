class Type:
    def __init__(self, name, nParticles, ForceFrom, ForceTo):
        self.ForceMatrix = None
        self.name = name
        self.nParticles = nParticles
        self.ForceFrom = ForceFrom
        self.ForceTo = ForceTo
        self.Particles = []
