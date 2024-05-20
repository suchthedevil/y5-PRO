def prvo(cislo):
    for i in range(2,int(cislo**(1/2)+1)):
        if cislo%i == 0:
            return False
    return True

with open("y5 PRO/CVP/cisla.txt","r") as sub:
    for line in sub:
        cislo = int(line.rstrip())
        rozklad = f'{cislo}= '
        zoz = []
        if prvo(cislo):
            print(f"{cislo}= {cislo}*1")
            continue
        while cislo != 1:
            for i in range(2,int(cislo)+1):
                if cislo%i == 0 and prvo(i):
                    zoz.append(i)
                    cislo = cislo//i
        zoz.sort(reverse=True)
        for i in zoz:
            pocet = zoz.count(i)
            if f"{i}" not in rozklad[rozklad.find("="):]:
                if pocet == 1:
                    rozklad += f"{i}*"
                else:
                    rozklad += f"{i}^{pocet}*"
        print(rozklad[0:-1])
        
