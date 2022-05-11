dados = []
conjunto = []

while True:
    x = input().split()
    N = int(x[0])
    M = int(x[1])
    if N > 0 and M > 0:
        dados.append(N)
        dados.append(M)

        conjunto.append(dados[:])
        dados.clear()

    if N <= 0 or M <= 0:
        break

for i in conjunto:
    if i[0] < i[1]:
        soma = 0
        for t in range(i[0], i[1] + 1):
            soma = soma + t
            print('{}'.format(t), end=' ')
        print('Sum={}'.format(soma))

    elif i[0] > i[1]:
        soma = 0
        for y in range(i[1], i[0] + 1):
            soma = soma + y
            print('{}'.format(y), end=' ')
        print('Sum={}'.format(soma))
