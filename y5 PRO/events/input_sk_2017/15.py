import tkinter, random
c = tkinter.Canvas(width=900,height=600)
c.pack()

r = 50
x, y = 450,300
for i in range(10):
    c.create_oval(x-r,y-r,x+r,y+r,fill=f'#{random.randrange(255**3):06x}',tag='k')
    r -= 5

def timer():
    c.move('k',5,0)
    c.after(50,timer)

timer()


tkinter.mainloop()