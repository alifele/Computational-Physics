import numpy as np

class Type:
    def __init__(self, name, nParticles, ForceFrom, ForceTo, coeff):
        self.ForceMatrix = None
        self.name = name
        self.nParticles = nParticles
        self.ForceFrom = ForceFrom
        self.ForceTo = ForceTo
        self.Particles = []
        self.coeff = coeff


    def calculateForceMatrix(self, typeDict):
        self.forceVector = np.zeros((self.nParticles,2))
        for i, particle in enumerate(self.Particles):
            force = np.zeros(2,dtype='float')
            for forceSourceParticle in typeDict[self.ForceFrom[0]].Particles:
                X = forceSourceParticle.X - particle.X
                r = np.linalg.norm(X)
                force += X/(r**3+0.001)
            self.forceVector[i,:] = force
            particle.force = force


    def calculateParticlePosition(self, mySolver):
        for i,particle in enumerate(self.Particles):
            mySolver.SolveX(particle, self.coeff)

