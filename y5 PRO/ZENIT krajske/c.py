n = int(input())
cisla = list(map(int,input().split()))

unique_elements = set(cisla)
maxim = 0

for i in unique_elements:
    for j in unique_elements:
        if i == j:
            continue

        count = 0
        dp = [0] * len(cisla)
        for idx, k in enumerate(cisla):
            if k == i or k == j:
                count += 1
            else:
                count = 0
            dp[idx] = count
        maxim = max(maxim, max(dp))
print(maxim)