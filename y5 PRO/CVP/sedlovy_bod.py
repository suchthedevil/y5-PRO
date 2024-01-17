m = [[12,6,31,16,18],
     [13,10,18,32,6],
     [32,21,40,22,26],
     [8,13,24,41,19]]

for i in range(len(m)):
    minimum = min(m[i])
    col_index = m[i].index(min(m[i]))
    col = []
    for j in range(len(m)):
        col.append(m[j][col_index])
    maximum = max(col)
    if minimum == maximum:
        print(f"Sedlovy bod je: {maximum}, suradnice: [{i+1},{col_index+1}]")
        exit()
    elif i == len(m)-1:
        print("Nema sedlovy bod")

    

