from more_itertools import batched

file = open("day2_input.txt","r")

f=file.read()
ids = f.split(",")

invalids = []
invalidpt2 = []

def allsame(items):
     return all(x == items[0] for x in items)

for i in ids:
    i = i.split("-")
    a = int(i[0])
    b = int(i[1])
    ls = list(range(a,b+1))
    
    for x in ls:
        invalid = False
        s = str(x)
        half = int(len(s)/2)
        if s[:half] == s[half:]:
            invalid = True
            invalids.append(x)
            invalidpt2.append(x)
        grouprange = list(range(half))
        for n in grouprange:
            if invalid:
              break
            groups = batched(s, n+1)
            groups = ["".join(j) for j in list(groups)]
            if allsame(groups):
              #print("invalid")
              invalid = True
              invalidpt2.append(x)
              break
            
            
        
        
print("part1:", sum(invalids))
#p1 64215794229
print("part2:", sum(invalidpt2))
#p2 85513235135



file.close()