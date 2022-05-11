lista = input('').split()

a = round(float(lista[0]), 2)
b = round(float(lista[1]), 2)
c = round(float(lista[2]), 2)

# AREA
triangulo = (a * c)/2
circulo = 3.14159 * c**2
trapezio = ((a + b) * c) / 2
quadrado = b * b
retangulo = a * b

print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))