count = 0
for x in range(1, 6):
    y = int(input(''))
    if y % 2 == 0:
        count = count + 1

print('{} valores pares'.format(count))