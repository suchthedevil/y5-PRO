import random, time
nums = [1000,10000,100000,1000000]
times = {}
for n in nums:
    li = []
    start = time.time()
    for i in range(n):
        li.append(random.randrange(0,100))
    duration = time.time()-start
    times[n] = round(duration*1000,3)

print(times)

