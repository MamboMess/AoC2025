
file = open("day5_input.txt","r")
f=file.read()

lines = f.split("\n")

idx = lines.index("")
freshids = lines[:idx]
availableids= lines[idx+1:]

freshranges = []
freshlist = []
for i in freshids:
    min,max = i.split("-")
    f = (int(min),int(max))
    freshranges.append(f)

windows = [freshranges[0]]

def first(tup):
    return tup[0]
    
freshranges.sort(key=first)
merged = []

for min,max in freshranges:
    if len(merged) == 0:
        merged.append((min,max))
    else:
        l,r = merged[-1]
        if min > r:
           merged.append((min,max))
        else:
            if max > r:
                 merged[-1] = (l,max)
                            
print("pt2", sum([r-l+1 for l,r in merged]))

file.close()