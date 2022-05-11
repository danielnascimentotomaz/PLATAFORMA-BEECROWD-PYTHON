x = float(input(''))
x = float('{:.2f}'.format(x))

if 0 <= x <= 2000:
    print('Isento')

elif 2000 < x <= 3000:
    z = x - 2000
    a = (z * 8) / 100
    print('R$ {:.2f}'.format(a))

elif 3000 < x <= 4500:
    z1 = x - 2000
    z2 = z1 - 1000
    a = (1000 * 8) / 100
    b = (z2 * 18) / 100
    y = a + b
    print('R$ {:.2f}'.format(y))
else:
    z = x - 2000
    z1 = z - 2500
    a = (1000 * 8) / 100
    b = (1500 * 18) / 100
    c = (z1 * 28) / 100
    y = a + b + c
    print('R$ {:.2f}'.format(y))





