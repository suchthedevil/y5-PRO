import tkinter

canvas = tkinter.Canvas(height=400, width=800)
canvas.pack()

zoznam = []

def klik(event):
    global ciara
    zoznam[:] = [event.x, event.y]
    ciara = canvas.create_line(0, 0, 0, 0)

def tahanie(event):
    zoznam.extend([event.x, event.y])
    canvas.coords(ciara, zoznam[0], zoznam[1], zoznam[-2], zoznam[-1])

canvas.bind('<Button-1>', klik)
canvas.bind('<B1-Motion>', tahanie)
tkinter.mainloop()