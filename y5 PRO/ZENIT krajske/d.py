n = int(input())

numbers = list(map(int, input().split(" ")))
multip = 1

for i in range(n):
    multip = (multip * numbers[i]) % (10**9 + 7)
out = [str(pow(numbers[i], -1, 10**9 + 7) * numbers % (10**9 + 7)) for i in range(n)]
print(" ".join(out))
