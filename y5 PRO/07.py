import tkinter

c = tkinter.Canvas()
c.pack()

def kresli(nazov):
    body = []
    with open(nazov,"r") as sub:
        for line in sub:
            prve, druhe = int(line[:line.find(" ")]), int(line[line.find(" "):])
            body.append(prve)
            body.append(druhe)
        c.create_line(body)

kresli("body.txt")

tkinter.mainloop()