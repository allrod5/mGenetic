from random import randint

def populate(popsize, variation, mutate, gene_length=8):
	population = []
	fitness = []
	for i in range(0,popsize):
		population.append([1,2,3,4,5,6,7,8])
		a = 0
		while a < randint(variation[0],variation[1]):
			a += 1
			population[i] = mutate(population[i])
		fitness.append(check(population[i]))
	return population, fitness

def check(array):
	board=[1,2,3,4,5,6,7,8]

	collisions = 0
	
	for i in range(1,len(array)+1):
		if i not in array:
			print("DUPLICATE NUMBER ERROR - KILLING GENE")
			return 0

	for i in range(0, len(array)):
		col = 0
		for j in range(0, len(array)):
			if i != j:
				if abs(board[i]-board[j]) == abs(array[j]-array[i]):
					col = 1
		if col == 1:
			collisions += 1

	#print("OK")
	# return fitness
	return len(array)-collisions