inter = 0
gremio = 0
empates = 0
while True:
    x = input().split()
    i = int(x[0])
    g = int(x[1])

    if i > g:
        inter = inter + 1

    elif g > i:
        gremio = gremio + 1

    elif i == g:
        empates = empates + 1

    print('Novo grenal (1-sim 2-nao)')
    Novogrenal = int(input())
    if Novogrenal == 2:
        break

print('{} grenais'.format(inter + gremio + empates))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empates))


if inter == gremio:
    print('Nao houve vencedor')
elif inter > gremio:
    print('Inter venceu mais')
elif gremio < inter:
    print('Gremio venceu mais')
