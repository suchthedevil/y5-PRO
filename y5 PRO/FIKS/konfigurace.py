def perms(n):
    for i in range(2**n):
        s = bin(i)[2:]
        s = "0" * (n-len(s)) + s
        yield s

with open("kolo2txt.txt","r") as sub:
    m,n = map(int,sub.readline().split())
    permutacie = list(perms(m))
    lines = []
    number_solutions = 0
    solutions = ""
    for c,line in enumerate(sub):
            scripts = n*[False]
            line = [int(x) for x in line.strip() if x != " "]
            affects_number = line[0]
            lines.append(line[1:])
    for permutation in permutacie:
        scripts = n*[False]
        for c,switch in enumerate(permutation):
            if switch == "1":
                for i in lines[c]:
                    scripts[int(i-1)] = not scripts[int(i-1)]
        if False not in scripts:
             number_solutions += 1
             solutions += f"{permutation}\n"
    print(number_solutions)
    print(solutions)

#storenut susedov kazdeho cisla, a potom aj pocet susedov, zistime tak ake cisla su na sebe zavisle 
