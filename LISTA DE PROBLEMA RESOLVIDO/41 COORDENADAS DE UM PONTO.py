valores = input().split()
x= float(valores[0])
x =float('{:.1f}'.format(x))
y = float(valores[1])
y=float('{:.1f}'.format(y))

if x == 0 and y == 0:
    print('Origem')

elif x != 0 and y == 0:
    print('Eixo X')
elif y != 0 and x == 0:
    print('Eixo Y')

elif x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')

elif x < 0 and y < 0:
    print('Q3')

elif x > 0 and y < 0:
    print('Q4')