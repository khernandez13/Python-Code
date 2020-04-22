import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_415348.txt"
handle = open(name)
numlist = list()
for line in handle :
    lines = line.rstrip()
    #gets the file split out
#findall to get the numbers
    x = re.findall('[0-9]+',lines)
#tell the code that if there is nothing in the line skip it
    if len(x) == 0 : continue
    #add the numbers to the list
    for nums in x :
       numlist.append(nums)
    #Converts strings to integers in numlist
numlist = [int(nums) for nums in numlist]
print(sum(numlist))
