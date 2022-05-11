numero = round(float(input('')), 2)
horas = round(float(input('')), 2)
valor = round(float(input('')), 2)

total = horas * valor

print('NUMBER = {:.0f}'.format(numero))
print('SALARY = U$ {:.2f}'.format(total))