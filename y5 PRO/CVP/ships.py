import tkinter, random

c = tkinter.Canvas(height=800, width=500)
c.pack()
x,y = 15,20
def lodicka(x,y,n,color):
    c.create_rectangle(x,y,x+100,y+50,fill=color, tag=f"bot{n}")

c.create_line(400,0,400,800,fill='red')
my = random.randrange(0,10)
for i in range(10):
    if i != my:
        lodicka(x,y,i,'black')
    else:
        lodicka(x,y,i,'red')
    y += 75

"""
c.itemconfig(my,tag="myboat")
c.itemconfig('myboat',fill='red')
"""
def click(e):
    dx = 10
    c.move(f'bot{my}',dx,0)

pause = False

def timer():
    global pause
    if c.coords(my)[2] > 400:
        c.create_text(300,250,text="You won")
        pause = not pause
        c.unbind_all('<space>')
        c.unbind('<1>')
    if pause:
        for i in range(0,10):
            if i != my:
                dx = random.randrange(2,10)
                c.move(f'bot{i}',dx,0)
        c.after(100,timer)
timer()

def space(f):
    global pause
    pause = not pause
    timer()

c.bind('<1>',click)
c.bind_all('<space>',space)

tkinter.mainloop()