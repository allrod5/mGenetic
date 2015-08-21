import sys
import getopt
import importlib
import global_settings as this
from itertools import product
import copy
from random import uniform

#inertial coefficient 
w = 0.5

#learning rates
c1 = 2.0
c2 = 2.0

#initial values of velocity, position and stuff
v = []
#p[0][0] = 1.0
#g[0][0] = 1.0
#x[0][0] = 1.0
#p = []
#g = []

#p_fitness = []


def sigmoid(t):
	return 1 / (1 + exp(-t))

def pso(p, g, n, d):
	fill_v = False
	if(len(v)==0):
		fill_v = True
	for i, j in product(range(1, n + 1), range(1, d + 1)):
		rand1 = uniform(0.0,1.0)
		rand2 = uniform(0.0,1.0)
		try:
			v[i][j] = w * v[i][j] + c1 * rand1 * (p[i][j] - this.population[i][j]) + c2 * rand2 * (g[j] - this.population[i][j])
		except:
			try:
				v[i]
				v[i].append(w + c1 * rand1 * (p[i][j] - this.population[i][j]) + c2 * rand2 * (g[j] - this.population[i][j]))
			except:
				print(i)
				print(j)
				print(len(p))
				print(len(this.population))
				print(len(g))
				v.append([w + c1 * rand1 * (p[i][j] - this.population[i][j]) + c2 * rand2 * (g[j] - this.population[i][j])])
	return v

def main(argv):
	module_name = ''
	g_fitness = 0
	p = []
	g = []
	p_fitness = []

	try:
		opts, args = getopt.getopt(argv,"hm:",["module="])
	except getopt.GetoptError:
		print('Error: incorrect parameters.\n Usage: pso.py -m <module_name>\n')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('Usage: pso.py -m <module_name>\n')
			sys.exit()
		elif opt in ("-m", "--module"):
			module_name = arg

	try:
		check = getattr(__import__("modules.%s" % module_name, fromlist=['check']), 'check')
		populate = getattr(__import__("modules.%s" % module_name, fromlist=['populate']), 'populate')
		stopCriteria = getattr(__import__("modules.%s" % module_name, fromlist=['stopCriteria']), 'stopCriteria')
	except ImportError:
		print("Specified module not found. Make sure it is under modules directory.")

	this.popsize = int(input("Population size: "))

	

	populate()
	print(len(this.population))
	p = copy.deepcopy(this.population)
	print(len(p))
	p_fitness = copy.deepcopy(this.fitness)

	while not stopCriteria():
		this.maxi = 0
		for i in range(0,this.popsize):
			if this.fitness[i] > p_fitness[i]:
				p[i] = copy.deepcopy(this.population[i])
				p_fitness[i] = this.fitness[i]

			if this.fitness[i] > this.maxi:
				this.maxi = this.fitness[i]
				if this.maxi > g_fitness:
					g_fitness = this.maxi
					g = copy.deepcopy(this.population[i])

				if stopCriteria():
					array = []
					for j in range(0, len(this.population[i]), this.block_size):
						s = ''
						for k in range(0, this.block_size):
							s += str(this.population[i][j+k])
						array.append(int(s, 2)+1)
					print(array)
					break
		v = pso(p, g, this.popsize, this.dimensions)

		for i in range(len(v)):
			for j in range(len(v[i])):
				if uniform(0.0,1.0) < sigmoid(v[i][j]):
					this.population[i][j] = 1
				else:
					this.population[i][j] = 0
			fitness[i] = check(this.population[i])




if __name__ == "__main__":
	main(sys.argv[1:])
