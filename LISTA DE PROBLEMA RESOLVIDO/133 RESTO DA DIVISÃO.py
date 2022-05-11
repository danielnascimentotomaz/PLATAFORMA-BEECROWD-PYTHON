x = int(input())
y = int(input())

if x < y:
    for t in range(x + 1, y):
        if t % 5 == 3 or t % 5 == 2:
            print(t)

elif x > y:
    for f in range(y + 1, x):
        if f % 5 == 3 or f % 5 == 2:
            print(f)
