import numpy as np
import math

def in_unit_cirle(x, y):
	return (x**2 + y**2) <= 1.0

n_points = [10**y for y in range(10)]
for n in n_points:
	sample = np.random.rand(n, 2)
	results = np.zeros(n)
	for i in range(n):
		results[i] = in_unit_cirle(sample[i, 0], sample[i, 1])
	print(math.atan(1) - np.mean(results))

