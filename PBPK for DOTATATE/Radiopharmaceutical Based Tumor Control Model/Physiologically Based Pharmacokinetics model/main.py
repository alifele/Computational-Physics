import numpy as np
import matplotlib.pyplot as plt
from Patient import Patient, Therapy
from Encoder import Encoder
from Solver import Solver






patient = Patient()
therapy = Therapy()
encoder = Encoder(patient, therapy)
solver = Solver(encoder)
solver.solve()


print("Hello")