import random
"""
with open("CVP/tabulka.txt","w") as sub:
    out = "  "
    abeceda = []
    for i in range(26):
        out += chr(i+65)
        out += " "
        abeceda.append(chr(i+65))
    print(out,file=sub)

    abeceda_zaloha = abeceda[:]
    random.shuffle(abeceda)
    for i in range(26):
        print(abeceda_zaloha[i],end=" ",file=sub)
        abeceda = abeceda[1:] + [abeceda[0]]
        print(" ".join(abeceda),file=sub)
"""
def sifruj(slovo,heslo):
    with open("CVP/tabulka.txt","r") as sub:
        tab = []
        for i, line in enumerate(sub):
            if i > 0:
                r = line.split()
                tab.append(r)
            else:
                abeceda = line.split()
        #first letter in each line is key
        slovo = slovo.upper()
        heslo = heslo.upper()
        out = ""
        for c,letter in enumerate(slovo):
            if letter in abeceda:
                i = ord(letter)-ord("A")
                ih = ord(heslo[c%len(heslo)])-ord("A")
                out += tab[ih][i+1]
            else:
                out += letter
        return out
    
def desifruj(sifrovane,heslo):
    with open("CVP/tabulka.txt","r") as sub:
        tab = []
        for i, line in enumerate(sub):
            if i > 0:
                r = line.split()
                tab.append(r)
            else:
                abeceda = line.split()
        sifrovane = sifrovane.upper()
        heslo = heslo.upper()
        out = ""
        for c,letter in enumerate(sifrovane):
            if letter in abeceda:
                row = ord(heslo[c%len(heslo)])-ord("A")
                col = tab[row][1:].index(letter)
                out += abeceda[col]
            else:
                out += letter
        return out

print(desifruj(sifruj("Ja, cteny host! Tomas, LAMLECH.","prditko"),"prditko"))

