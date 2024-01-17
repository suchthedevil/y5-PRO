n = int(input())
vysledky = []
for i in range(n):
    cislo = '{:032b}'.format(int(input()))
    obratene = str(cislo)[::-1]
    vysledky.append(int(obratene,2))

for i in vysledky:
    print(i)

