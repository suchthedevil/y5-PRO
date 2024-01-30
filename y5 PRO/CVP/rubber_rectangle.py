import tkinter,random

canvas = tkinter.Canvas(height=400,width=800)
canvas.pack()

sur = []
def klik(event):
    color = f"#{random.randrange(255**3):06x}"
    global id
    sur[:] = [event.x, event.y]*2
    id = canvas.create_rectangle(sur, fill=color)

def tahanie(e):
    sur[2:4] = [e.x,e.y]
    canvas.coords(id,sur)

canvas.bind('<Button-1>', klik)
canvas.bind('<B1-Motion>', tahanie)


tkinter.mainloop()