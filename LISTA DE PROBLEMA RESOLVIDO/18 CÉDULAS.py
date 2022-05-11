"""n = int(input(''))
print(n)

# total nota de 100
n100 = n // 100  # divisao inteira
r = n % 100  # resto divisao
print('{} nota(s) de R$ 100,00'.format(n100))

# total nota de 50
n50 = r // 50
r1 = r % 50
print('{} nota(s) de R$ 50,00'.format(n50))

# total de nota 20
n20 = r1 // 20
r2 = r1 % 20
print('{} nota(s) de R$ 20,00'.format(n20))

# total de nota 10
n10 = r2 // 10
r3 = r2 % 10
print('{} nota(s) de R$ 10,00'.format(n10))

# total de nota 5
n5 = r3 // 5
r4 = r3 % 5

print('{} nota(s) de R$ 5,00'.format(n5))

n2 = r4 // 2
r5 = r4 % 2
print('{} nota(s) de R$ 2,00'.format(n2))

n1 = r5 // 1
print('{} nota(s) de R$ 1,00'.format(n1))"""

valor = int(input(''))
print(valor)
cout = 0
cout1 = 0
cout2 = 0
cout3 = 0
cout4 = 0
cout5 = 0
cout6 = 0

for c in range(1, valor + 1):
    if c % 100 == 0:
        cout = cout + 1
print('{} nota(s) de R$ 100,00'.format(cout))

total = valor - cout * 100
for c in range(1, total + 1):
    if c % 50 == 0:
        cout1 = cout1 + 1
print('{} nota(s) de R$ 50,00'.format(cout1))

total2 = total - cout1 * 50
for c in range(1, total2 + 1):
    if c % 20 == 0:
        cout2 = cout2 + 1
print('{} nota(s) de R$ 20,00'.format(cout2))


total3 = total2 - cout2 * 20
for c in range(1, total3 + 1):
    if c % 10 == 0:
        cout3 = cout3 + 1
print('{} nota(s) de R$ 10,00'.format(cout3))


total4 = total3 - cout3 * 10
for c in range(1, total4 + 1):
    if c % 5 == 0:
        cout4 = cout4 + 1
print('{} nota(s) de R$ 5,00'.format(cout4))


total5 = total4 - cout4 * 5
for c in range(1, total5 + 1):
    if c % 2 == 0:
        cout5 = cout5 + 1
print('{} nota(s) de R$ 2,00'.format(cout5))


total6 = total5 - 2 * cout5
for c in range(1, total6 + 1):
    if c % 1 == 0:
        cout6 = cout6 + 1
print('{} nota(s) de R$ 1,00'.format(cout6))
