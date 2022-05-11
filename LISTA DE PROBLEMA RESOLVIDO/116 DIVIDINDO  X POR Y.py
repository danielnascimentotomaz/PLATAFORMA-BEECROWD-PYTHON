N = int(input(''))

for z in range(N):
    valores = input().split()
    x = int(valores[0])
    y = int(valores[1])

    if y != 0:
        d = x / y
        print('{:.1f}'.format(d))
    elif y == 0:
        print('divisao impossivel')


