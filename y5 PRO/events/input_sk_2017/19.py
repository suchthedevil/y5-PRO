import tkinter, random
c = tkinter.Canvas(width=900,height=600)
c.pack()

interval = 1000
r = 50
score = 0
i = 0
sc = c.create_text(10,10,text=f"Score:{score}",font='Helvetica 20', anchor='nw')
def timer():
    global ball,i
    i += 1
    x,y = random.randrange(50,750), random.randrange(50,550)
    ball = c.create_oval(x-r,y-r,x+r,y+r,fill='red',tag=f'ball{i}')
    c.delete(f'ball{i-1}')
    c.after(interval,timer)
    

def click(e):
    global score
    c.itemconfig(sc,text=f"Score:{score}")
    if len(c.find_overlapping(e.x,e.y,e.x,e.y)) > 0:
        c.delete(ball)
        score += 1
    else:
        score -= 1

timer()
c.bind('<1>',click)
tkinter.mainloop()