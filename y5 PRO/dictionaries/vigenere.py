f = open("y5 PRO/dictionaries/text.txt", encoding="utf-8")
obs = f.read()
f.close()

def decode(text,key):
    slov = {}
    with open("y5 PRO/dictionaries/tabulka.txt", encoding="utf8") as table:
        letters = table.readline().strip().split()
        for line in table:
            slov[line[0]] = line[1:].rstrip().split()
    decoded = ""
    i = 0
    for l in text:
        if "A" <= l <= "Z":
            ind = slov.get(key[i%len(key)]).index(l)
            decoded += letters[ind]
            i += 1
        else:
            decoded += l
    print(decoded)

decode(obs, "COVID")
