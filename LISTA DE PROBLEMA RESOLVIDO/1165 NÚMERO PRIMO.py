"""
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100),
indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro
X (1 < X ≤ 107), que pode ser ou não, um número primo.
"""
N = int(input(""))
c = 0
while c < N:
    X = int(input(""))
    contador = 0
    for i in range(1, (X + 1),1):
        if X % i == 0:
            contador = contador + 1
    print(X,end= " ")

    if contador == 2:
        print("eh primo")
    else:
        print("nao eh primo")
    c = c + 1