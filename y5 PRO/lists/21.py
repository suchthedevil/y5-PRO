def zdvoj(zoznam):
    for i in range(0,2*(len(zoznam)),2):
        zoznam.insert(i,zoznam[i])
    print(zoznam)


zdvoj([1, 'Python', 2, 'Java', 3, 'C#'])
