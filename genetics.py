import global_settings as this
from random import randint

def reproduce(geneA, geneB):

	# Choose a random point to make the crossover process
	crosspoint = randint(1,len(geneA)-1)

	# First Child : geneA then geneB
	child1 = geneA[:crosspoint]

	for i in geneB[crosspoint:]:
		child1.append(i)

	if randint(0,100) > 20:
		child1 = mutate(child1)
	
	# Second Child : geneB then geneA
	child2 = geneB[:crosspoint]

	for i in geneA[crosspoint:]:
		child2.append(i)

	if randint(0,100) > 20:
		child2 = mutate(child2)
	
	return child1, child2

def mutate(gene):
	#print(len(gene))
	a = randint(0,len(gene)-1-this.block_size)
	b = randint(0,len(gene)-1-this.block_size)
	# swap
	c = gene[a:a+this.block_size]
	gene[a:a+this.block_size] = gene[b:b+this.block_size]
	gene[b:b+this.block_size] = c
	return gene
