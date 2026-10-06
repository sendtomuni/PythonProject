D = dict()

for x in enumerate(range(2)):
    print(x)
    print(x[0], x[1])
    D[x[0]] = x[1]
    print((x[1]+7), x[0])
    D[x[1]+7] = x[0]
    print(D)
    print("===========")
print(D)