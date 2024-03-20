with open('CVP/CSV files/klienti.txt','r',encoding='utf8') as f:
    for line in f:
        l = line.rstrip().split("\t")
        print(f"('{l[0]}','{l[1]}',{round(float(l[2].replace(',','.')),1)},'{l[3].replace(' ','')}','{l[4]}')")
