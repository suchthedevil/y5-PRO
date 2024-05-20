def nsd(a,b):
    a_store = a
    b_store = b
    if a > b:
        a = b_store
        b = a_store
    delitel = 1
    for i in range(1,a+1):
        if a%i == 0 and b%i == 0:
            delitel = i
    return delitel

with open("y5 PRO/CVP/zlomky.txt","r") as f:
    for line in f:
        menovatele, citatele, men_unique = [],[],[]
        vysledne = 0
        vysledky = []
        zlomky = line.split()
        zlomky.remove("=")
        while "+" in zlomky:
            zlomky.remove("+")
        for zlomok in zlomky:
            citatel, menovatel = zlomok.split("/")
            menovatele.append(int(menovatel))
            citatele.append(int(citatel))
            if menovatel not in men_unique:
                men_unique.append(int(menovatel))
        common = 1
        for n in men_unique:
            common *= n
        for i,citatel in enumerate(citatele):
            nasobok = common//menovatele[i]
            vysledne += nasobok*citatel
        najv = nsd(vysledne,common)
        vysledne = vysledne//najv
        common = common//najv
        if common == 1:
            zlomok  = f"{vysledne}"
        else:
            zlomok = f"{vysledne}/{common}"
        print(f"{line.rstrip()} {zlomok}")


