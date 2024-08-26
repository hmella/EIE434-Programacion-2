import numpy as np
from funciones import *

A = np.array([[1.0, 2.0], [2.0, 1.0]])
B = np.array([1.0], [1.0])
c = matmul(A, B)
print(c)