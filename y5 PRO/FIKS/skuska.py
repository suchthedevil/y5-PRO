lines = [[1],[1,2],[1,2]]
scripts = [False, False]
permutation = "001"

for c,switch in enumerate(permutation):
    if switch == "1":
        for i in lines[c]:
            scripts[int(i-1)] = not scripts[int(i-1)]
print(scripts)