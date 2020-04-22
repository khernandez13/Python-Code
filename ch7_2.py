# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    count = count + 1
    num = (line[20:])
    numb = float(num)
    tot = tot + numb
    av = tot/count


print('Average spam confidence:',av)
