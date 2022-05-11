while True:
    try:

        lista = []
        Expressao = input('')
        for x in Expressao:
            if x == '(':
                lista.append('(')
            elif x == ')':
                if len(lista) > 0:
                    lista.remove('(')
                else:
                    lista.append(')')
                    break

        if len(lista) == 0:
                print('correct')
        else:
                print('incorrect')

    except EOFError:
        break