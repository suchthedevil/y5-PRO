
t = open('sub.txt', encoding="utf8")
riadok = t.readline()
riadok2 = t.readline()
print(riadok.rstrip())    #strips empty characters from the right 
print(riadok2.rstrip())

for riadok in t:
    print(riadok.rstrip())
t.close() #treba zavriet subor po spracovani aby sme sa k nemu vedeli znova dostat neskor

#druhy sposob (tu nemusim davat na konci close)
with open('sub.txt', encoding='utf8') as t:
    for riadok in t:
        print(riadok.rstrip())



t.read() #precita cely subor naraz
t.read(15) #precita 15 znakov


#zapis do suboru metoda 1
t = open('novy.txt', "w", encoding="utf8")

t.write('jedna, dva tri\n')
t.write('styri,pat, sest\n')


#metoda 2

print("nieco", end=" ", file=t)
t.close()