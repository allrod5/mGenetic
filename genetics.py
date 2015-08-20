def reproduce(geneA, geneB):

	# Choose a random point to make the crossover process
	crosspoint = randint(0,len(geneA))

	# First Child : geneA then geneB
    # child1 = geneA[0:len(geneA)/2]
	child1 = geneA[0:crosspoint]
	
	for i in geneB:
		if i not in child1:
			child1.append(i)

	if randint(0,100) > 20:
		child1 = mutate(child1)
	
	# Second Child : geneB then geneA
	# child2 = geneB[0:len(geneB)/2]
	child2 = geneB[crosspoint:len(geneB) - 1]

	for i in geneA:
		if i not in child2:
			child2.append(i)
	if randint(0,100) > 20:
		child2 = mutate(child2)
	
	return child1, child2

def mutate(gene):
	a = randint(0,len(gene)-1)
	b = randint(0,len(gene)-1)
	# swap
	c = gene[a]
	gene[a] = gene[b]
	gene[b] = c
	return gene
