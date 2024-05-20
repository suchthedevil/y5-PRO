with open("y5 PRO/CVP/ziaci.txt","r",encoding="utf8") as sub:
    predmety = sub.readline().rstrip().split()
    mena, priemery, znamky = [], [], []
    for line in sub:
        meno = line[0:line.find(" ",line.find(" ")+1)]
        znamky.append(line[line.find(" ",line.find(" ")+1):].replace(" ","").rstrip())
        mena.append(meno)
        pocet, sucet = 0, 0
        for i in line.replace(" ",""):
            if i in "12345":
                pocet += 1
                sucet += int(i)
        priemery.append(round(sucet/pocet,2))
    najlepsi = 5
    predmet = ""
    for p in range(len(predmety)):
        pocet = 0
        sucet = 0
        for i in range(len(znamky)):
            if znamky[i][p] != "x":
                sucet += int(znamky[i][p])
                pocet += 1
        print(sucet/pocet)
        if sucet/pocet < najlepsi:
            najlepsi = sucet/pocet
            predmet = predmety[p] 
    print(f"Najlepší priemer známok {min(priemery)} má {mena[priemery.index(min(priemery))]}")
    print(f"Najlepšie výsledky boli dosiahnuté v predmete {predmet}")
