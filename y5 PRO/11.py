#program vytvori program prvocisla.py, ktory vytvori
#textovy subor s random prvocislami do dopredu zadaneho poctu
#riadkov a stlpcov

def vyrob(nazov,n,riadkov):
    with open(nazov,'w') as subor:
        text = f"""
import random
def prvo(cislo):
    for i in range(2,int(cislo**(1/2)+1)):
        if cislo%i == 0:
            return False
        return True
with open("prvocisla.txt","w") as subor:
    for i in range({riadkov}):
        p = 0
        while p != {n}:
            cislo = random.randrange(0,5000)
            if prvo(cislo):
                print(cislo, end=" ", file=subor)
                p += 1
        print(file=subor)
"""
        print(text, file=subor)

vyrob("prvocisla.py",8,5)