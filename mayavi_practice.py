import numpy as np
from numpy import sin, cos, pi, mgrid
import mayavi.mlab as mlb

#
# dphi , dtheta = pi / 250 , pi / 250
# phi = np.arange(0,pi+dphi,0.05)
# theta = np.arange(0,2*pi+dtheta,0.05)
# phi, theta = np.meshgrid(phi, theta)
#
# Y = -sin(theta)**2*cos(theta)*cos(2*phi)
# r = np.abs(Y)
# x = r * sin ( phi ) * cos ( theta ) ; y = r * cos ( phi )
# z = r * sin ( phi ) * sin ( theta )

x = np.arange(-10,10,0.05)
y = np.arange(-10,10,0.05)
z = np.arange(-10,10,0.05)

X,Y,Z = np.meshgrid(x,y,z)

YY= Z/(X**2+Y**2+0.0001)**0.5


s = mlb.mesh(X,Y,)
mlb.show()
