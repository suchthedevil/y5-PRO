import tkinter
from math import sin, cos, radians
c = tkinter.Canvas(width=900,height=600)
c.pack()

my_line = c.create_line(150, 150, 150, 50)
m = 100
r = 50
angle = 120

def timer():
    global angle
    angle += 6
    c.coords(my_line,m+cos(radians(angle))*r,m+sin(radians(angle))*r,m+cos(radians(angle+180))*r,m+sin(radians(angle+180))*r)
    c.after(1000,timer)
timer()

tkinter.mainloop()