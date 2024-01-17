pocet = int(input())
ceny = list(input().split())
najv = 0
for cena in ceny:
    najv += int(cena)

for cena in ceny:
    sucet = najv-int(cena)
    print(sucet)
