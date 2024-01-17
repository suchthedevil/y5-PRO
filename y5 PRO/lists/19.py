def do_suboru(meno_suboru, zoznam):
    with open(meno_suboru,"w") as sub:
        for prvok in zoznam:
            if type(prvok) == int:
                print(prvok,file=sub)
            else:
                print(" ".join(list(map(str,prvok))),file=sub)




do_suboru('a.txt', [[100, 200], 300, 400, [500, 600]])