import tkinter
c = tkinter.Canvas(height=600,width=900)
c.pack()

def out(e):
    c.create_text(e.x,e.y,text=f"[{e.x},{e.y}]",font=("Arial",20))

id = c.create_rectangle(20,20,40,40, fill='red')
id2 = c.create_text(50,50,text='pica')

print(c.itemcget(id2,'text'))

c.bind('<1>', out)
tkinter.mainloop()