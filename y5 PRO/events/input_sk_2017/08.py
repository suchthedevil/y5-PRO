import tkinter

c = tkinter.Canvas(width=900,height=600)
c.pack()

stv = c.create_rectangle(425,275,475,325,fill='red')
ova = c.create_oval(300,150,350,200,fill='blue')
clicked = False

def click(e):
    global clicked, which, dx, dy
    if len(c.find_overlapping(e.x,e.y,e.x,e.y)) > 0:
        which = c.find_overlapping(e.x,e.y,e.x,e.y)[0]
        clicked = True
        dx, dy = e.x-c.coords(which)[0], e.y-c.coords(which)[1]
        c.lift(which)

def drag(e):
    if clicked:
        size = abs(c.coords(which)[2] - c.coords(which)[0])
        c.coords(which,e.x-dx,e.y-dy,e.x-dx+size,e.y-dy+size)

c.bind('<1>',click)
c.bind('<B1-Motion>',drag)
tkinter.mainloop()