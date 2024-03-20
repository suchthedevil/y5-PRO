import tkinter
c = tkinter.Canvas(width=900,height=600)
c.pack()

x, y = 450, 300
stv = c.create_rectangle(x-50,y-50,x+50,y+50,fill='blue')
pause = False
dx = 5
def stop(e):
    global pause
    pause = not pause

def timer():
    global dx
    if not pause:
        c.move(stv,dx,0)
    if 0 > c.coords(stv)[0] or c.coords(stv)[2] > 900:
        dx = -dx
    c.after(100,timer)
    
timer()
c.bind('<1>',stop)
tkinter.mainloop()