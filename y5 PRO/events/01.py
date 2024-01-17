import tkinter

canvas = tkinter.Canvas(height=500,width=900)
canvas.pack()

def click(event):
    canvas.create_text(event.x,event.y,text=f"({event.x},{event.y})")


canvas.bind('<Button-1>', click)
tkinter.mainloop()