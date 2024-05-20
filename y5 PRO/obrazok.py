import tkinter

c = tkinter.Canvas(height=900, width=900)
c.pack()
"""
with open("cotuje.txt", 'r') as sub:
    code = sub.read()
    farba = ''
    x,y = 0,0
    for j in code:
        if j != "\n":
            farba += str(j)
        else:
            y += 1
            x = 0
        if len(farba) == 6:
            c.create_rectangle(x,y,x+1,y+1, fill=f"#{farba}", outline='')
            x += 1
            farba = ''
"""   

with open("y5 PRO/cotuje.txt", 'r') as sub:
    x,y,farba = 0,0,''
    for j,line in enumerate(sub):
        for i in range(0,len(line)-1,6):
            farba += line[i:i+6]
            c.create_rectangle(x,y,x+1,y+1, fill=f"#{farba}", outline='')
            farba = ''
            x +=  1
        y += 1
        x = 0

"""
with open("cotuje.txt", 'r') as sub:
    x,y,farba = 0,0,''
    for j,line in enumerate(sub):
        for i in range(0,len(line)-1,6):
            farba += line[i:i+6]
            r,g,b = farba[0:2], farba[2:4], farba[4:6]
            vypocet = (int(r,16)+int(g,16)+int(b,16))//3
            grayscale = f"{vypocet:06}"
            c.create_rectangle(x,y,x+1,y+1, fill=f"#{grayscale}", outline='')
            farba = ''
            x +=  1
        y += 1
        x = 0
"""
tkinter.mainloop()