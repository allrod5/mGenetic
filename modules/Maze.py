import global_setting as this

# the maze is maked by a depth-first algorithm, so it's always solvable
# at least it's what is visible from the class examples

# our maze is always squared, n x n

def make_maze(n):

    # http://rosettacode.org/wiki/Maze_generation#Python

    vis = [[0] * n + [1] for _ in range(n)] + [[1] * (n + 1)]
    ver = [["|  "] * n + ['|'] for _ in range(n)] + [[]]
    hor = [["+--"] * n + ['+'] for _ in range(n + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(n), randrange(n))
    for (a, b) in zip(hor, ver):
        print(''.join(a + ['\n'] + b))


def populate():
    this.int_a = int(input("Board size: "))
    this.population = []
    this.fitness = []
    this.block_size = 2

    # generate the maze
    make_maze(this.int_a)

    # do the thing
    for i in range(this.popsize):
		this.population[i].append([])
		for j in range(this.dimensions*this.dimensions*this.dimensions):
			tmp = [int(x) for x in bin(randint(0,3))[2:]]
			while len(tmp)!=this.block_size:
				tmp.insert(0,0)
			this.population[i][j] += tmp


def check(array):


def stopCriteria():
    #return current_pos == final_pos
