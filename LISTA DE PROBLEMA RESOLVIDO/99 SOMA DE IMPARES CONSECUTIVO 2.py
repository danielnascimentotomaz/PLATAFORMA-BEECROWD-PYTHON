N = int(input(''))
dados = []
conjunto = []
for v in range(N):
    z = input().split()

    x = int(z[0])
    dados.append(x)

    y = int(z[1])
    dados.append(y)

    conjunto.append(dados[:])
    dados.clear()

for k in conjunto:
    soma = 0
    if k[0] < k[1]:

        for r in range(k[0] + 1, k[1]):

            if r % 2 == 1:
                soma = soma + r

    elif k[1] < k[0]:
        for n in range(k[1] + 1, k[0]):
            if n % 2 == 1:
                soma = soma + n

    print('{}'.format(soma))
