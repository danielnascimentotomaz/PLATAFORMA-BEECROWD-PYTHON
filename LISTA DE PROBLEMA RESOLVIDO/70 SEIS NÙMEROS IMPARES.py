x = int(input(''))

if x % 2 == 1:
    for g in range(x, x + 11):
        if g % 2 == 1:
            print(g)
else:
    for g in range(x, x + 13):
        if g % 2 == 1:
            print(g)
