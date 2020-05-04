import numpy as np
data = [1, 2, 3, 4, 5, 6]
a = np.array(data).reshape(3, 2)
b = np.append(a, 7)
print(data)
print(a)
print(a.size)
print(b)
print(b.size)