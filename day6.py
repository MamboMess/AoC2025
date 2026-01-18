

file = open("day6_input.txt","r")
f=file.read()

lines = f.split("\n")
lines=[i.split(" ") for i in lines]
lines=[[a for a in b if a != ""] for b in lines]
input = [[] for i in lines[0]]
for i in lines:
    for n,x in enumerate(i):
      input[n].append(x)


def mult(nums):
    total = 1
    for i in nums:
        total = total * i
    return total

def add(nums):
    total = 0
    for i in nums:
        total = total + i
    return total
        
vals = []    
for i in input:
    o = i[-1]
    nums= [int(n) for n in i[:-1]]
    if o == "*":
        vals.append(mult(nums))
    else:
        vals.append(add(nums))
        
#6378679666679

   
        
print(sum(vals))
#print(lines)
#print(input)
file.close()