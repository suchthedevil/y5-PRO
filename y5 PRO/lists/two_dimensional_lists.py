"""
with open("lists/tab.txt","r") as sub:
    tabulka = []
    for line in sub:
        tabulka.append(line.strip().split())
    print(tabulka)
"""
#16 

import tkinter

c = tkinter.Canvas(height=400,width=600)
c.pack()
def kruhy(meno_suboru):
    with open(meno_suboru,"r") as sub:
        x,y = 30,30
        znaky = [",","(",")"]
        for line in sub:
            colors = line.strip().split()
            for i in range(len(colors)):
                if colors[i] == "None":
                    pass
                elif "(" in colors[i]:
                    for znak in znaky:
                        colors[i] = colors[i].replace(znak," ")
                    r, g, b = colors[i].split()
                    color = f'#{int(r):02x}{int(g):02x}{int(b):02x}'
                    c.create_oval(x,y,x+30,y+30, fill=color)
                else:
                    c.create_oval(x,y,x+30,y+30, fill=colors[i])
                x += 40
            y += 40
            x = 30
kruhy("lists/colors.txt")

tkinter.mainloop()

def precitaj(meno_suboru):
    with open(meno_suboru,"r") as sub:
        rs = list(map(int,sub.readline().strip().split()))
        zoz = []
        for i in range(rs[0]):
            pom = [0]*rs[1]
            zoz.append(pom)
        for i in range(rs[0]):
            coord = list(map(int,sub.readline().strip().split()))
            zoz[coord[0]][coord[1]] = coord[2]
        print(zoz)
