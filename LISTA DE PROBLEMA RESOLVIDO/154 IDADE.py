lista = []
soma = 0
while True:
    idade = int(input())
    if idade > 0:
        lista.append(idade)
    elif idade < 0:
        break

for x in lista:
    soma = soma + x
media = soma / len(lista)

print('{:.2f}'.format(media))