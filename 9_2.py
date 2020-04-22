name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith('From: ') : continue
    lines = line.split()
    words = lines[1]
    #print(words)
    if words not in counts:
          counts[words] = 1
    else:
          counts[words] = counts[words] +1
#print(counts)

largest = 0
email = None
for k,v in counts.items() :#get key and value
    #print(aa,bb)
    if v > largest :
        largest = v
        email = k

print(email,largest)
