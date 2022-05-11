valor = (float(input()))

n100 = valor // 100
a = valor - (100 * n100)

n50 = a // 50
b = a - (50 * n50)

n20 = b // 20
c = b - (20 * n20)

n10 = c // 10
d = c - (10 * n10)

n5 = d // 5
e = d - (5 * n5)

n2 = e // 2
f = e - (2 * n2)

# MOEDA

m1 = f // 1
g = (f - (m1 * 1))
m1 = float('{:.2f}'.format(m1)) # formatacão do input (casas descimais)
g = float('{:.2f}'.format(g))

m50 = g // 0.50
h = g - (0.50 * m50)
m50 = float('{:.2f}'.format(m50))#
h = float('{:.2f}'.format(h))

m25 = h // 0.25
i = h - (0.25 * m25)
m25 = float('{:.2f}'.format(m25))
i = float('{:.2f}'.format(i))

m10 = i // 0.10
j = i - (0.10 * m10)
m10 = float('{:.2f}'.format(m10))
j = float('{:.2f}'.format(j))

m5 = j // 0.05
k = j - (0.05 * m5)
m5 = float('{:.2f}'.format(m5))
k = float('{:.2f}'.format(k))

m01 = k * 100
m01 = float('{:.2f}'.format(m01))

print('NOTAS:')

print('{} nota(s) de R$ 100.00'.format(int(n100)))
print('{} nota(s) de R$ 50.00'.format(int(n50)))
print('{} nota(s) de R$ 20.00'.format(int(n20)))
print('{} nota(s) de R$ 10.00'.format(int(n10)))
print('{} nota(s) de R$ 5.00'.format(int(n5)))
print('{} nota(s) de R$ 2.00'.format(int(n2)))

print('MOEDAS:')

print('{} moeda(s) de R$ 1.00'.format(int(m1)))
print('{} moeda(s) de R$ 0.50'.format(int(m50)))
print('{} moeda(s) de R$ 0.25'.format(int(m25)))
print('{} moeda(s) de R$ 0.10'.format(int(m10)))
print('{} moeda(s) de R$ 0.05'.format(int(m5)))
print('{} moeda(s) de R$ 0.01'.format(int(m01)))
