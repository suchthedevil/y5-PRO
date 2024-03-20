import csv

sub = open("CVP/CSV files/NRSR2023.csv",encoding="utf-8-sig")
file2 = csv.reader(sub)

head = sub.readline().split(",")
c = 0
subjekty = {}
for line in file2:
    data_dic = {}
    if c == 0:
        pass   
    else:
        if "OĽANO" in line[0] or "Modrí" in line[0] or "Maďarské" in line[0]:
            pom = " ".join(line).split('"')
            s = pom[1].replace(",",";")
            pom2 = pom[0] + s + pom[2]
            line = pom2.split(",")
        for i in range(len(head)-1):
            data_dic[head[i]] = line[i]
        if data_dic['Názov politického subjektu'] not in subjekty.keys():
            subjekty[data_dic['Názov politického subjektu']] = int(data_dic['Počet platných prednostných hlasov'])
        else:
            subjekty[data_dic['Názov politického subjektu']] += int(data_dic['Počet platných prednostných hlasov'])
    c+=1

subjekty = dict(sorted(subjekty.items(),key=lambda x:x[1],reverse=True))
for pair in subjekty.items():
    print(f"{pair[0]}: {pair[1]}")

sub.close()