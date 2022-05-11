total = int(input(''))

horas = total // 3600   # DIVISÃO INTEIRA
resto1 = total % 3600   # RESTO


minutos = resto1 // 60  # DIVISÃO INTEIRA
resto2 = resto1 % 60  # RESTO

segundos = resto2

print('{}:{}:{}'.format(horas, minutos, resto2))
