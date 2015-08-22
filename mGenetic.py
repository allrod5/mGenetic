import sys
import getopt
import importlib
import global_settings as this
import time

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

	#importlib.Finder.find_module(module_name)
	#check = importlib.import_module("./modules/%s" % module_name)
	#check = getattr(__import__(module_name, fromlist=['check']), 'check')
	try:
		check = getattr(__import__("modules.%s" % module_name, fromlist=['check']), 'check')
		populate = getattr(__import__("modules.%s" % module_name, fromlist=['populate']), 'populate')
		stopCriteria = getattr(__import__("modules.%s" % module_name, fromlist=['stopCriteria']), 'stopCriteria')
	except ImportError:
		print("Specified module not found. Make sure it is under modules directory.")

	

	this.popsize = int(input("Population size: "))
	this.die = float(input("Death rate: "))
	this.kill_limit = this.die*this.popsize


	#f = open('mGenetic-'+module_name+'_'+str(this.popsize)+'-'+str(this.die)+'-8.csv', 'a')

	start = time.perf_counter()
	populate()

	# Generations loop
	while not stopCriteria():

		#print("Starting gene pool:")
		#printpop(population, fitness)

		# Picks top genes to be parents, kills rest
		killed = 0
		# Starting at the lowest fitness up to kill limit
		x = 0
		while killed < this.kill_limit:
			for i in range(0,this.popsize):
				try:
					if this.fitness[i] == x:
						this.population.pop(i)
						this.fitness.pop(i)
						killed += 1
					if killed == this.kill_limit:
						break
				except:
					break
			x += 1

		#print("Survial of fittest", killed, "killed off (Removed from gene pool)")
		#printpop(population, fitness)

		children = 0
		cpop = len(this.population)-1
		while children < killed:
			offspring = this.reproduce(this.population[this.randint(0,cpop)],this.population[this.randint(0,cpop)])
			for child in offspring:
				this.population.append(child)
				this.fitness.append(check(child))
			children += 2

		#print("Reproduced", children, "children (Added to gene pool)")

		# adds one to the generations
		this.generations += 1

		# Looks for highest fitness in the group and checks if any achieved goal
		this.maxi = 0
		for i in range(0,this.popsize):
			if this.fitness[i] > this.maxi:
				this.maxi = this.fitness[i]
				if stopCriteria():
					array = []
					for j in range(0, len(this.population[i]), this.block_size):
						s = ''
						for k in range(0, this.block_size):
							s += str(this.population[i][j+k])
						array.append(int(s, 2)+1)
					print(array)
					break

		#print("Fittest so far", maxi)
		# printpop(population, fitness)
		# input()
	end = time.perf_counter()
	elapsed = end - start

	#f.write(str(elapsed)+','+str(this.generations)+'\n')
	print("Took", this.generations, "generations")

if __name__ == "__main__":
	main(sys.argv[1:])
