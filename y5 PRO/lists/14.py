#multiplying matrices

a = [[1,2,3],
     [4,5,6],]
b = [[7,8],
     [9,10],
     [11,12]]

result = []
for i in range(len(a)):
    row = []
    for j in range(len(a)):
        dot_sum = 0
        for k in range(len(a[0])):
            dot_p = a[i][k]*b[k][j]
            dot_sum += dot_p
        row.append(dot_sum)
    result.append(row)
print(result)
