x = int(input(''))
y = int(input(''))

soma = 0
if y < x:
    for g in range(y + 1, x):
        if g % 2 == 1:
            soma = soma + g

else:
    for z in range(x + 1, y):
        if z % 2 == 1:
            soma = soma + z

print(soma)
