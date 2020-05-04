import numpy as np
import math 
p0 = np.array((1, 1))
p1 = np.array((6, 4))
A = p1 - p0
print(A)
dist = math.sqrt(pow(A[0],2) + pow(A[1],2))
print(dist)
a_dist = np.linalg.norm(A)
print(a_dist)