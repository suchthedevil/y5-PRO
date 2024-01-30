import json

file = open("CVP/CSV files/faktury_BB.json", 'r', encoding="utf-8")
data = json.load(file)

print(data)
file.close()
