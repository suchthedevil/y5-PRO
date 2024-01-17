def len_parne(zoz):
    novy = []
    for i in zoz:
        if i%2 == 0:
            novy.append(i)
    return novy

print(len_parne([2, 5, 7, 10, 13]))


