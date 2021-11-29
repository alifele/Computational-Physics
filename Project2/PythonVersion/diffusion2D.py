import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import inv
from scipy.sparse import spdiags
import matplotlib
from matplotlib.animation import FuncAnimation


class Diffusion2D:
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
        self.psi = np.zeros((self.M, self.M))
        self.psiData = np.zeros((self.M,self.M,self.N))
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
            self.psi = np.exp(-(((self.X - x0)/deltax)**2+((self.Y - y0)/deltay)**2))

        self.psi[0,:] = 0
        self.psi[-1,:] = 0
        self.psi[:,0] = 0
        self.psi[:,-1] = 0

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
        #self.create_abcd()
        for t in range(self.N):
            self.psiData[:,:,t] = self.psi
            self.psi = self.A.dot(self.psi.dot(self.A.transpose()))

    def createDeltaANDTilda(self):
        upDiag = np.ones(self.M) * (1)
        Diag = np.ones(self.M) * (-2)
        lowDiag = np.ones(self.M) * (1)
        upDiag[1] = 0
        lowDiag[-2] = 0
        Diag[0] = 1
        Diag[-1] = 1
        self.Delta = spdiags([lowDiag, Diag, upDiag], [-1, 0, 1], self.M, self.M)
        self.mat = self.Delta.toarray()

        self.D = np.eye(self.M) + self.R/2 * self.Delta.toarray()
        self.Dtilda = np.eye(self.M) - self.R/2 * self.Delta.toarray()
        self.A = (np.linalg.inv(self.Dtilda)).dot(self.D)




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
    idtype = 1
    vtype = 0
    vpar = [0.25,0.85,-2500]
    idpar = [0.5,0.5,0.075,0.075,0,0]
    #idpar = [2,3]
    tmax = 0.05
    level = 8
    lamda = 1

    system = Diffusion2D(tmax, level, lamda, idtype, idpar, vtype, vpar)
    system.Solve()
    results = system.Returns()
    psire = results['psire']
    psiim = results['psiim']
    psi = results['psimod']

    from matplotlib.animation import FuncAnimation

    fig = plt.figure()
    ax = plt.axes()
    im = plt.imshow(psi[:, :,0], interpolation='none')


    # initialization function: plot the background of each frame
    def init():
        im.set_array(psi[:, :, 0])
        return [im]


    # animation function.  This is called sequentially
    def animate(i):
        im.set_array(psi[:, :, i])
        ax.set_title("frame: {}".format(i))
        return [im]


    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=system.N, interval=50, blit=True)

    plt.colorbar()
    print("hello")

    # plt.style.use('seaborn-pastel')
    # fig = plt.figure()
    # ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
    # line, = ax.plot([], [], lw=3)
    #
    #
    # def init():
    #     line.set_data([], [])
    #     ax.set_xlim([0, 1])
    #     ax.set_ylim([-1, 1])
    #     return line,
    #
    #
    # def animate(i):
    #     ydata = psire[:,100, i]
    #     xdata = np.linspace(0, 1, ydata.shape[0])
    #     line.set_data(xdata, ydata)
    #     ax.set_title("frame: {}".format(i))
    #     return line,
    #
    #
    # anim = FuncAnimation(fig, animate, init_func=init,
    #                      frames=system.N, interval=2, blit=True)
    # plt.show()
    #
    # print("hello")




