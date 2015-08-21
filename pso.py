from itertools import product

#inertial coefficient 
w = 0.5

#learning rates
c1, c2 = 2.0

#initial values of velocity, position and stuff
v[0][0] = 1.0
p[0][0] = 1.0
g[0][0] = 1.0
x[0][0] = 1.0

#number of particles
n = 10

#dimensions
d = 1

def sigmoid(t):
	return 1 / (1 + exp(-t))

def pso():
	for i, j in product(range(1, n + 1), range(1, d + 1)):
		rand1 = randint(1,100) / 100.0
		rand2 = randint(1,100) / 100.0
		v[i][j] = w * v[i][j] + c1 * rand1 * (p[i][j] - x[i][j]) + c2 * rand2 * (glob[j] - x[i][j])

