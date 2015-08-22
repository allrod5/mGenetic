import global_setting as this

def populate():
    this.int_a = int(input("Board size: "))
    this.population = []
    this.fitness = []

    #def make_maze(w = 8, h = 4):
    w = 8
    h = 4
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    nowalls = []
    x = randrange(h)
    y = randrange(w)

    #def walk(x, y):
    vis[x][y] = 1
	d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
	shuffle(d)

    for (xx, yy) in d:
    	if vis[xx][yy]:
            continue

    	nowalls.append((x,y,xx,yy))
    	walk(xx, yy)

    # walk(randrange(h), randrange(w))
    nw = nowalls #?

    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    for (x,y,xx,yy) in nowalls:
    	print(x,y,xx,yy)
    	if xx == x: ver[x][max(y, yy)] = "   "
    	if yy == y: hor[max(x, xx)][y] = "+  "

    for (a, b) in zip(hor, ver):
    	print(''.join(a + ['\n'] + b))

    def posabs(x, y, w):
    	return(x*w+y)

    def posidx(pos, w):
    	return(pos//w, pos%w)

    def nowallsabs(nowallsidx, w = 8):
        return [(posabs(x,y,w), posabs(xx,yy,w)) for (x,y,xx,yy) in nowallsidx]

    # nw = make_maze()
    # draw_maze(nw)
    nwabs = nowallsabs(nw)




def check(array):


def stopCriteria():
    #return current_pos = final_pos
