alcool = 0
gasolina = 0
diesel = 0

while True:
    d = int(input(''))
    if d == 1:
        alcool = alcool + 1
    elif d == 2:
        gasolina = gasolina + 1
    elif d == 3:
        diesel = diesel + 1

    elif d == 4:
        break

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))