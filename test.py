__author__ = 'penghao'
from numpy import *
import numpy as np

w = np.ones(6)
list = [1,1,2,1,4,1]
indices = [i for i, x in enumerate(w) if x == 1]
w[indices] /= 2
print(w)