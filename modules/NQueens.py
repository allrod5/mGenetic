import global_settings as this

def populate():
	this.population = []
	this.fitness = []
	for i in range(0,this.popsize):
		this.population.append([1,2,3,4,5,6,7,8])
		a = 0
		while a < this.randint(this.variation[0],this.variation[1]):
			a += 1
			this.population[i] = this.mutate(this.population[i])
		this.fitness.append(check(this.population[i]))
	return

def check(array):
	board=[1,2,3,4,5,6,7,8]

	collisions = 0
	
	for i in range(1,len(array)+1):
		if i not in array:
			return 0

	for i in range(0, len(array)):
		col = 0
		for j in range(0, len(array)):
			if i != j:
				if abs(board[i]-board[j]) == abs(array[j]-array[i]):
					col = 1
		if col == 1:
			collisions += 1

	# Return fitness score
	return len(array)-collisions

def stopCriteria():
	return this.maxi == 8