import time
start = time.time()
sub2 = open('vystup2.txt', 'w')
with open("nw3.txt","r") as sub:
    tasks = int(sub.readline().strip())
    for task in range(tasks):
        n = int(sub.readline().strip())
        knots = [int(x) for x in sub.readline().split()]
        divisors = []
        divisors_unique = []
        for cislo in knots:
            divisors_unique.append(cislo)
            for i in range(1,(int(cislo**0.5))+1):
                if cislo%i == 0:
                    divisors.append(i)
                    divisors.append(cislo//i)
                    if i not in divisors_unique:
                        divisors_unique.append(i)
                        divisors_unique.append(cislo//i)
        divisors_unique.sort()
        max = 0
        for i in divisors_unique:
            if i > 200:
                break
            if i <= divisors.count(i):
                max = i
        print(max,file=sub2)     
sub2.close()
end = time.time()
print(end-start,"s")