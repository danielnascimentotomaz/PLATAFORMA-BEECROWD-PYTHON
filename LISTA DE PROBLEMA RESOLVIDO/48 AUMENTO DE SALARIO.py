valor = float(input(''))
valor = float('{:.2f}'.format(valor))

if 0 <= valor <= 400:
    reajuste = (valor * 15) / 100
    aumento = valor + reajuste
    print('Novo salario: {:.2f}'.format(aumento))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 15 %')

elif 400 < valor <= 800:
    reajuste = (valor * 12) / 100
    aumento = valor + reajuste
    print('Novo salario: {:.2f}'.format(aumento))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 12 %')

elif 800 < valor <= 1200:
    reajuste = (valor * 10) / 100
    aumento = valor + reajuste
    print('Novo salario: {:.2f}'.format(aumento))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 10 %')

elif 1200 < valor <= 2000:
    reajuste = (valor * 7) / 100
    aumento = valor + reajuste
    print('Novo salario: {:.2f}'.format(aumento))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 7 %')
else:
    reajuste = (valor * 4) / 100
    aumento = valor + reajuste
    print('Novo salario: {:.2f}'.format(aumento))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 4 %')