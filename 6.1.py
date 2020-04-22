fruit = 'banana'
length = len(fruit)
last = fruit[length -1]
index = 0
while index  <= length:
    letter = fruit[index-1]
    print(letter)
    if index < 0 :
        break

print('Done')
