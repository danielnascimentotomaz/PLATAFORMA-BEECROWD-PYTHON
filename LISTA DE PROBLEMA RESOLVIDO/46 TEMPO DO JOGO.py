valor = input("").split()
a = int(valor[0])
b = int(valor[1])

if a > b or a == b:
    x = 24 + (b  - a )
    print('O JOGO DUROU {} HORA(S)'.format(x))

elif a < b:
    x = (b - a)
    print('O JOGO DUROU {} HORA(S)'.format(x))
