import tkinter

canvas = tkinter.Canvas(height=500,width=900)
canvas.pack()

zoznam = 'python java pascal c++ ruby php logo javascript'.split()

def click(event):
    if len(zoznam):
        canvas.create_text(event.x,event.y,text=zoznam.pop(0))
        canvas.create_text(event.x,event.y+20,text=f"({event.x},{event.y})")
canvas.bind('<Button-1>', click)
tkinter.mainloop()
