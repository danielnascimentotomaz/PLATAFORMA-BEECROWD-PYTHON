z1 = []
x = int(input())

while True:
    z = int(input())
    if z > x:
        z1.append(z)
        break

soma = 0
count = 0
for r in range(x, z1[0] + 1):
    soma = soma + r
    count = count + 1
    if soma > z1[0]:
        break

print(count)



