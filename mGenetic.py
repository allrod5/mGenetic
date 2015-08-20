import sys
import getopt
import importlib
from genetics import reproduce
from genetics import mutate

def printpop(population, fitness):
	for i in range(0, len(population)):
		print(population[i], fitness[i])

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

	importlib.Finder.find_module(module_name)
	#check = importlib.import_module("./modules/%s" % module_name)
	check = getattr(__import__(module_name, fromlist=['check']), 'check')

	popsize = 40
	variation = [4,14]  
	die = 0.40 
	kill_limit = die*popsize
	maxi = 0
	generations = 1

	population = []
	fitness = []
	for i in range(0,popsize):
		population.append([1,2,3,4,5,6,7,8])
		a = 0
		while a < randint(variation[0],variation[1]):
			a += 1
			population[i] = mutate(population[i])
		fitness.append(check(population[i]))

	# Generations loop
	while maxi != 8:
		
		#print("Starting gene pool:")
		#printpop(population, fitness)
		
		# Picks top genes to be parents, kills rest
		killed = 0
		# Starting at the lowest fitness up to kill limit
		x = 0
		while killed < kill_limit:
			for i in range(0,popsize):
				try:
					if fitness[i] == x:
						population.pop(i)
						fitness.pop(i)
						killed += 1
					if killed == kill_limit:
						break
				except:
					break
			x += 1
		
		#print("Survial of fittest", killed, "killed off (Removed from gene pool)")
		#printpop(population, fitness)
		
		children = 0
		cpop = len(population)-1
		while children < killed:
			offspring = reproduce(population[randint(0,cpop)],population[randint(0,cpop)])
			for child in offspring:
				population.append(child)
				fitness.append(check(child))
			children += 2 
		
		#print("Reproduced", children, "children (Added to gene pool)")

		# adds one to the generations
		generations += 1

		# Looks for highest fitness in the group and checks if any achieved goal
		maxi = 0
		for i in range(0,popsize):
			if fitness[i] > maxi:
				maxi = fitness[i]
				if maxi == 8:
					print(population[i])
					break

		#print("Fittest so far", maxi)
		# printpop(population, fitness)
		# raw_input()

	print("Took", generations, "generations")

if __name__ == "__main__":
	main(sys.argv[1:])