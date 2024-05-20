import tkinter

c = tkinter.Canvas(height=800,width=900)
c.pack()

def vypis_subor(nazov):
    x, y = 30,40
    with open(nazov,"r") as file:
        for line in file:
            c.create_text(x,y,text=line,anchor="w",font=("Calibri",30))
            y += 40

vypis_subor("y5 PRO/06.py")

tkinter.mainloop()

