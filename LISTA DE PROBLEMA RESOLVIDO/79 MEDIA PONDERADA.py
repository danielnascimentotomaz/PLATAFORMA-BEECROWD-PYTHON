dados = []
conjunto = []
N = int(input(''))
for x in range(N):
    y = input().split()
    a = float(y[0])
    dados.append(a)
    b = float(y[1])
    dados.append(b)
    c = float(y[2])
    dados.append(c)
    conjunto.append(dados[:])
    dados.clear()

for i in conjunto:
    p = ((i[0] * 2) + (i[1] * 3) + (i[2] * 5)) / 10
    print('{:.1f}'.format(p))
