import tkinter

c = tkinter.Canvas(height=600,width=900)
c.pack()
zoznam = 'python java pascal c++ ruby php logo javascript'.split()
i = 0

def out(e):
   global i
   if i < len(zoznam):
    c.create_text(e.x,e.y,text=zoznam[i])
    i += 1

c.bind('<1>', out)
tkinter.mainloop()