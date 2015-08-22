from genetics import reproduce
from genetics import mutate
from random import randint
from random import uniform

popsize = 40 # population size
variation = [4,14]  # vector to pick a number to make mutations in NQueens module
die = 0.40  # death rate
kill_limit = die*popsize  # number of individuals to die from the population
maxi = 0  # maximum fitness
generations = 1 # number of current generations
population = [] # the population
fitness = [] # fitness of population individuals
dimensions = 1 # board size / hypercube dimension
block_size = 1 # number of bits to represent an item in an individual's solution

int_a = 0
int_b = 0
int_c = 0
int_d = 0
int_e = 0
int_f = 0
int_g = 0
int_h = 0
int_i = 0
int_j = 0

float_a = 0.0
float_b = 0.0
float_c = 0.0
float_d = 0.0
float_e = 0.0
float_f = 0.0
float_g = 0.0
float_h = 0.0
float_i = 0.0
float_j = 0.0

string_a = 0
string_b = 0
string_c = 0
string_d = 0
string_e = 0
string_f = 0
string_g = 0
string_h = 0
string_i = 0
string_j = 0

list_a = []
list_b = []
list_c = []
list_d = []
list_e = []
list_f = []
list_g = []
list_h = []
list_i = []
list_j = []