def gcf(a,b):
    while a%b != 0:
        zv = a%b
        a = b
        b = zv
    return b
"""
with open("CVP/cisla_gcf.txt","r") as sub:
    for line in sub:
        line = line.rstrip()
        cisla = [int(x) for x in line.split()]
        for i in range(min(cisla),0,-1):
            pocet = 0
            for cislo in cisla:
                if cislo%i == 0:
                    pocet += 1
                else:
                    break
            if pocet == len(cisla):
                print(f"NSD({line.replace(' ',',')})={i}")
                break

"""
            
print(gcf(8,12))
    
    