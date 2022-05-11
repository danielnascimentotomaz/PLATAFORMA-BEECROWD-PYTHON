while True:
    x = int(input())

    if x == 0:
        break

    elif x % 2 == 0:
        soma = 0
        for r in range(x, x + 9):
            if r % 2 == 0:
                soma = soma + r
        print(soma)


    elif x % 2 == 1:
        soma1 = 0
        for s in range(x, x + 10):
            if s % 2 == 0:
                soma1 = soma1 + s
        print(soma1)

