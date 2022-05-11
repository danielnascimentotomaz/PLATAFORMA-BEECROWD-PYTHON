valor = input('').split()

a = float(valor[0])
b = float(valor[1])
c = float(valor[2])

delta = b ** 2 - (4 * a * c)

if delta < 0 or a == 0:
    print('Impossivel calcular')

elif delta > 0:
    x = (- b + delta ** (1 / 2)) / (a * 2)
    y = (- b - delta ** (1 / 2)) / (a * 2)
    print('R1 = {:.5f}'.format(x))
    print('R2 = {:.5f}'.format(y))
