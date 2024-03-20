import tkinter
c = tkinter.Canvas(width=900,height=600)
c.pack()
h,m,s = 17, 59, 58.5
clock = c.create_text(450,300,text=f'{h}:{m}:{round(s,1)}', font='Helvetica 50')

def timer():
    global h,m,s
    s += 0.1
    if round(s,1) == 60.0:
        m += 1
        s = 0.0
    elif m == 60:
        h += 1
        m = 0
    c.itemconfig(clock,text=f'{h}:{m}:{round(s,1)}')
    c.after(100,timer)

timer()
tkinter.mainloop()