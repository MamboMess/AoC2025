
file = open("day3_input.txt","r")
f=file.read()
banks = f.split("\n")

def findbatt(row, batt,digits):
    last,idx = batt[-1]
    end = digits - len(batt) -1
    nextpart = ""
    if end == 0:
        nextpart = row[idx+1:]
    else:
        nextpart = row[idx+1:-end]
    n = max(nextpart)
    idx2 = nextpart.index(n) + 1 + idx
    return (n,idx2)

def getoutput(digits):
    output = []
    for row in banks:
      batt = []
      n1 = max(row[:len(row)-digits+1])
      idx = row.index(n1)
      batt.append((n1,idx))
      while len(batt) < digits:
         n2= findbatt(row,batt,digits)  
         batt.append(n2) 
      jolts = [i[0] for i in batt]
      jolts = "".join(jolts)
      output.append(int(jolts))
    return sum(output)  
    

print("part1: ", getoutput(2))
print("part2: ", getoutput(12))
file.close()