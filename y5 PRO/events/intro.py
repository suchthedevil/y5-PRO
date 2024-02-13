"""
import tkinter

canvas = tkinter.Canvas(height="500",width="900")
canvas.pack()

def klik(event):
    canvas.create_line(100, 200, event.x, event.y, fill='red', width=3)

def tahanie(event):
    canvas.create_line(100, 200, event.x, event.y)

canvas.bind('<Button-1>', klik)
canvas.bind('<B1-Motion>', tahanie)
"""
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

zoznam = []

def klik(event):
    global ciara
    zoznam[:] = [event.x, event.y]
    ciara = canvas.create_line(0, 0, 0, 0)

def tahanie(event):
    zoznam.extend([event.x, event.y])
    print(zoznam)
    canvas.coords(ciara, zoznam[0], zoznam[1], zoznam[-2], zoznam[-1])

canvas.bind('<Button-1>', klik)
canvas.bind('<B1-Motion>', tahanie)
tkinter.mainloop()