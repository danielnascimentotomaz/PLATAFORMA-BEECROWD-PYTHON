n = input().split()
a = float(n[0])
b = float(n[1])
c = float(n[2])
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
medio = a
if maior == a and menor == b or menor == a and maior == b:
    medio = c
elif maior == a and menor == c or menor == a and maior == c:
    medio = b



if maior >= medio + menor:
    print('NAO FORMA TRIANGULO')
else:
    if maior ** 2 == medio ** 2 + menor ** 2:
        print('TRIANGULO RETANGULO')
    elif maior ** 2 > medio ** 2 + menor ** 2:
        print('TRIANGULO OBTUSANGULO')
    elif maior ** 2 < medio ** 2 + menor ** 2:
        print('TRIANGULO ACUTANGULO')
    if maior == medio == menor:
        print('TRIANGULO EQUILATERO')
    elif maior == medio or maior == menor or medio == menor:
        print('TRIANGULO ISOSCELES')