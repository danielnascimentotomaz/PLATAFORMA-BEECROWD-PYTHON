dados = []
lista = []
while True:
    x = input().split()
    D = int(x[0])
    N = int(x[1])
    if 1 <= D <= 9 and 1 <= N < 10 ** 100:
        dados.append(D)
        dados.append(N)

        lista.append(dados[:])
        dados.clear()

    elif D == 0 and N == 0:
        break

