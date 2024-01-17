from sys import exit
subor2 = open('vystup.txt', 'w')
with open(input(),'r') as subor:
    t = int(subor.readline().strip())
    for oi in range(t):
        h, w, n = tuple(subor.readline().strip().split())
        zoznam = [' ']*2*(int(h)+int(w))
        for k in range(int(n)):
            y, x, c = tuple(subor.readline().strip().split())
            if int(x) == 0:
                zoznam[int(y)] = c
            elif int(y)==int(h):
                zoznam[int(h)+int(x)] = c
            elif int(x)==int(w):
                zoznam[int(h)+int(w)+int(h)-int(y)] = c
            elif int(y)==0:
                zoznam[int(h)+int(w)+int(h)+int(w)-int(x)] = c
        zoznam = [x for x in  zoznam if x != ' ']
        zoz_string = ''.join(str(i) for i in zoznam)
        zoznam_unique = []
        for i in zoznam:
            if i not in zoznam_unique:
                zoznam_unique.append(i)

        if len(zoznam)%2 != 0:
            print("ajajaj",file=subor2)
            continue
        elif zoznam == zoznam[::-1]:
            print("pujde to",file=subor2)
            continue

        while zoz_string:
            count = 0
            for k in zoznam_unique:                                   # [1,2,3,4]
                if f'{k}{k}' in zoz_string:
                    zoz_string = zoz_string.replace(f'{k}{k}','')
                elif f'{k}{k}' not in zoz_string:
                    count += 1
            if count == len(zoznam_unique):
                print("ajajaj",file=subor2)
                break
        if zoz_string == '':
            print("pujde to",file=subor2)
            continue
