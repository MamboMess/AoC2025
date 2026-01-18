
file = open("day4_input.txt","r")

f=file.read()
f = f.split("\n")

def inrange(item):
    x,y = item
    if x < maxx and x>=0 and y >= 0 and y < maxy:
        return True
    else:
        return False

def getadj(item):
    x,y= item
    adj = [(x+1,y), (x-1,y), (x, y+1), (x, y-1), (x+1,y+1), (x+1,y-1), (x-1,y+1), (x-1,y-1)]  
    adj = filter(inrange,adj)
    return adj

def canaccess(item):
    adj = getadj(item)
    spots = []
    for x,y in adj:
        i = grid[y][x]
        spots.append(i)
    if spots.count('@') < 4:
        return True
    else:
        return False

def removepaper(grid):
   gridnew = []
   removed = 0
   for y,r in enumerate(grid):
      gridnew.append([])
      #print(r)
      for x,c in enumerate(r):
         if c == "@":
           item = (x,y)
           k = canaccess(item)
           if k:
             gridnew[y].append("x")
             removed += 1
           else:
             gridnew[y].append(c)
         else:
            gridnew[y].append(c)
   return (removed,gridnew)
                   

grid = [list(i) for i in f]

maxx = len(grid[0])
maxy = len(grid)
rounds = []

removed, grid = removepaper(grid)
rounds.append(removed)
while removed > 0:
   removed, grid = removepaper(grid)
   rounds.append(removed)


print("pt1:",rounds[0])
print("pt2:",sum(rounds))

file.close()