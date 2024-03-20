import tkinter
c = tkinter.Canvas(height=600,width=900)
c.pack()

def out(e):
    c.create_text(e.x,e.y,text=f"[{e.x},{e.y}]",font=("Arial",20))

c.bind('<1>', out)
tkinter.mainloop()