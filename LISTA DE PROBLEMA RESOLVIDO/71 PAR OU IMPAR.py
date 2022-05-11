N = int(input())
lista = []
for x in range(N):
    X = int(input())
    lista.append(X)

for y in lista:
    if y > 0:
        if y % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    elif y < 0:
        if y % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')

    elif y == 0:
        print('NULL')