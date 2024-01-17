with open("priklady.txt","r") as sub:
    vyhovujuce = []
    for line in sub:
        priklad = ""
        for i in line.strip():
            if i != " " and i != "=":
                priklad += i
        if "+" in priklad:
            if int(priklad.split("+")[0]) + int(priklad.split("+")[1]) <= 100:
                vyhovujuce.append(line.strip())
        elif "-" in priklad:
            if int(priklad.split("-")[0]) - int(priklad.split("-")[1]) >= 0:
                vyhovujuce.append(line.strip())

with open("priklady.txt","w") as sub:
    for priklad in vyhovujuce:
        print(priklad,file=sub)
