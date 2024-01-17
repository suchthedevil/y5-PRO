def vyrob1(zoznam):
    kopia = []
    for i in zoznam:
        if i%2 == 0:
            kopia.append(i+1)
        else:
            kopia.append(i)
    print(kopia)
        