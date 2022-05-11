x = int(input(''))
y = int(input(''))

if x < y:
    soma = 0
    for r in range(x, y + 1):
        if r % 13 != 0:
            soma = soma + r
    print(soma)

elif y < x:
    soma = 0
    for r in range(y, x + 1):
        if r % 13 != 0:
            soma = soma + r
    print(soma)