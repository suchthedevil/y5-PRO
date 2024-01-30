import tkinter

canvas = tkinter.Canvas()
canvas.pack()

sur = []
def klik(event):
    global id
    sur[:] = [event.x, event.y]*2
    id = canvas.create_line(sur)

def tahanie(e):
    sur[2:4] = [e.x,e.y]
    canvas.coords(id,sur)

canvas.bind('<Button-1>', klik)
canvas.bind('<B1-Motion>', tahanie)

tkinter.mainloop()