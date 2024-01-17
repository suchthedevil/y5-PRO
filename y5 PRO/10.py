"""
def vypis_slova(meno_suboru):
    dni = []
    with open(meno_suboru,'r', encoding="utf8") as subor:
        for line in subor:
            dni.append(line)
        l = 0
        while dni != []:
            l += 1
            for i in range(l%4):
                print(dni[0].rstrip(), end=" ")
                dni.pop(0)
            print("",end="\n")
            
vypis_slova("sub.txt")
"""
def vypis_slova(meno_suboru):
    with open(meno_suboru,'r', encoding="utf8") as subor:
        i = 1
        j = 1
        for riadok in subor:
            riadok = riadok.rstrip()
            if i%j == 0:
                print(riadok)
                j += 1
                i = 1
            else:
                print(riadok,end=" ")
                i += 1
            
vypis_slova("sub.txt")
