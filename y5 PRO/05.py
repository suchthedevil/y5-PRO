"""
import random
with open("cisla.txt",'w') as cisla:
    for i in range(10):
        print(random.randrange(1,100), file=cisla)
    cisla.close()
"""
def priemer(meno):
    with open(meno,"r") as subor:
        sucet = 0
        for i,riadok in enumerate(subor):
            if riadok != "\n":       #existuje funkcia .isnumeric()
                pocet = i+1
                sucet += int(riadok.strip())
        avg = sucet/pocet
    print(avg)

priemer("cisla.txt")