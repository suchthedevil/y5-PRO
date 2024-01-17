def zo_suboru(meno):
    zoz = []
    with open(meno,"r") as sub:
        for line in sub:
            riadok = line.rstrip()
            if len(line.rstrip().split()) == 1:
                zoz.append(int(riadok))
            else:
                zoz.append(list(map(int,riadok.split())))
    print(zoz)

zo_suboru("lists/a.txt")