N = []
cont = 0
while cont < 20:
    cont = cont + 1
    a = int(input())
    N.append(a)

N.reverse()

for i, y in enumerate(N):
    print('N[{}] = {}'.format(i, y))
