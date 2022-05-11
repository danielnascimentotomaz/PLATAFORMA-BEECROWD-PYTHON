from math import sqrt
lista1 = input('').split()
lista2 = input('').split()

x1 = float(lista1[0])
y1 = float(lista1[1])

x2 = float(lista2[0])
y2 = float(lista2[1])

valor1 = (x2**2 - 2 * x1 * x2 + x1**2)
valor2 = (y2**2 - 2 * y1 * y2 + y1**2)

distancia = sqrt(valor1 + valor2)

print('{:.4f}'.format(distancia))