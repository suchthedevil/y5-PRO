import random
with open("farbicky.txt", "a") as subor:
    for i in range(4):
        print(random.choice(("red","green","blue")),file=subor)
