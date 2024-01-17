import tkinter

c = tkinter.Canvas()
c.pack()

def kresli(nazov):
    body = []
    with open(nazov,"r") as sub:
        for line in sub:
            if line != "\n":
                prve, druhe = int(line[:line.find(" ")]), int(line[line.find(" "):])
                body.append(prve)
                body.append(druhe)
            else:
                c.create_line(body)
                body = []
        c.create_line(body)

kresli("body.txt")
tkinter.mainloop()