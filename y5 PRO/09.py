import tkinter

c = tkinter.Canvas(height=400,width=400)
c.pack()

def do_riadkov(nazov,sirka):
    with open(nazov,'r') as sub:
        x,y = 20,20
        for i,riadok in enumerate(sub):
            c.create_rectangle(x,y,x+50,y+50,fill=riadok.rstrip())
            x += 50
            if (i+1)%sirka == 0:
                y += 50
                x = 20

do_riadkov("farbicky.txt",5)


tkinter.mainloop()