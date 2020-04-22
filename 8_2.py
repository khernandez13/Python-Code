fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
lines = list()
lst=list()
count = 0
for line in fh :
    if not line.startswith('From:') : continue
    line = line.rstrip()
    lines =line.split()
    count = count +1
    email =lines[1]
    print(email)


print("There were", count, "lines in the file with From as the first word")
