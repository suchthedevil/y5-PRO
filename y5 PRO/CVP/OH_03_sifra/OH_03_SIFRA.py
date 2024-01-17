from random import randrange

def sifruj(sifrovat,kluc):
    output_file = open(sifrovat,"a", encoding="utf8")
    zoz = []
    with open(sifrovat, "r", encoding="utf8") as sub:
        text = sub.read()
        with open(kluc, "r") as key:
            for line in key:
                zoz.append(line.strip().split())
    out = ""
    for pismeno in text:
        if "A" <= pismeno.upper() <= "Z":
            for i in range(len(zoz)):
                if f"{pismeno.upper()}:" in zoz[i]:
                    out += zoz[i][randrange(1,len(zoz[i])-1)]
        else:
            out += pismeno
    print(f"\n\n{out}",file=output_file)
    output_file.close()

def desifruj(desifrovat,kluc):
    output_file = open(desifrovat,"a", encoding="utf8")
    zoz = []
    out = ''
    with open(desifrovat, "r", encoding="utf8") as sub:
        sifrovane = sub.read()
        with open(kluc, "r") as key:
            for line in key:
                zoz.append(line.strip().split())
        c = 0
        while c < len(sifrovane):
            if "0" <= sifrovane[c] <= "9":
                current = sifrovane[c] + sifrovane[c+1]
                c += 2
                for j in range(len(zoz)):
                    if current in zoz[j]:
                        out += zoz[j][0][0]
            else:
                out += sifrovane[c]
                c += 1
    print(f"\n\n{out}",file=output_file)
    output_file.close()

sifruj("CVP/OH_03_sifra/sifruj.txt","CVP/OH_03_sifra/homofona.txt")
desifruj("CVP/OH_03_sifra/desifruj.txt","CVP/OH_03_sifra/homofona.txt")
