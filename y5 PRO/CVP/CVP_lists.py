"""
n = int(input())
ceruzky = []

for i in range(n):
    c = int(input())
    ceruzky.append(c)
if len(ceruzky) > 1:
    for i in range(2):
        najv = max(ceruzky)
        ceruzky.pop(ceruzky.index(max(ceruzky)))  
    pocet = najv-1
    if pocet >= len(ceruzky):
        pocet = len(ceruzky)
    elif pocet <= 2 or len(ceruzky) <= 2:
        pocet = 0
    print(pocet)
else:
    print(0)
"""
start, end = [int(x) for x in input().split()] 
n = int(input())
mystery = [int(x) for x in input().split()]
all = mystery + [start,end]
all.sort()

pocet = 0
for i in range(len(all)-1):
    if all[i+1] in mystery and all[i] in mystery and n>0:
        odpocet = 1
    elif n>0:
        odpocet = 0
    else:
        odpocet = -1
    
    if all[i+1] - all[i] - odpocet > pocet:
        pocet = all[i+1]-all[i]-odpocet
print(pocet)