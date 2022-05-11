valor = int(input(''))
for x in range(1, valor + 1):
    if x % 2 == 0:
        print('{}^{} = {}'.format(x, 2, x**2))