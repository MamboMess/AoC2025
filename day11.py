
file = open("day11_practice.txt","r")

f=file.read()

f = f.split('\n')
dick = {}
for i in f:
    a, b= i.split(": ")
    b = b.split(" ")
    dick[a] = b

x = "you"
end = "out"

#print(dick[x])

visited = []
seen = [x]
paths = 0
while len(seen) > 0:
    x = seen.pop()
    nexts = dick[x]
    if nexts[0] == "out":
        paths += 1
    else:
      seen.extend(nexts)
      visited.append(x)
     
print(paths)

file.close()