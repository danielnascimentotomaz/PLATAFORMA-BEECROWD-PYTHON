lista1 = [1,2,3,4,5]
lista2 = ['cachorro', 'quente', 'x-salada', 'x-bacom', 'torrada simple', 'refrigerante']
lista3 = [4.00, 4.50, 5.00, 2.00, 1.50]

valor = input('').split()

a = int(valor[0])
b = int(valor[1])

print('Total: R$ {:.2f}'.format(lista3[a -1] * b))