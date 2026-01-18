import math

f = open("day1_input.txt","r")

file = f.read()
file = file.split("\n")


visited = []


def cycle(v, c):
    global visited
    lst = list(range(100))
    #lst.reverse()
    #print(lst)
    ticks = v
    first = True
    idx = c
    last = 0
    #print("starting at:", idx, "going up:",ticks)
    while ticks > 0:
     for n,i in enumerate(lst):
        if first:
            if idx == 99:
                first = False
                ticks = ticks - 1
                last = i 
                visited.append(i)
                print("oops edge case")
            elif idx == 0:
               first = False
               last = i 
               #visited.append(i)
            elif i > idx:
               ticks = ticks - 1
               first = False
               last = i 
               visited.append(i)
               #print("on #:",i, n, "start", idx, "ticks remaining", ticks)
           
        else:
            if ticks > 0:
               ticks = ticks - 1
               last = i
               visited.append(i)
               #print("on #:",last, n, "start", idx, "ticks remaining", ticks)
               
    return last

def revcycle(v, c):
    global visited
    lst = list(range(100))
    lst.reverse()
    #print(lst)
    ticks = v
    first = True
    idx = c
    last = 0
    #print("starting at:", idx, "going down:",ticks)
    while ticks > 0:
     for n,i in enumerate(lst):
        if first and idx != 0:
           if i < idx:
               ticks = ticks - 1
               first = False
               last = i
               visited.append(i)
               #print("on #:",i, n, "start", idx, "ticks remaining", ticks, "z", z)
               
        else:
            if ticks > 0:
               ticks = ticks - 1
               last = i
               visited.append(i)
               #print("on #:",last, "start", idx, "ticks remaining", ticks, "z", z)
               
    return last
    
def turn(dir,val,current):
    if dir == "R":
        x = cycle(val,current)
        return x
    else:
        x = revcycle(val,current)
        return x

#print(file)


current = 50
stops = []

for i in file:
    dir = i[0]
    val = int(i[1:])
    current = turn(dir,val,current)
    stops.append(current)


#print(stops)    
print("part1:",stops.count(0))


print("part2:",visited.count(0))
#not 7420
f.close()