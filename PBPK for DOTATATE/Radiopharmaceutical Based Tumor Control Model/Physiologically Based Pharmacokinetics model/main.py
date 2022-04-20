import numpy as np
import matplotlib.pyplot as plt
from Patient import Patient, Therapy
from Encoder import Encoder



patient = Patient()
therapy = Therapy()
encoder = Encoder(patient, therapy)


print("Hello")