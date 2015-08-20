from genetics import reproduce
from genetics import mutate
from random import randint
popsize = 40
variation = [4,14]  
die = 0.40 
kill_limit = die*popsize
maxi = 0
generations = 1
population = []
fitness = []