from sys import exit
from sketch import *
from RealWorld import *
from SimWorld import *
from Screen import *
from Solver import *
from Main import *
from Core import *
from Star import *

core = Core()
star = Star(core)

typesList = {'core': core,
             'star': star}

ScreenParams = {'width': 800,
                'height': 600,
                'background': (15, 50, 70)}


RealWorldParameters = {'t0': 0,
                       'tmax': 1500,  # years
                       'dt': 1,  # years
                       'l': [6, 7, 8]}

SimWorldParameters = {'TimeRatio': 1,
                      'MassRatio': 1,
                      'LengthRatio': 1}

myRealWorld = RealWorld(RealWorldParameters)
mySimWorld = SimWorld(SimWorldParameters, RealWorldParameters)
myScreen = Screen(ScreenParams)
mySolver = Solver(mySimWorld.params)

myMain = Main(myRealWorld, mySimWorld, myScreen, mySolver, typesList)
myMain.run()
