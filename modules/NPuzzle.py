import global_settings as this
from random import shuffle
import math
import copy

def solvable():
	if len(this.list_a) == 0:
		return False

	summation = 0
	for i in range(len(this.list_a)):
		for j in range(i, len(this.list_a)):
			if(this.list_a[j] != 0 and this.list_a[j]<this.list_a[i]):
				summation += 1
	if summation % 2 == 0:
		return True
	else:
		return False

def populate():
	this.dimensions = int(input("Board size: "))
	this.population = []
	this.fitness = []

	#this.block_size = math.ceil(math.log2(this.dimensions*this.dimensions))
	while not solvable():
		this.list_a = []
		for i in range(this.dimensions*this.dimensions):
			this.list_a.append(i)
		shuffle(this.list_a)

		'''for i in range(len(this.list_b)):
			tmp = [int(x) for x in bin(this.list_b[i])[2:]]
			while len(tmp)!=this.block_size:
				tmp.insert(0,0)
			this.list_a += tmp

		array = []
		for i in range(0, len(this.list_a), this.block_size):
			s = ''
			for j in range(0, this.block_size):
				s += str(this.list_a[i+j])
			array.append(int(s, 2))'''

	this.block_size = 2
	for i in range(this.popsize):
		this.population.append([])
		for j in range(this.dimensions*this.dimensions*this.dimensions):
			tmp = [int(x) for x in bin(this.randint(0,3))[2:]]
			while len(tmp)!=this.block_size:
				tmp.insert(0,0)
			this.population[i] += tmp
		this.fitness.append(check(this.population[i]))



def check(array):
	game = copy.deepcopy(this.list_a)
	for bit in array:
		for i in range(len(game)):
			if game[i] == 0:
				break

		if i==0 or i==this.dimensions-1 or i==len(game)-1 or i==len(game)-this.dimensions:
			mod = 2
		elif 0 < i < this.dimensions-1 or len(game)-this.dimensions < i < len(game)-1 \
			or i%this.dimensions==0 or i%this.dimensions==this.dimensions-1:
			mod = 3
		else:
			mod = 4

		moves = []
		if i%this.dimensions!=0:
			moves.append(i-1)
		if i > this.dimensions:
			moves.append(i-this.dimensions)
		if i%this.dimensions!=this.dimensions-1:
			moves.append(i+1)
		if i <= len(game)-this.dimensions:
			moves.append(i+this.dimensions)

		game[i], game[moves[bit%mod]] = game[moves[bit%mod]], game[i]

	for i in range(len(game)):
		if i%this.dimensions == 0:
			print()
		print(game[i], end='')


	mDistance = 0
	for i in range(len(game)):
		if(game[i]):
			mDistance += abs((i)%this.dimensions-(game[i]-1)%this.dimensions)
			mDistance += abs((i)//this.dimensions-(game[i]-1)//this.dimensions)
	print()
	print(2*this.dimensions*this.dimensions*this.dimensions-mDistance)
	print("\n")
	return 2*this.dimensions*this.dimensions*this.dimensions-mDistance

def stopCriteria():
	this.maxi ==  2*this.dimensions*this.dimensions*this.dimensions
	'''for i in range(1, len(array)):
		if array[i] >= array[i-1]:
			return False
	return True'''
