import numpy as np
import matplotlib.pyplot as plt
from Patient import Patient, Therapy
from Encoder import BigVectEncoder



patient = Patient()
therapy = Therapy()
BigVect = BigVectEncoder(patient, therapy)

print("Hello")