import tkinter, random

c = tkinter.Canvas(height=600,width=900)
c.pack()
zoz = []
def timer():
    for id in zoz:
        c.coords(id,c.coords(id)[0]+1,c.coords(id)[1]+1,c.coords(id)[2]-1,c.coords(id)[3]-1)
    c.after(100,timer)

def click(e):
    id = c.create_oval(e.x-50,e.y-50,e.x+50,e.y+50,fill=f'#{random.randrange(255**3):06x}')
    zoz.append(id)

timer()

c.bind('<1>',click)
tkinter.mainloop()