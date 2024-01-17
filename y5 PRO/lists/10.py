def vyrob2(zoznam):
    kopia = []
    for i in zoznam:
        if type(i) == str:
            kopia.append(i)
    print(kopia)



vyrob2([1, 2.2, ['a', 'b'], 'tri', 4, ''])