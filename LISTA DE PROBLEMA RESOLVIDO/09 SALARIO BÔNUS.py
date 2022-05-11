nome = str(input(''))
salario = round(float(input('')), 2)
vendas = round(float(input('')), 2)

comisão = (vendas * 15) / 100
total = comisão + salario

print('TOTAL = R$ {:.2f}'.format(total))