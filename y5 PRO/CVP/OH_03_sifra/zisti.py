with open("CVP/OH_03_sifra/text.txt", "r", encoding="utf8") as sub:
    zeny = 0
    muzi = 0
    for line in sub:
        if "ová" in line:
            zeny += 0.5
    print(zeny)
