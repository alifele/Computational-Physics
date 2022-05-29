import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-2,2,0.005)
y = np.arange(-2,2,0.005)*1j
X,Y = np.meshgrid(x,y)
C = X+Y
maxiter = 25



def mandel(C,maxiter):
    color = np.zeros(C.shape)

    for i,row in enumerate(C):
        for j,c in enumerate(row):
            z = 0
            n = 0
            while np.absolute(z)<=2 and n<maxiter:
                z = z**2 + c
                n+=1

            color[i,j]=n
    return color


## This function calculates the set much much faster (Because I am using matrix multiplication
## of numpy to calculate the set
def mandelMat(C,maxiter):
    color = np.ones(C.shape)*maxiter
    Z = np.zeros(C.shape)
    for i in range(maxiter):
        Z = np.add(np.multiply(Z,Z) , C)
        absZ = np.absolute(Z)
        color[absZ>=10] = i
        Z[absZ>=10] = float('nan')

    return color

def Julia(Z,maxiter):
    color = np.ones(Z.shape)*maxiter
    C = np.zeros(Z.shape)+(-0.66j)+0.1
    for i in range(maxiter):
        Z = np.add(np.multiply(Z,Z) , C)
        absZ = np.absolute(Z)
        color[absZ>=10] = i
        Z[absZ>=10] = float('nan')

    return color



Z = X+Y ## For generating the Julia set
C = X+Y ## For generating the Mandelbrot fractal


plt.figure()
colorJulia = Julia(Z,maxiter)
colorJulia = (maxiter - colorJulia)
plt.imshow(colorJulia,cmap='turbo')


plt.figure()
colorMandel = mandelMat(C,maxiter)
colorMandel = (maxiter - colorMandel)
plt.imshow(colorMandel, cmap='turbo')
plt.colorbar()

plt.show()



#
# def mandel(C, iteration):
#     Z = np.zeros(C.shape)
#     color = np.zeros(C.shape)
#     for i in range(iteration):
#         Z_new = Z**2 + C
#         color = np.log(np.absolute(Z-Z_new)+0.00001)
#         Z = Z_new;
#         # if (np.absolute(Z) > 1E150).any():
#         #     break
#         Z[np.absolute(Z)>100]=0
#     color
#     return color


