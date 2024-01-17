import tkinter
import random 

canvas = tkinter.Canvas(height=500,width=900)
canvas.pack()
x,y = 100, 50
r = 50
for i in range(8):
    canvas.create_rectangle(x,y,x+r,y+r)
    x += r
colors = ['white','blue','red']

kolko = 0

def vypln(event):
    global kolko
    kolko += 1
    index = (event.x-100)//50
    if 0 <= index < 8:
        color = colors[(kolko%3)-1]
        canvas.itemconfig(index+1,fill=color)

canvas.bind('<1>',vypln)
tkinter.mainloop()
