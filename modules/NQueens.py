import global_settings as this

def populate():
	this.int_a = int(input("Board size: "))
	this.population = []
	this.fitness = []
	for i in range(0,this.popsize):
		gene = []
		for j in range(this.int_a):
			gene.append(j+1)
		this.population.append(gene)
		a = 0
		while a < this.randint(this.variation[0],this.variation[1]):
			a += 1
			this.population[i] = this.mutate(this.population[i])
		this.fitness.append(check(this.population[i]))
	return

def check(array):
	collisions = 0
	
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
	return this.maxi == this.int_a