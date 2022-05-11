lista = input('').split(' ')
lista2 = input('').split(' ')

codigo1 = int(lista[0])
peça1 = int(lista[1])
valor11 = float(lista[2])

codigo2 = int(lista2[0])
peça2 = int(lista2[1])
valor2 = float(lista2[2])

pagar = (peça1 * valor11) + (peça2 * valor2)

print('VALOR A PAGAR: R$ {:.2f}'.format(pagar))