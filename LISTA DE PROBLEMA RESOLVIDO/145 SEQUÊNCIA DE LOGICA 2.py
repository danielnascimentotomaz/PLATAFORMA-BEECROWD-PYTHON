z = input('').split()
x = int(z[0])
y = int(z[1])

a = 1
b = 2
c = 3
for t in range(1, 4 ):
    print('{} {} {}'.format(a, b, c))
    a = a + x
    b = b + x
    c = c + x