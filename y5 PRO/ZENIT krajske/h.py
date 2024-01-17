n = int(input())
dosky = list(map(int,input().split()))
naj = min(dosky)
tahy = naj

for i in range(len(dosky)):
    dosky[i] -= naj

sublists = []
def subdiv(zoznam):
    sublist = []
    for i in zoznam:
        if i == 0:
            if sublist != []:
                sublists.append(sublist)
            sublist= []
        else:
            sublist.append(i)
    if sublist != []:
        sublists.append(sublist)
        naj = min(sublist)
        tahy += naj
        for k in range(len(sublist)):
            dosky[k] -= naj
            subdiv(sublist)
    print(tahy)

subdiv(dosky)
