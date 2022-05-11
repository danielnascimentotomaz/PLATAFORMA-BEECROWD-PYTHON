dados = [[], []]


N = int(input())
for N in range(1, N + 1):
    x = int(input())
    if x % 2 == 0:
        dados[0].append(x)
    else:
        dados[1].append(x)


dados[0].sort()
dados[1].sort(reverse=True)

for t in dados[0]:
    print(t)
for f in dados[1]:
    print(f)