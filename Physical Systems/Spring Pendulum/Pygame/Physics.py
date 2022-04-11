import numpy as np


class Physics:
    def __init__(self):
        self.t_min = 0
        self.t_max = 50
        self.l = 14
        self.N_t = 2 ** self.l
        self.tList = np.linspace(self.t_min, self.t_max, self.N_t)
        self.dt = self.tList[1] - self.tList[0]

        self.Psi = np.zeros((2, 2, self.N_t))
        self.Psi[0, :, 0] = np.array([3, 1])
        self.Psi[1, :, 0] = np.array([0, 0])

        self.L = 1
        self.M = 0.2
        self.g = 10

    def G(self, t, Psi):
        x = Psi[0, 0]
        x_d = Psi[1, 0]
        theta = Psi[0, 1]
        theta_d = Psi[1, 1]
        g1 = np.array([x_d, theta_d])
        g2 = self.F(t, Psi)

        return np.array([g1, g2])

    def F(self, t, Psi):
        ## Psi[0] --> Phi
        ## Psi[1] --> Phi'
        ## Phi = [x,theta]
        x = Psi[0, 0]
        x_d = Psi[1, 0]
        theta = Psi[0, 1]
        theta_d = Psi[1, 1]
        f1 = (1 + x) * theta_d ** 2 + self.g*np.cos(theta) - x/self.M
        f2 = (1 / (1 + x)) * (-self.g*np.sin(theta) - 2 * x_d * theta_d)

        return np.array([f1, f2])


    def calculate(self):
        for i, t in enumerate(self.tList[:-1]):
            Psi_ = self.Psi[:, :, i]
            f0 = self.G(t, Psi_)
            f1 = self.G(t, Psi_ + f0 / 2 * self.dt)
            f2 = self.G(t, Psi_ + f1 / 2 * self.dt)
            f3 = self.G(t, Psi_ + f2 * self.dt)
            Psi_ = Psi_ + self.dt / 6 * (f0 + 2 * f1 + 2 * f2 + f3)
            self.Psi[:, :, i + 1] = Psi_
