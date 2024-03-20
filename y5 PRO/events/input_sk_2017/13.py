import tkinter, random
c = tkinter.Canvas(width=900,height=600)
c.pack()
color = 'red'

def timer():
    global color
    x,y = random.randrange(20,880), random.randrange(20,580)
    l = chr(random.randrange(65,91))
    c.create_text(x,y,text=l,fill=color)
    c.after(100,timer)

def timer2():
    global color
    color = f'#{random.randrange(255**3):06x}'
    c.after(3000,timer2)
    
timer()
print('pica')
timer2()

tkinter.mainloop()