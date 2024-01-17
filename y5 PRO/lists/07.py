def na_parnych(zoznam):
    return [zoznam[i] for i in range(0,len(zoznam),2)]

print(na_parnych(list('programovanie')))

