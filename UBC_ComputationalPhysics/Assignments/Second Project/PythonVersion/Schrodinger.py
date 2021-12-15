import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import inv
from scipy.sparse import spdiags
import matplotlib
from matplotlib.animation import FuncAnimation


class Schrodinger:
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
        self.dt = self.lamda*self.dx
        self.xList = np.arange(0, 1+self.dx, self.dx)
        self.tList = np.arange(0, self.tmax, self.dt)
        self.M = self.xList.shape[0]
        self.N = self.tList.shape[0]
        self.psi = np.zeros(self.xList.shape[0], dtype='complex')
        self.psiData = np.zeros((self.N,self.M), dtype='complex')
        self.R = self.dt/self.dx**2

    def evaluate_idtype(self):
        if self.idtype == 0:
            m = self.idpar[0]
            self.psi = np.sin(m*np.pi*self.xList)

        if self.idtype == 1:
            x0 = self.idpar[0]
            delta = self.idpar[1]
            p = self.idpar[2]
            self.psi = np.exp(1j*p*self.xList) * np.exp(-((self.xList-x0)/delta)**2)

        self.psi[0] = 0
        self.psi[-1] = 0

    def evaluate_vtype(self):
        self.V = np.zeros(self.xList.shape[0])

        if self.vtype == 1:
            x_min = self.vpar[0]
            x_max = self.vpar[1]
            Vc = self.vpar[2]
            self.V[(self.xList>x_min)*(self.xList<x_max)]=Vc



    def Solve(self):
        self.createDelta()
        self.calculate_AB()
        for t in range(self.N):
            self.psiData[t,:] = self.psi
            self.psi = self.A.dot(self.B.dot(self.psi))

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
        psi = self.psiData
        psi = np.abs(psi)**2
        integ_ = 0.5*(psi + np.roll(psi, -1, axis=1))*self.dx
        self.integ = integ_[:,:-1]
        self.calculateP()

    def Returns(self):
        results = dict()
        results["x"] = self.xList
        results["t"] = self.tList
        results["psi"] = self.psi
        results["psire"] = np.real(self.psiData)
        results["psiim"] = np.imag(self.psiData)
        results["psimod"] = np.abs(self.psiData)
        results["v"] = self.V
        self.Integral()
        results["prob"] = self.P

        return results

    def calculateP(self):
        self.P = np.zeros(self.integ.shape)
        summed = np.zeros(self.integ.shape[0])
        for i in range(self.integ.shape[1]):
            summed += self.integ[:,i]
            self.P[:,i] = summed



if __name__ == "__main__":
    idtype = 1
    vtype = 0
    vpar = [0.25,0.75,-2500]
    idpar = [0.5,0.075,0.0]
    tmax = 0.8
    level = 8
    lamda = 0.01

    system = Schrodinger(tmax, level, lamda, idtype, idpar, vtype, vpar)
    system.Solve()
    results = system.Returns()
    psire = results['psire']
    psiim = results['psiim']
    psi = results['psimod']
    integ = results['prob']

    plt.style.use('seaborn-pastel')
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
    line, = ax.plot([], [], lw=3)


    def init():
        line.set_data([], [])
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 0.25])
        return line,


    def animate(i):
        ydata = integ[i, :]
        xdata = np.linspace(0, 1, ydata.shape[0])
        line.set_data(xdata, ydata)
        ax.set_title("frame: {}".format(i))
        return line,


    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=system.N, interval=1, blit=True)
    plt.show()

    print("hello")




