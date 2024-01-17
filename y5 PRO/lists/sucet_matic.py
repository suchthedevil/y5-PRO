a = [[5, 6], [1, 2, 3], [4]]
b = [[-1, -3], [-2, 0, 1], [2]]

def sucet_matic(tab1,tab2):
    sucet = []
    for i in range(len(a)):
        s = []
        for j in range(len(a[i])):
            s.append(a[i][j] + b[i][j])
        sucet.append(s)
    print(sucet)

def citaj(meno_suboru):
    with open(meno_suboru,"r",encoding="utf8") as f:
        tab = []
        for line in f:
            tab.append([int(x) for x in line.strip().split()])
    print(tab)

citaj('lists/tab.txt')


