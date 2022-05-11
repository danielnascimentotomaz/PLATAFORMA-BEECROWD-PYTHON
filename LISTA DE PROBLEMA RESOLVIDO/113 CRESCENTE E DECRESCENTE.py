while True:
    valor = input('').split()
    x = int(valor[0])
    y = int(valor[1])
    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
    elif x == y:
        break
