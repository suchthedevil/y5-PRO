def uprac(zoznam):
    sposob = "201"
    dlzka = len(zoznam)
    for a in sposob:
        zoznam.extend([int(a)]*zoznam.count(int(a)))
    zoznam[:] = zoznam[dlzka:]

zoznam = [0, 1, 2, 0, 0, 2]

uprac(zoznam)
print(zoznam)