N = int(input(''))
dados = []
conjunto = []
total = 0
coelho = 0
ratos = 0
sapos = 0
for x in range(N):
    cobaia = input().split()

    valor = int(cobaia[0])
    dados.append(valor)

    animal = str(cobaia[1]).upper().strip()[0]
    dados.append(animal)

    conjunto.append(dados[:])
    dados.clear()

for i in conjunto:
    if i[0]:
        total = total + i[0]
for t in conjunto:

    if t[1] == 'C':
        coelho = coelho + t[0]

    elif t[1] == 'R':
        ratos = ratos + t[0]

    elif t[1] == 'S':
        sapos = sapos + t[0]

t1 = total

m1 = (100 * coelho) / t1
m2 = (100 * ratos) / t1
m3 = (100 * sapos) / t1

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelho))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format(m1))
print('Percentual de ratos: {:.2f} %'.format(m2))
print('Percentual de sapos: {:.2f} %'.format(m3))