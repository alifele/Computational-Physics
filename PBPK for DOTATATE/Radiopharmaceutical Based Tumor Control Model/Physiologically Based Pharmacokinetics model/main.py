import numpy as np
import matplotlib.pyplot as plt
from Patient import Patient
from Therapy import Therapy

from Patient2 import Patient2
from Therapy2 import Therapy2
from Encoder import Encoder
from Solver import Solver
from AdaptiveSolver import AdaptiveSolver
from StiffSolver import StiffSolver
from MyStiffSolver import MyStiffSolver
from DataProcessing import DataProcessing
import numpy as np

## TODO: I need to add Albumin compartment to the model. Also I should evaluate its effect in the dynamics

# injectionProfileList = ["constantInjection60", "constantInjection120", "constantInjection180", "constantInjection240",
#                         "constantInjection300", "constantInjection360", "bolusInjection", "bolusTrainInjection2",
#                         "bolusTrainInjection3",
#                         "bolusTrainInjection4", "bolusTrainInjection5", "bolusTrainInjection6", "bolusTrainInjection7"]

injectionProfileList = ["bolusInjection"]

for i, profile in enumerate(injectionProfileList):

    patient = Patient()
    therapy = Therapy(i)
    encoder = Encoder(patient, therapy)
    # solver = Solver(encoder)
    # solver = AdaptiveSolver(encoder)
    solver = StiffSolver(encoder)
    # solver = MyStiffSolver(encoder)
    solver.solve()
    DP = DataProcessing(patient, therapy, encoder, solver)
    DP.plotter()
    #np.save("data/"+profile, dataProcessing.results.BigVectList)

print("Hello")
