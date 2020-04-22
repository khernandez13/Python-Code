name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
hourline= list()
for line in handle:
    if  not line.startswith('From '): continue
    lines = line.split()
    times = lines[5]
    t = times.split(':')
    hours = t[0]
    hourline.append(hours)#This gets the hours into a list

#This gets the hours and count ino a dictionary
for h in hourline:
    counts[h] = counts.get(h,0) + 1
#print(counts)

tmp = list()
#this code will get the keys and values from the dictionary
#and append them to the tmp list and sort them by key
for k,v  in sorted(counts.items()) :
    newt = (k,v)
    tmp.append(newt)
    print(k,v)





#print('Flipped',tmp)
#tmp = sorted(tmp) #this will sort the list from biggest to smallest
#print('Sorted', tmp)

#This code will print the value and the key
#for v,k in tmp:
    #print(k,v)
