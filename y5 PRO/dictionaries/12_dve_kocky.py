import random

def dve_kocky(n):
    ft = {}
    freq = [0]*12
    for i in range(n):
        k1 = random.randrange(1,7)
        k2 = random.randrange(1,7)
        sucet = k1+k2
        freq[sucet-1] += 1
    for i,s in enumerate(freq):
        ft[f'{i+2}'] = freq[i]
    print(ft)
    
dve_kocky(1000)


