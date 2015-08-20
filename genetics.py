def reproduce(geneA, geneB):
	# First Child : geneA then geneB
	child1 = geneA[0:len(geneA)/2]
	for i in geneB:
		if i not in child1:
			child.append(i)

	if randint(0,100) > 20:
		child = mutate(child)
	
	# Second Child : geneB then geneA
	child2 = geneB[0:len(geneB)/2]
	for i in geneA:
		if i not in child:
			child.append(i)
	if randint(0,100) > 20:
		child = mutate(child)
	
	return child1, child2

def mutate(gene):
	a = randint(0,len(gene)-1)
	b = randint(0,len(gene)-1)
	# swap
	c = gene[a]
	gene[a] = gene[b]
	gene[b] = c
	return gene
