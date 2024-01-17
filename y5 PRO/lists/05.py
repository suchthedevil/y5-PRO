def zisti(zoznam):
    novy = []
    for i in zoznam:
        if type(i) == int and i%7 == 0:
            novy.append(i)
    print(novy)

zisti([4, 7.0, 14.25, '7', 0, 14])

