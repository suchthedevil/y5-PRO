rows, cols = map(int,input().split())
pismena = input().split()
out = ""
for i in range(cols):
    cisla = input()
    for j,cislo in enumerate(cisla):
        if cislo == '.':
            out += cislo
        else:
            out += pismena[(int(cislo)-1)%9]
    if i != cols-1:
        out += "\n"
print(out)

