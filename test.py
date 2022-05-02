import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model
import matplotlib.animation as animation
A = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]).T
A_square = np.array([A[:,0] ** 2]).T
ones = np.ones((A.shape[0],1),dtype = np.int8)

A = np.concatenate((ones,A,A_square),axis=1)
print(A)