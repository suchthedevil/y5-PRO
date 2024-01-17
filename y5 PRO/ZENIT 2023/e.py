n = int(input())
filmy = []
for i in range(n):
    filmy.append(int(input()))
filmy.sort()
if len(filmy) <= 2:
    print(0)
else:    
    najdlhsi_1 = filmy.pop()
    najdlhsi_2 = filmy.pop()
    pocet_moznych = najdlhsi_2-1
    if pocet_moznych > len(filmy):
        ans = len(filmy)
    else:
        ans = pocet_moznych
    print(ans)

