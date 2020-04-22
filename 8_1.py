fname = input("Enter file name: ")
fh = open(fname)
lst = list()
stuff = list()
lyst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    lst.append(words)
    #print(words)
#put all the words in one list
    for w in words:
        stuff.append(w)

for s in stuff:
    if s not in lyst:
        lyst.append(s)

lyst.sort()
print(lyst)



















#print(stuff)
