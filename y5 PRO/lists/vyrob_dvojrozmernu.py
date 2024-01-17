def vyrob(pr, ps, hodnoty):
    tab = []
    c = 0
    for i in range(pr):
        riadok = []
        for j in range(ps):
            if c > len(hodnoty)-1:
                riadok.append(hodnoty[c%len(hodnoty)])
            else:
                riadok.append(hodnoty[c])
            c += 1
        tab.append(riadok)
    print(tab)

vyrob(3, 3, list(range(1, 20, 2)))

