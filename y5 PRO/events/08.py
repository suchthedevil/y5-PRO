import tkinter

canvas = tkinter.Canvas(height=500,width=900)
canvas.pack()

x,y = 375,225
canvas.create_polygon(x,y,(x+x+50)//2,y+100,x+50,y,(x+x+50)//2,y-100,fill="red", tag="s")
canvas.create_rectangle(x,y+100,x+100,y+200, fill="blue",tag="s")


def klik(f):
    global dx, dy
    sur = canvas.coords('s')
    if sur[0] <= f.x <= sur[2] and sur[1] <= f.y <= sur[3]:
        dx,dy = f.x-sur[0], f.y-sur[1]
        klik = True

def drag(f):
    sur = canvas.coords('s')
    if klik:
        canvas.coords('s',f.x-dx,f.y-dy,f.x+50-dx,f.y+50-dy)
    

canvas.bind('<1>',klik)
canvas.bind('<B1-Motion>',drag)
tkinter.mainloop()