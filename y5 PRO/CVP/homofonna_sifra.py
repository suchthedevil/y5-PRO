import random

#vytvorenie kluca homofonnej sifry, kazde pismeno je sifrovane ako dvojcislie, ale jedno pismeno moze byt zasifrovane ako viacero dvojcisli
"""
key = []
used = []
cisla = list(range(0,100))
for i in range(ord("A"),ord("Z")+1):
    key.append([chr(i)])
    while len(key[i-65])-1 < 2:
        num = random.randrange(0,100)
        if num not in used:
            used.append(num)
            if len(str(num)) == 1:
                key[i-65].append(f"0{num}")
            else:
                key[i-65].append(str(num))

ostavaju = [str(x) for x in cisla if x not in used]
indexy = list(range(0,26))
for i in range(0,26):
    if ostavaju == []:
        break
    pridat = []
    for j in range(random.randrange(0,8)):
        if ostavaju == [] or indexy == []:
            break
        cis = random.choice(ostavaju)
        ostavaju.pop(ostavaju.index(cis))
        pridat.append(cis)
    ktore = random.choice(indexy)
    indexy.pop(indexy.index(ktore))
    key[ktore].extend(pridat)
print(key)

with open("CVP/sifra_kluc.txt", "w") as sub:
    for i in range(len(key)):
        out = ""
        for j in key[i]:
            out += f"{j} "
        print(out, file=sub)

"""
def sifruj(text):
    zoz = []
    with open("CVP/sifra_kluc.txt", "r") as sub:
        for line in sub:
            zoz.append(line.strip().split())
    print(zoz)
    out = ""
    for pismeno in text:
        if "A" <= pismeno.upper() <= "Z":
            for i in range(len(zoz)):
                if pismeno.upper() in zoz[i]:
                    out += zoz[i][random.randrange(1,len(zoz[i])-1)]
        else:
            out += pismeno
    print(out)

sifruj("JOzEF mAK")
