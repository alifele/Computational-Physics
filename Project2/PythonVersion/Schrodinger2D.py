import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import inv
from scipy.sparse import spdiags
import matplotlib
from matplotlib.animation import FuncAnimation


class Schrodinger2D:
    def __init__(self, tmax, level, lamda, idtype, idpar, vtype, vpar):
        self.tmax = tmax
        self.level = level
        self.lamda = lamda
        self.idtype = idtype
        self.idpar = idpar
        self.vtype = vtype
        self.vpar = vpar

        self.discrete_initiate()
        self.evaluate_idtype()
        self.evaluate_vtype()


    def discrete_initiate(self):
        self.dx = 2**(-self.level)
        self.dy = self.dx
        self.dt = self.lamda*self.dx
        self.xList = np.arange(0, 1+self.dx, self.dx)
        self.yList = np.arange(0, 1+self.dy, self.dy)
        self.X,self.Y = np.meshgrid(self.xList, self.yList)
        self.tList = np.arange(0, self.tmax, self.dt)
        self.M = self.xList.shape[0]
        self.N = self.tList.shape[0]
        self.psi = np.zeros((self.M, self.M), dtype='complex')
        self.psiData = np.zeros((self.M,self.M,self.N), dtype='complex')
        self.R = self.dt/self.dx**2

    def evaluate_idtype(self):
        if self.idtype == 0:
            mx = self.idpar[0]
            my = self.idpar[1]
            self.psi = np.sin(mx*np.pi*self.X)*np.sin(my*np.pi*self.Y)

        if self.idtype == 1:
            x0 = self.idpar[0]
            y0 = self.idpar[1]
            deltax = self.idpar[2]
            deltay = self.idpar[3]
            px = self.idpar[4]
            py = self.idpar[5]
            self.psi = np.exp(1j*px*self.X)*np.exp(1j*py*self.Y)*np.exp(-(((self.X - px)/deltax)**2+((self.Y - py)/deltay)**2))

        self.psi[0] = 0
        self.psi[-1] = 0

    def evaluate_vtype(self):
        self.V = np.zeros((self.M, self.M))

        if self.vtype == 1:
            x_min = self.vpar[0]
            x_max = self.vpar[1]
            y_min = self.vpar[2]
            y_max = self.vpar[3]
            Vc = self.vpar[4]
            self.V[(self.X>x_min)*(self.X<x_max)*(self.Y>y_min)*(self.Y<y_max)]=Vc



    def Solve(self):
        self.createDeltaANDTilda()
        self.create_abcd()
        for t in range(self.N):
            self.psiData[:,:,t] = self.psi
            self.psi = self.ab.dot(self.psi.dot(self.cd))

    def createDeltaANDTilda(self):
        upDiag = np.ones(self.M, dtype='complex') * (1)
        Diag = np.ones(self.M, dtype='complex') * (-2)
        lowDiag = np.ones(self.M, dtype='complex') * (1)
        upDiag[1] = 0
        lowDiag[-2] = 0
        Diag[0] = 1
        Diag[-1] = 1
        self.Delta = spdiags([lowDiag, Diag, upDiag], [-1, 0, 1], self.M, self.M)
        self.mat = self.Delta.toarray()

        self.DtildaY = self.Delta - self.dt/self.R * self.V
        self.DtildaX = self.Delta - self.dt/self.R * self.V.T

    def create_abcd(self):
        Mx = np.linalg.inv(1 - 1j*self.R/2 * self.DtildaX)
        M = (1 + 1j*self.R/2 * self.Delta.toarray())
        My = 1 + 1j*self.R/2 * self.DtildaY

        self.ab = (np.linalg.inv(M)).dot(My)
        self.cd = (M.transpose()).dot((np.linalg.inv(Mx)).transpose())





    def createDelta(self):
        upDiag = np.ones(self.M) * (1)
        Diag = np.ones(self.M) * (-2)
        lowDiag = np.ones(self.M) * (1)
        upDiag[1] = 0
        lowDiag[-2] = 0
        Diag[0] = 1
        Diag[-1] = 1
        self.Delta = spdiags([lowDiag, Diag, upDiag], [-1, 0, 1], self.M, self.M)
        self.mat = self.Delta.toarray()

    def calculate_AB(self):
        ## Ctilda
        Diag = 1j - self.dt/2 * self.V
        Ctilda = spdiags([Diag],[0],self.M,self.M)

        ## C
        Diag = 1j + self.dt/2 * self.V
        C = spdiags([Diag],[0],self.M,self.M)

        self.A = inv(Ctilda + self.R/2 * self.Delta)
        self.B = C - self.R/2 * self.Delta


    def Integral(self):
        pass

    def Returns(self):
        results = dict()
        results["x"] = self.xList
        results["t"] = self.tList
        results["psi"] = self.psi
        results["psire"] = np.real(self.psiData)
        results["psiim"] = np.imag(self.psiData)
        results["psimod"] = np.abs(self.psiData)
        results["v"] = self.V
        results["prob"] = "not ready yet"

        return results



if __name__ == "__main__":
    idtype = 0
    vtype = 0
    vpar = [0.25,0.85,-2500]
    idpar = [2,3]
    tmax = 0.01
    level = 8
    lamda = 0.01

    system = Schrodinger2D(tmax, level, lamda, idtype, idpar, vtype, vpar)
    system.Solve()
    results = system.Returns()
    psire = results['psire']
    psiim = results['psiim']
    psi = results['psimod']

    from matplotlib.animation import FuncAnimation

    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes()
    im = plt.imshow(psi[:, :, 0], interpolation='none')


    # initialization function: plot the background of each frame
    def init():
        im.set_data(psi[:, :, 0])
        return [im]


    # animation function.  This is called sequentially
    def animate(i):
        im.set_array(psi[:, :, i])
        return [im]


    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=system.N, interval=50, blit=True)

    plt.colorbar()
    # anim.save('diff.gif', writer='imagemagick')

    print("hello")




