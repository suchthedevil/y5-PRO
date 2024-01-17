import random, time, math
'''
pole = [random.randint(2,20) for x in range(15)]

print(pole)
'''
pole = [3, 11, 19, 4, 37, 13, 13, 20, 4, 5, 13, 18, 10]
"""
#Rozdelit na dve casti
rozdiel_max = float('inf')  #rozdiel nastavime na zaciaktu na neklonecno
start = time.time()
for i in range(1,(2**len(pole))//2):
    delenie = [[],[]]
    #binar = bin(i)[2:]
    #binar = "0"*(len(pole)-len(binar))+binar
    binar = f'{i:0{len(pole)}b}'
    for j,znak in enumerate(binar):
        delenie[int(znak)].append(pole[j])
    rozdiel = abs(sum(delenie[0])-sum(delenie[1]))
    if rozdiel <= rozdiel_max:
        rozdiel_max = rozdiel
        ake = [delenie[0],delenie[1]]
        if rozdiel == 0:
            break
print(ake[0],ake[1])
print(sum(ake[0]),sum(ake[1]))          
print(time.time()-start)
"""
#Rozdelit na lubovolne vela casti
def convert(num, system, new_system):
    whole = str(num)
    base_10_w = 0
    converted_w = ""
    for c,i in enumerate(whole[::-1]):
        base_10_w += int(i)*system**c
    while base_10_w > 0:
        rem = base_10_w%new_system
        base_10_w = base_10_w//new_system
        converted_w = str(rem) + str(converted_w)
    return(f"{converted_w}")

def rozdel(zoz,n):
    rozdiel_max = float('inf')  #rozdiel nastavime na zaciaktu na neklonecno
    for i in range(1,(n**len(zoz))):
        delenie = [[]]*n
        cislo = convert(i,10,n)
        cislo = "0"*(len(zoz)-len(cislo))+str(cislo)
        for j,znak in enumerate(cislo):
            delenie[int(znak)] = delenie[int(znak)] + [zoz[j]]
        rozdiel = 0
        for k in range(n-1):
            rozdiel += abs(sum(delenie[k])-sum(delenie[k+1]))
        print(rozdiel)    
        if rozdiel <= rozdiel_max:
            rozdiel_max = rozdiel
            ake = delenie[:]
            if rozdiel == 0:
                break
    print(ake)
    for i in ake:
        print(sum(i),end=" ")

rozdel([10,8,7,12,3,9,1,6],4)

