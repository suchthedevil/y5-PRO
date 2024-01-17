tab = [[1,2,3], [4], [5,6], [7,8,9], [10,11]]

def zoznam_suctov(tab):
    out = []
    for row in tab:
        out.append(sum(row))
    print(out)

def zoznam_suctov2(tab):
    for row in tab:
        row.append(sum(row))
    print(tab)
zoznam_suctov2(tab)
