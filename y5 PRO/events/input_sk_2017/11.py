import tkinter
c = tkinter.Canvas(width=900,height=600)
c.pack()

formula_img = tkinter.PhotoImage(file='events/input_sk_2017/formula.png')
formula = c.create_image(450,300,image=formula_img)
c.create_text(10,10,text='pica',angle=50)

def motion(e):
    if e.char == 'w':
        c.move(formula,0,-10)
    elif e.char == 's':
        c.move(formula,0,10)
    elif e.char == 'a':
        c.move(formula,-10,0)
    elif e.char == 'd':
        c.move(formula,10,0)
    
c.bind_all('<Key>',motion)
tkinter.mainloop()