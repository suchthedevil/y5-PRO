"""
funkcia posledny_riadok(meno_suboru)
funkcia predposledny_riadok(meno_suboru)
funkcia najdlhsi_riadok(meno_suboru)
"""
"""
def posledny_riadok(meno_suboru):
    with open(meno_suboru,'r', encoding='utf8') as subor:
        for riadok in subor:
            vypis = riadok
    print(vypis)

posledny_riadok('sub.txt')

def predposledny_riadok(meno_suboru):
    zoz = []
    with open(meno_suboru,'r', encoding='utf8') as subor:
        for riadok in subor:
            zoz.append(riadok)
    print(zoz[-2])
predposledny_riadok('novy.txt')
"""
def najdlhsi_riadok(meno_suboru):
    dlzka = 0
    with open(meno_suboru,'r', encoding='utf8') as subor:
        for riadok in subor:
            print(len(riadok))
            if len(riadok) >= dlzka:
                dlzka = len(riadok)
                display = riadok
    print(display)
najdlhsi_riadok("sub.txt")

