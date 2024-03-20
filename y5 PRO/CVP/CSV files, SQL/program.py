import csv

sub = open("CVP/CSV files/naklady.csv",encoding="utf-8-sig")
file2 = csv.reader(sub)
dic, new_dic = {}, {}
for line in file2:
    datum, suma = line[0].split(" ")
    dic[datum] = float(suma[:-1])
#vypis trzieb po measiacoch
for pair in dic.items():
    mesiac = int(pair[0].split(".")[1])
    if mesiac in new_dic.keys():
        new_dic[mesiac] = round(new_dic[mesiac] + pair[1],2)
    else:
        new_dic[mesiac] = pair[1]

print(dict(sorted(new_dic.items(),key= lambda x : x[0])))

#zapis do .csv file chronologicky
zoz = []
for pair in dic.items():
    d,m,r = str(pair[0]).split(".")
    if len(d) == 1:
        d = "0"+d
    if len(m) == 1:
        m = "0"+m
    num_str = r+m+d
    num_int = int(num_str)
    zoz.append([num_int,pair[0]])

zoz = list(sorted(zoz,key=lambda x:x[0]))

sorted_dic = {}
for i in zoz:
    sorted_dic[i[1]] = dic[i[1]]

f = open("naklady_sorted.csv", "w", encoding="utf-8-sig")
writer = csv.writer(f,lineterminator="\n", delimiter=" ")
for pair in sorted_dic.items():
    writer.writerow(pair)

f.close()
sub.close()