import global_settings as this
import math

def populate():
	this.dimensions = int(input("Board size: "))
	this.population = []
	this.fitness = []
	for i in range(0,this.popsize):
		gene = []
		this.block_size = math.ceil(math.log2(this.dimensions))
		for j in range(this.dimensions):
			tmp = [int(x) for x in bin(j)[2:]]
			while len(tmp)!=this.block_size:
				tmp.insert(0,0)
			gene += tmp
		this.population.append(gene)
		a = 0
		while a < this.randint(this.variation[0],this.variation[1]):
			a += 1
			this.population[i] = this.mutate(this.population[i])
		this.fitness.append(check(this.population[i]))

	return

def check(gene):
	collisions = 0
	array = []
	for i in range(0, len(gene), this.block_size):
		s = ''
		for j in range(0, this.block_size):
			s += str(gene[i+j])
		array.append(int(s, 2)+1)

	for i in range(1,len(array)+1):
		if i not in array:
			return 0

	for i in range(0, len(array)):
		col = 0
		for j in range(0, len(array)):
			if i != j:
				if abs(i-j) == abs(array[j]-array[i]):
					col = 1
		if col == 1:
			collisions += 1

	# Return fitness score
	return len(array)-collisions

def stopCriteria():
	return this.maxi == this.dimensions
