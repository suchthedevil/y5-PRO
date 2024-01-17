import tkinter, random

c = tkinter.Canvas(height=500, width=500,background="black")
c.pack()

hz = ['32','64','128','256','512','1k','2k','3k','4k']


while True:
    x = 50
    y = 450
    for i,j in enumerate(hz):
        c.create_text(x+15,y+20,text=j, font="Arial 10", fill="white")
        h = random.randint(1,400)

        if h <= 200:
            c.create_rectangle(x,y,x+30,y-h, outline="", fill="green",tags="stlpec")
        elif 200 < h <= 300:
            c.create_rectangle(x,y,x+30,y-200, outline="", fill="green",tags="stlpec")
            c.create_rectangle(x,y-200,x+30,y-200-(h-200), outline="",fill="yellow",tags="stlpec")
        else:
            c.create_rectangle(x,y,x+30,y-200, outline="",fill="green",tags="stlpec")
            c.create_rectangle(x,y-200,x+30,y-300, outline="",fill="yellow",tags="stlpec")
            c.create_rectangle(x,y-300,x+30,y-300-(h-300), outline="",fill="red",tags="stlpec")
        x += 50
    c.update()
    c.after(100)
    c.delete("stlpec")

tkinter.mainloop()

#druhy sposob: vygenerovat vsetky stlpce v plnej vyske, 
#potom len z hora generovat cierny kt. prekryje do pozadovanej vysky