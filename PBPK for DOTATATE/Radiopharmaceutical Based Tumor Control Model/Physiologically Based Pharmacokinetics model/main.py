import numpy as np
import matplotlib.pyplot as plt
from Patient import Patient
from Therapy import Therapy
from Encoder import Encoder
from Solver import Solver
from DataProcessing import DataProcessing

## TODO: I need to add Albumin compartment to the model. Also I should evaluate its effect in the dynamics




patient = Patient()
therapy = Therapy()
encoder = Encoder(patient, therapy)
solver = Solver(encoder)
solver.solve()
dataProcessing = DataProcessing(patient, therapy, encoder, solver)
dataProcessing.plotter()

print("Hello")
