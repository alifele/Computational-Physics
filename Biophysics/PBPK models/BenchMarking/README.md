
![enter image description here](https://raw.githubusercontent.com/alifele/Computational-Physics/main/Biophysics/PBPK%20for%20DOTATATE/BenchMarking/diagram.PNG)

Differential Equations:

$$\frac{dA}{dt} = -pA+rB+I_0$$

$$\frac{dB}{dt} = -(r+q)B+pA + sC + I_1$$

$$\frac{dC}{dt} = qB - sC + I_2$$


The variables are summarized in the $\Phi$ vector. So the system of differential equaitons can be written as:

$$F(t,\Phi) = M\Phi + I(t)$$

in which M is the system matrix.

