import numpy as np



class Physics:
    def __init__(self, N):
        self.t_min = 0
        self.t_max = 30
        self.l = 12
        self.N_t = 2 ** self.l
        self.tList = np.linspace(self.t_min, self.t_max, self.N_t)
        self.dt = self.tList[1] - self.tList[0]

        self.N = N

        # self.PhiList = np.zeros((2, self.N, self.N_t))
        # self.PhiList[0, :, 0] = [0, 0, 0, 0, 0, 0]
        # self.PhiList[1, :, 0] = [1, 0, 0, 0, 0, 0]
        self.X = np.zeros(self.N)
        self.X_dot = np.zeros(self.N)
        self.X_dot[0] = 1

        self.Phi = np.array([self.X, self.X_dot])


        self.M = np.zeros((self.N, self.N))

        TheEndsConnectedToWall = 1
        if (TheEndsConnectedToWall):
            a = -2
        else:
            a = -1
        for row in range(self.N):
            if row == 0:
                self.M[row, 0] = a
                self.M[row, 1] = 1
            elif row == self.N - 1:
                self.M[row, -1] = a
                self.M[row, -2] = 1

            else:
                j = row
                self.M[row, j-1] = 1
                self.M[row, j] = -2
                self.M[row, j+1] = 1

        # self.M = np.array([[-1, 1, 0, 0, 0, 0], [1, -2, 1, 0, 0, 0], [0, 1, -2, 1, 0, 0],
        #                    [0, 0, 1, -2, 1, 0], [0, 0, 0, 1, -2, 1], [0, 0, 0, 0, 1, -1]])


    def F(self, Phi, M):
        X = Phi[0]
        F0 = Phi[1]
        F1 = np.matmul(self.M, X)
        return np.array([F0,F1])


    def calculate(self):
        f0 = self.F(self.Phi, self.M)
        f1 = self.F(self.Phi+f0/2*self.dt, self.M)
        f2 = self.F(self.Phi+f1/2*self.dt, self.M)
        f3 = self.F(self.Phi+f2*self.dt, self.M)
        self.Phi = self.Phi+self.dt/6*(f0+2*f1+2*f2+f3)
        return self.Phi


