diai = input('').split()
diai = int(diai[1])
hora = input('').split()
hi = int(hora[0])
mi = int(hora[2])
si = int(hora[4])


diaf = input('').split()
diaf = int(diaf[1])
hora = input('').split()
hf = int(hora[0])
mf = int(hora[2])
sf = int(hora[4])

tempoi = (hi * 3600) + (mi * 60) + si + (86400 * diai)
tempof = (hf * 3600) + (mi * 60) + si + (86400 * diaf)

if tempoi < tempof:
    tempo = tempof - tempoi
    

    print('{} dia(s)'.format())
    print('{} minuto(s)'.format())
    print('{} segundo(s)'.format())