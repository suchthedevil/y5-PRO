import tkinter, random
h,w = 600,900
c = tkinter.Canvas(height=h,width=w)
c.pack()
r = 50
i = 1
list = []
def click(e):
    global i
    color = f"#{random.randrange(255**3):06x}"
    obj = c.create_oval(e.x-50,e.y-50,e.x+50,e.y+50,fill=color,tag=f'k{i}')
    list.append(obj)
    i += 1

def timer():
    for i in list:
        if c.coords(i)[2] - c.coords(i)[0] > 2:
            c.coords(i,c.coords(i)[0]+1,c.coords(i)[1]+1,c.coords(i)[2]-1,c.coords(i)[3]-1)
        else:
            c.delete(i)
            list.remove(i)
    c.after(100,timer)
timer()
c.bind('<1>',click)
tkinter.mainloop()