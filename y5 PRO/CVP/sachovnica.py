import random

yes = 0
no = 0
pairs = []
grid = []
pattern = "bwbwbwbw"
for i in range(8):
    grid.append(pattern)
    pattern = pattern[1:] + pattern[0]
    
for j in range(1000):
    white = 0
    black = 0
    count = 0
    while count < 8:
        x = random.randrange(0,8)
        y = random.randrange(0,8)
        if [x,y] not in pairs:
            if grid[x][y] == "w":
                white += 1
            else:
                black += 1
            count += 1
            pairs.append([x,y])
    if white >= 3:
        yes += 1
    else:
        no += 1

print(yes/(yes+no)*100)
