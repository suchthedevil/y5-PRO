import random
zoz = []
volne = list(range(10,100))
for i in range(20):
    c = random.choice(volne)
    volne.remove(c)
    zoz.append(c)
zoz.sort()
print(zoz)

def hladaj(cislo,zoznam):
    najdene = False
    z, zi = zoznam[0], 0
    k, ki = zoznam[len(zoznam)-1], len(zoznam)-1
    while not najdene:
        s, si = (z+k)//2, (zi+ki)//2
        locator = ["  "]*len(zoznam)
        print(" ".join([str(x) for x in zoznam]))
        locator[zi] = " z"
        locator[ki] = " k"
        locator[si] = " s"
        print(" ".join(locator))
        if s == cislo:
            najdene = True
        elif s > cislo:
            k = s+1
            ki = si+1
        elif s < cislo:
            z = s-1
            zi = si-1
    print(cislo)

hladaj(random.choice(zoz),zoz)



            
