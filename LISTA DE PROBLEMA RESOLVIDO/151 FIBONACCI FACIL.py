n = int(input())
i = 0
ii = 1
l = [0, 1]
count = 3
while count <= n:
    iii = i + ii
    l.append(iii)
    i = ii
    ii = iii
    count = count + 1

for b in range(0, n):
    l[b] = str(l[b])

x = ' '.join(l)
print(x)
