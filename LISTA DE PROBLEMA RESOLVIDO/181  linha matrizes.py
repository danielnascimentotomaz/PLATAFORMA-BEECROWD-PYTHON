x = int(input())
T = str(input('')).upper()
y = x
m = T

matriz = []
for l in range(0, 12):
    lista = []
    for c in range(0, 12):
        x = float(input(''))
        lista.append(x)

    matriz.append(lista[:])


soma = 0
for z in range(0, 12):
    k = matriz[y][z]
    soma = soma + k


if m == 'S':
    print('{:.1f}'.format(soma))

elif m == 'M':
    print('{:.1f}'.format(soma/12))