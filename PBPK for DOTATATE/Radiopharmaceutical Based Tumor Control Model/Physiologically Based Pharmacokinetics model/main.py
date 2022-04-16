import numpy as np
import matplotlib.pyplot as plt
from Patient import Patient, Therapy
from Encoder import BigVectEncoder



patient = Patient()
therapy = Therapy()
bigVectEncoder = BigVectEncoder(patient, therapy)

print("Hello")