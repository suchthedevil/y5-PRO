n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()
kopia_b = b[:]

for i in kopia_b:
    if i in a:
        a.remove(i)
        b.remove(i)

for i in b:
    if i-1 in a:
        a.remove(i-1)
        
if a == []:
    print("Jednoduche")
else:
    print("Neda sa")
    