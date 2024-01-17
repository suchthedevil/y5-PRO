aux = {}
main = {}
m = [[1,2,3],
     [4,5,6],
     [3,2,1]]

for i in range(len(m)):
    for j in range(len(m[0])):
        if i-j in main:
            main[i-j].append(m[i][j])
        else:
            main[i-j] = [m[i][j]]
        if i+j in aux:
            aux[i+j].append(m[i][j])
        else:
            aux[i+j] = [m[i][j]]

for key,field in main.items():
    print(key,field)
print()
for key,field in aux.items():
    print(key,field)

