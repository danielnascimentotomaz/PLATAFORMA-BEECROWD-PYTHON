lista = []
maior = 0
for x in range(1,101):
    valor = int(input(''))
    lista.append(valor)

    if x == 1:
        maior = valor
    else:
        if valor > maior:
            maior = valor
print(maior)

for s , r in enumerate (lista):
    if r == maior:
        print('{}'.format(s + 1))