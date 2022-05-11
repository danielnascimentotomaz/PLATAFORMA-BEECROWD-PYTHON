lista = input('').split()

a = int(lista[0])
b = int(lista[1])
c = int(lista[2])

maior = a

if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c

print('{} eh o maior'.format(maior))



