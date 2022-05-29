import numpy as np



class Balls:
    def  __init__(self, screen, physConf):
        self.screen = screen
        self.physConf = physConf    ## height and width of physics box

        self.N = self.physConf["N"]
        self.R = self.physConf["R"]
        self.Kb = self.physConf["Kb"]
        self.Kw = self.physConf["Kw"]
        self.width = self.physConf["width"]
        self.height = self.physConf["height"]
        # self.pos = np.zeros((3, self.N))
        # self.vel = np.zeros((3,self.N))
        self.Phi = np.ones((6,self.N))
        self.F = np.zeros((3,self.N))

        self.t = 0
        self.m = 1

        self.initiateBalls()



    def initiateBalls(self):

        self.Phi[0,:] = ((np.random.random(self.N)*2)-1)*self.width/2
        self.Phi[1,:] = ((np.random.random(self.N)*2)-1)*self.height/2

        self.Phi[3, :] = ((np.random.random(self.N) * 2) - 1)
        self.Phi[4, :] = ((np.random.random(self.N) * 2) - 1)


    def move(self, dt):
        self.calculateForce()
        f0 = self.G(self.t, self.Phi)
        f1 = self.G(self.t+dt/2, self.Phi+dt/2*f0)
        f2 = self.G(self.t+dt/2, self.Phi+dt/2*f1)
        f3 = self.G(self.t+dt, self.Phi+dt*f2)

        self.Phi += dt/6 * (f0+2*f1+2*f2+f3)

        self.t += dt



    def calculateForce(self):
        ### Ball-Ball interaction
        self.F = np.zeros((3,self.N))

        for i in range(self.N-1):
            force_i = np.zeros((2,1))
            for j in range(i+1, self.N):
                DR = (self.Phi[:2, j] - self.Phi[:2,i]).reshape((2,1))
                DR_norm = np.linalg.norm(DR)
                collisionDetection =  2*self.R - DR_norm
                if collisionDetection > 0:
                    force = -self.Kb*(collisionDetection)*DR/DR_norm
                    force_i += force
                    self.F[:2,j] += -force.reshape((2,))

            self.F[:2,i] += force_i.reshape((2,))


        ### Ball Wall interaction
        # for i in range(self.N):
        #
        #     if self.Phi[0,i]+self.R > self.width/2:
        #         force = -self.Kw*(self.Phi[0,i]+self.R-self.width/2)
        #         self.F[0,i]+=force
        #
        #     if self.Phi[0,i]-self.R < -self.width/2:
        #         force = -self.Kw*(self.Phi[0,i]-self.R+self.width/2)
        #         self.F[0,i]+=force
        #
        #     if self.Phi[1, i] + self.R > self.height / 2:
        #         force = -self.Kw * (self.Phi[1, i] + self.R - self.height / 2)
        #         self.F[1, i] += force
        #
        #     if self.Phi[1, i] - self.R < -self.height / 2:
        #         force = -self.Kw * (self.Phi[1, i] - self.R + self.height / 2)
        #         self.F[1, i] += force



    def G(self, t, Phi):
        results = Phi.copy()
        results[:2,:] = Phi[3:5,:]
        results[3:5,:] = self.F[:2,:]/self.m
        return results



if __name__ == "__main__":
    import matplotlib.pyplot as plt
    physConf = {"width": 100,
                "height": 100,
                "N": 100,
                "R": 3,
                "Kb": 50,
                "Kw": 50}
    balls = Balls("hello", physConf)

    balls.initiateBalls()
    dt = 0.1
    # for i in range(100):
    #     balls.move(dt)


    plt.scatter(balls.Phi[0,:], balls.Phi[1,:]);plt.show()

