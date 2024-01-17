def preklop(matica):
    nova = []
    for c in range(len(matica[0])):
        new_row = []
        for row in matica:
            new_row.append(row[c])
        nova.append(new_row)
    print(nova)
            
#zisti dlzky
def zisti_dlzky(tab):
    dlzka = len(tab[0])
    for row in tab:
        if len(row) != dlzka:
            return False
    return True



#Funkcia dopln(tab) doplní do vstupnej tabuľky do každého riadka minimálny počet None tak, aby mali všetky riadky rovnakú dĺžku.
def dopln(tab):
    dlzka = 0
    for row in tab:
        if len(row) > dlzka:
            dlzka = len(row)
    for row in tab:
        if len(row) < dlzka:
            kolko = dlzka-len(row)
            row.extend([None]*kolko)
    print(tab)


#Funkcia zisti(tab1, tab2) zistí, či majú dve vstupné tabuľky úplne rovnaké rozmery, t. j. majú rovnaký počet rovnakodlhých riadkov.

tab1 = [[5, 6], [1, 2, 3], [4]]
tab2 = [[0, 0], [0, 0, 0], [0]]
def zisti(tab1, tab2):
    for i in range(len(tab1)):
        if len(tab1[i]) != len(tab2[i]):
            return False
    return True

print(zisti(tab1,tab2))

