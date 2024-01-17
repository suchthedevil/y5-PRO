n, k = map(int,input().split())
pole = [int(x) for x in input().split()]
out = ""
for i in range(n-k+1):
    maxim = max(pole[i:i+k])
    if i < n-k:
        out += str(maxim) + " "
    else:
        out += str(maxim)
print(out)
