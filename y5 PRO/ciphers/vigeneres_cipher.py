def sifruj(text, key):
    with open("y5 PRO/ciphers/tabulka.txt") as f:
        dic = {}
        for i, line in enumerate(f):
            if i == 0:
                abc = line.strip().split()
            else:
                dic[line.split()[0]] = line.strip().split()[1:]
    i = 0
    out = ""
    for l in text:
        if 'a' <= l.lower() <= 'z':
            index = abc.index(l.upper())
            new_l = dic[key[i%len(key)].upper()][index]
            i += 1
        else:
            new_l = l
        out += new_l
    print(out)


def desifruj(text,key):
    with open("y5 PRO/ciphers/tabulka.txt") as f:
        dic = {}
        for i, line in enumerate(f):
            if i == 0:
                abc = line.strip().split()
            else:
                dic[line.split()[0]] = line.strip().split()[1:]
    i = 0
    out = ''
    for l in text:
        if l != " ":
            index = dic[key[i%len(key)].upper()].index(l)
            new_l = abc[index]
            i += 1
        else:
            new_l = l
        out += new_l
    print(out)


sifruj('janko a marienka','hrasko')
desifruj('MWZCS O BWWUORWW','hrasko')