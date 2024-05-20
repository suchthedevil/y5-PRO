import tkinter

c = tkinter.Canvas(height=800, width=600)
c.pack()

c.create_text(300,100, text='pocet spadnutych kvapiek: 0', font='Arial 30', tag='counter')

x,y = 300,500
#kvapka a kaluza
c.create_oval(x-10,y-300,x+10,y-280, fill='cyan', outline='', tag='kvapka')
c.create_oval(x,y,x,y,fill='cyan', outline='', tag='kaluza')

#miska
c.create_oval(x-200,y-50,x+200,y+50)
c.create_oval(x-200,y-50-50,x+200,y+50-50)
c.create_line(x-200,y-50,x-200,y+50-50)
c.create_line(x+200,y-50,x+200,y+50-50)


i = 0
dx, dy, dy2 = 0, 0, 0
def fall():
    global i, dx, dy, dy2
    c.move('kvapka',0,10)
    if c.coords('kvapka')[3] == y+20:
        i += 1
        if dx == 200:
            dy2 -= 2
            c.create_oval(x-dx,y-50+dy2,x+dx,y+50+dy2, outline='', fill='cyan')
        else:
            dx += 200//10
            dy += 50//10
            c.coords('kaluza',x-dx,y-dy,x+dx,y+dy)
        c.coords('kvapka', x-10,y-300,x+10,y-280)
        c.itemconfig('counter', text=f'pocet spadnutych kvapiek: {i}')
    c.after(10,fall)

fall()
tkinter.mainloop()