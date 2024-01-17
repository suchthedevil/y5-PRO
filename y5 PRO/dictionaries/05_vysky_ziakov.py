vysky = {'Jano': 148, 'Tomas': 183, 'Igor': 190, 'Peter': 158, 'Denis': 191, 'Andrea': 182, 'Filip': 197, 'Matej': 168, 'Jana': 200, 'Livia': 195}

#Sort by names alphabetically
vysky = dict(sorted(vysky.items()))
for item in vysky.items():
    print(item)

#Sort by heights in ascending order
vysky = dict(sorted(vysky.items(),key= lambda x : x[1]))
for item in vysky.items():
    print(item)

#Calculate the average of the heights
def avg(dic):
    sum = 0
    for v in dic.values():
        sum += v
    return round(sum/len(dic.values()),2)

#Add ABOVE to the key:value pair if above average, analogically if below
average = avg(vysky)
def vypis(dic):
    for i in dic.items():
        if i[1] > average:
            add = "ABOVE"
        elif i[1] < average:
            add = "BELOW"
        else:
            add = "AVERAGE"
        print(i[0],i[1],add)

#vypis(vysky)

def len_od_do(dic,od,do):
    new_dic = {}
    for i in dic.items():
        if od < i[1] < do:
            new_dic[i[0]] = i[1]
    print(new_dic)

def prevrat(dic):
    new_dic = {}
    for i in dic.items():
        new_dic[i[1]] = i[0]
    print(new_dic)

prevrat(vysky)

