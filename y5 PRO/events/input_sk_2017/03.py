import tkinter

c = tkinter.Canvas(height=600,width=900)
c.pack()

x,y = 100,100
for i in range(8):
    c.create_rectangle(x,y,x+50,y+50,tag=f"s{i}")
    x += 50

def color(e):
    if 100 <= e.x <= 100+8*50 and 100 <= e.y <= 150:
        index = (e.x-100)//50
        c.itemconfig(f's{index}',fill='red')


c.bind('<1>', color)
tkinter.mainloop()