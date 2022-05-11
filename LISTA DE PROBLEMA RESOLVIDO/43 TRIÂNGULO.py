x = input().split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    m = a + b + c
    print('Perimetro = {:.1f}'.format(m))

else:
    area = ((a + b) * c) / 2
    print('Area = {:.1f}'.format(area))
