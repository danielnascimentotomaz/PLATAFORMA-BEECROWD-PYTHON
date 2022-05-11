cout = 0
soma = 0
for a in range(1, 7):
    x = float(input(''))
    if x > 0:
        cout = cout + 1
        soma = soma + x

media = soma/cout
print('{} valores positivos'.format(cout))
print('{:.1f}'.format(media))