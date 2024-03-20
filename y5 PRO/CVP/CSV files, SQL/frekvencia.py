import csv
import matplotlib.pyplot as plt

sub = open("CVP/CSV files/populacia.csv",encoding="utf-8-sig")
file = csv.reader(sub)

dic = {}
for line in file:
    country, population, area = line[0].split(";")
    if population[0] == "p":
        continue
    if population[0] not in dic.keys():
        dic[population[0]] = 1
    else:
        dic[population[0]] += 1

dic = dict(sorted(dic.items(),key=lambda x:x[0]))
for pair in dic.items():
    print(f"{pair[0]}: {pair[1]}")

plt.bar(dic.keys(),dic.values())
plt.show()
sub.close()