
import random
def nahodny_zoznam(n, vyber):
    novy = []
    for i in range(n):
        novy.append(random.choice(vyber))
    return novy

#22
def uprac(zoznam):
    poradie = [2,0,1]
    pocty = []
    for i in poradie:
        pocty.append(zoznam.count(i))
    zoznam.clear()
    for c,i in enumerate(poradie):
        zoznam.extend([i]*pocty[c])
    return zoznam

#21
def zdvoj(zoznam):
    dlzka = len(zoznam)
    while len(zoznam) < 2*dlzka:
        zoznam.extend(2*[zoznam[0]])
        zoznam.pop(0)
    print(zoznam)

#20
z = [5, 3.14, [1, 2], -4, 'ab']

def krat2(zoz):
    for i in range(len(zoz)):
        zoz[i] *= 2
    return zoz



