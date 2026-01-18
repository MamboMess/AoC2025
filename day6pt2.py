import numpy

file = open("day6_input.txt","r")
f=file.read()

lines = f.split("\n")

input = [[] for i in lines[0]]
lines = [list(i) for i in lines]

arr = numpy.array(lines[:-1])
arr=arr.transpose()
newlist = list(arr.tolist())

ops = [i for i in lines[-1] if i != " "]
#print(ops)

nums = []
for i in newlist:
   i = "".join(i)
   i = i.lstrip()
   i = i.rstrip()
   #print(i)
   nums.append(i)

vals = []
numa = "_".join(nums)
numa = numa.split("__")
#print(numa)
nums = []
for n in numa:
    nums.append(n.split("_"))
    
#nums = [int(i) for i in nums if i != ""]
#print(len(nums), len(op))
#chunk= int(len(nums)/len(ops))
#print(chunk)
#chunks = [nums[n*chunk:(n*chunk)+chunk] for n,i in enumerate(ops)]

def mult(nums):
    total = 1
    for i in nums:
        total = total * int(i)
    return total

def add(nums):
    total = 0
    for i in nums:
        total = total + int(i)
    return total
 
vals = []        
for n, c in enumerate(nums):
    if ops[n] == "*":
        vals.append(mult(c))
    else:
        vals.append(add(c))
        
        
print(sum(vals))
#6491000938
#11494432585168


       
"""vals = []    
for i in input:
    o = i[-1]
    nums= [int(n) for n in i[:-1]]
    
"""        
#6378679666679

   
        
#print(sum(vals))
#print(lines)
#print(input)
file.close()