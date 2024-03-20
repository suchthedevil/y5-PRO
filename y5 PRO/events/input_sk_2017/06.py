import tkinter
c = tkinter.Canvas(height=600,width=900)
c.pack()

def click(e):
    global coordinates, id
    coordinates = [e.x,e.y]
    id = c.create_line(coordinates*2)

def drag(e):
    coordinates[2:] = [e.x,e.y]
    c.coords(id,coordinates)


c.bind('<1>', click)
c.bind('<B1-Motion>',drag)
tkinter.mainloop()