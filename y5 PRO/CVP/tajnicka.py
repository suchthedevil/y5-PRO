import tkinter

c = tkinter.Canvas(height=600,width=800)
c.pack()

def tajnicka(subor,hidden):
    x,y = 150,60
    with open(subor,"r") as sub:
        riesenie = sub.readline().rstrip()
        slova = []
        for line in sub:
            slova.append(line.rstrip())
        for i in range(len(riesenie)):
            c.create_rectangle(x,y,x+30,y+30,fill="gray")
            index = slova[i].lower().find(riesenie[i].lower())
            for l,k in enumerate(slova[i]):
                c.create_rectangle(x-(index-l-1)*30,y,x-(index-l)*30,y+30)
                if l != index:
                    c.create_text(x-(index-l-1)*30-15,y+15,text=k.upper())
                else:
                    c.create_text(x-(index-l-1)*30-15,y+15,text=k.upper(),font="Arial 10 bold")
            y += 30
        x,y = 500,60
        for i in range(len(riesenie)):
            c.create_rectangle(x,y,x+30,y+30,fill="gray")
            index = slova[i].lower().find(riesenie[i].lower())
            for l,k in enumerate(slova[i]):
                c.create_rectangle(x-(index-l-1)*30,y,x-(index-l)*30,y+30)
            y += 30
tajnicka("y5 PRO/CVP/tajn.txt","no")
tkinter.mainloop()