
file = open("day7_input.txt","r")

f=file.read()
hits = []
def inrange(item):
    x,y = item
    if x < maxx and x>=0 and y >= 0 and y < maxy:
        return True
    else:
        return False


def find(grid, layer):
    loc= []
    for n, i in enumerate(grid[layer]):
        if i == "S" or i == "|":
            loc.append((layer,n))
    return(loc)


def down(grid,coord):
    y,x = coord[0]+1,coord[1]
    if inrange((x,y)):
      if grid[y][x] == ".":
        grid[y][x] = "|"
      elif grid[y][x] == "^":
        hits.append((y,x))
        if inrange((x+1,y)) and grid[y][x+1] != "^":
            grid[y][x+1] = "|"
        if inrange((x-1,y)) and grid[y][x-1] != "^":
            grid[y][x-1] = "|"
    return grid
    
def printgrid(grid):
    for i in grid:
        print("".join(i))


grid = f.split("\n")
grid = [list(i) for i in grid]
#print(grid)
maxx = len(grid[0])
maxy = len(grid)
layer = 0

for n,row in enumerate(grid):
    loc = find(grid,n)
    for i in loc:
        grid = down(grid, i)

print("part1:",len(set(hits)))


file.close()