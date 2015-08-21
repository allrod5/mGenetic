import sys
import getopt
import importlib
import global_settings as this
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

def sigmoid(t):
	return 1 / (1 + exp(-t))

def pso():
	for i, j in product(range(1, n + 1), range(1, d + 1)):
		rand1 = randint(1,100) / 100.0
		rand2 = randint(1,100) / 100.0
		v[i][j] = w * v[i][j] + c1 * rand1 * (p[i][j] - x[i][j]) + c2 * rand2 * (g[j] - x[i][j])

def main(argv):
	module_name = ''

	try:
		opts, args = getopt.getopt(argv,"hm:",["module="])
	except getopt.GetoptError:
		print('Error: incorrect parameters.\n Usage: mGenetic.py -m <module_name>\n')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('Usage: mGenetic.py -m <module_name>\n')
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




