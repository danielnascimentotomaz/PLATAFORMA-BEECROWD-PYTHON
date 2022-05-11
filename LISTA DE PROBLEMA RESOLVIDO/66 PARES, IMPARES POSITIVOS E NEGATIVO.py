pares = 0
impares = 0
positivos = 0
negativos = 0
for x in range(1, 6):
    y = int(input(''))
    if y % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if y > 0:
        positivos = positivos + 1
    if y < 0:
        negativos = negativos + 1

print('{} valor(es) par(es)'.format(pares))
print('{} valor(es) impar(es)'.format(impares))
print('{} valor(es) positivo(s)'.format(positivos))
print('{} valor(es) negativo(s)'.format(negativos))
