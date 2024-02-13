
import tkinter

c = tkinter.Canvas(height=500,width=800)
c.pack()
x1,y1 = 100,100

stv = c.create_rectangle(x1,y1,x1+50,y1+50,fill='red',tag='stv')
obd = c.create_rectangle(x1+120,y1+100,x1+220,y1+150,fill='blue',tag='obd')

def klik(e):
    global dx, dy, klik, aky
    dx,dy = None, None
    print(c.find_overlapping(e.x,e.y,e.x,e.y))
    print(c.bbox('current'))
    print(c.find_withtag('current'))
    for prvok in stv, obd:
        sur = c.coords(prvok)
        if sur[0] <= e.x <= sur[2] and sur[1] <= e.y <= sur[3]:
            dx,dy = e.x-sur[0], e.y-sur[1]
            aky = prvok
            c.lift(aky)
            
def tahanie(e):
    sur = c.coords(aky)
    if dx != None:
        sirka, vyska = abs(sur[0]-sur[2]), abs(sur[1]-sur[3])
        c.coords(aky, e.x-dx, e.y-dy, e.x-dx+sirka,e.y-dy+vyska)

c.bind('<1>', klik)
c.bind('<B1-Motion>',tahanie)
tkinter.mainloop()


"""
import tkinter, random

c = tkinter.Canvas(height=500,width=800)
c.pack()

pocet = 15
farba = 'green'
vzd = 20
r = 1

def kresli(sx,sy):
    for i in range(pocet):
        x = sx+random.randrange(-vzd,vzd+1)
        y = sy+random.randrange(-vzd,vzd+1)
        c.create_oval(x-r, y-r, x+r, y+r, fill=farba, outline='')
        
def hover(e):
    kresli(e.x,e.y) 

c.bind('<B1-Motion>', hover)
c.bind('<Button-1>', hover)
#c.bind('<Motion>',hover)
tkinter.mainloop()
"""















