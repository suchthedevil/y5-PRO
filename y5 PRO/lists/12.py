def gener(a,b,c):
    zoz = [a]
    if abs(c) == c:
        while a < b-c:
            zoz.append(a+c)
            a += c
    else:
        while a > b-c:
            zoz.append(a+c)
            a += c
    print(zoz)

gener(4,18,3)
