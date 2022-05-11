notas = input().split()

a = float(notas[0])
a = float('{:.1f}'.format(a))

b = float(notas[1])
b = float('{:.1f}'.format(b))

c = float(notas[2])
c = float('{:.1f}'.format(c))

d = float(notas[3])
d = float('{:.1f}'.format(d))

peso = ((a * 2) + (b * 3) + (c * 4) + (d * 1))

media = peso / 10

if media >= 7:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')

elif media < 5:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
elif 5 <= media <= 6.9:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    exame = float(input(''))
    print('Nota do exame: {:.1f}'.format(exame))

    total = (media + exame) / 2
    if total >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(total))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(total))
