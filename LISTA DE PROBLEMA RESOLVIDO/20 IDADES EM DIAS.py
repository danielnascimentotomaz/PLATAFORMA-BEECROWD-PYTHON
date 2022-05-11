dias = int(input(''))

ano = dias // 365  # DIISÃO INTEIRA
resto1 = dias % 365  # RESTO

mes = resto1 // 30  # DIISÃO INTEIRA
resto2 = resto1 % 30   # RESTO

dias = resto2

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dias))
