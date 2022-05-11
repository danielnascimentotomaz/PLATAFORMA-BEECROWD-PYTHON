valor = input().split()
a = int(valor[0])
b = int(valor[1])
if a == 0 and b == 0:
    print('Nao sao Multiplos')

elif a % b == 0 or b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')