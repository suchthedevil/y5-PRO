
a = [[1,2,3],
     [4,5,6]]

b = [[7,8],
     [9,10],
     [11,12]]

v = []

for i in range(len(a)):
    riadok = []
    for k in range(len(b[0])):
        suc = 0
        for j in range(len(a[0])):
            suc += a[i][j]*b[j][k]
        riadok.append(suc)
    v.append(riadok)
print(v)
