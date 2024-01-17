#create a dictionary from a txt file
with open("CVP\dics.txt", "r") as f:
    dict1 = {}
    for line in f:
        key = line[0]
        value = line[2:].split()
        dict1[f"{key}"] = value
    print(dict1)
