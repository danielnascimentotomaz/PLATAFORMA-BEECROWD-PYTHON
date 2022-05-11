n = int(input(''))
cout = 0
cout1 = 0
for x in range(n):
    valor = int(input(''))
    if 10 <= valor <= 20:
        cout = cout + 1
    else:
        cout1 = cout1 + 1

print('{} in'.format(cout))
print('{} out'.format(cout1))
