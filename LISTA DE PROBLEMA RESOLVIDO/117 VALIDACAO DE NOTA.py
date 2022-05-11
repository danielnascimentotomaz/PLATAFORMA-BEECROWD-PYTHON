lista = []

while True:
    nota = float(input(''))
    if 0 <= nota <= 10:
        lista.append(nota)

    else:
        print('nota invalida')
    if len(lista) == 2:
        break
soma = 0
for y in lista:
    soma = soma + y

media = soma / 2

print('media = {:.2f}'.format(media))