"""
import tkinter

c = tkinter.Canvas(height=400, width=800)
c.pack()

stv = c.create_rectangle(150,150,200,200, fill='red')
smer = 2

pauza = False

def timer():
    global smer
    if pauza:
        if c.coords(stv)[0] < 1 or c.coords(stv)[2] >799:
            smer *= -1
        c.move(stv,smer,0)
    c.after(10,timer)
def klik(e):
    global pauza
    pauza = False if pauza else True

timer()
c.bind('<1>',klik)
c.mainloop()

"""

import tkinter, random
c = tkinter.Canvas(height=400, width=800)
c.pack()

x,y = random.randrange(60,740), random.randrange(60,340)
interval = 1000
r = 30
score = 0
clicked = False
kruh = c.create_oval(x, y,x+2*r, y+2*r, fill="red")
s = c.create_text(50,20,text=f"Skore: {score}",font="Arial 15")
def timer():
    global clicked, score
    if clicked:
        clicked = False
    elif score > 0:
        score -= 1
        new_x, new_y = random.randrange(60,740), random.randrange(60,340)
        c.coords(kruh,new_x, new_y,new_x+2*r,new_y+2*r)
    c.itemconfig(s,text=f"Skore: {score}")
    if score != 10:
        c.after(interval,timer)

def klik(e):
    global score, clicked
    if len(c.find_withtag("current")):
        clicked = True
        score += 1
        c.itemconfig(s,text=f"Skore: {score}")
    new_x, new_y = random.randrange(60,740), random.randrange(60,340)
    c.coords(kruh,new_x, new_y,new_x+2*r,new_y+2*r)

timer()
c.bind('<1>',klik)
c.mainloop()


















