
import random
def prvo(cislo):
    for i in range(2,int(cislo**(1/2)+1)):
        if cislo%i == 0:
            return False
    return True
with open("prvocisla.txt","w") as subor:
    for i in range(5):
        p = 0
        while p != 8:
            cislo = random.randrange(0,5000)
            if prvo(cislo):
                print(cislo, end=" ", file=subor)
                p += 1
        print(file=subor)

