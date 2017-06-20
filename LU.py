import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0., 5., 5.], [2., 9., 0.], [6., 8., 8.]])

def id(n):
	return np.diag([1.] * n)

size, _ = X.shape

# Initialize 
E1 = id(size)
E2 = id(size)
E3 = id(size)
E4 = id(size)
E5 = id(size)
E6 = id(size)
E7 = id(size)
E8 = id(size)

# Set values
E1[2, 1] = -3.
E2[2, 0] = 3.8
E3[2, 2] = 1.0 / 27.0
E4[0, 2] = -5.
E5[0, 0] = .2
E6[1, 0] = -9. 
E7[1, 1] = .5

# Permutation
E8[1, :] = [1, 0, 0]
E8[0, :] = [0, 1, 0]

E = [E1, E2, E3, E4, E5, E6, E7, E8]

print(X)
print()

for M in E:
	X = np.matmul(M, X)

print(str(X) + "\n")

prod = id(size)
for M in reversed(E):
	prod = np.matmul(M, prod)	

print(prod)
