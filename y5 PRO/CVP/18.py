import random
import tkinter

c = tkinter.Canvas(height=550, width=700)
c.pack()
x,y = 20,500
with open("kocky.txt","w") as f:
    for i in range(100000):
        print(f"{random.randint(1,6)} {random.randint(1,6)} {random.randint(1,6)}", file=f)

with open("kocky.txt","r") as f:
    sucty = []
    for line in f:
        sucet = int(line[0])+int(line[2])+int(line[4])
        sucty.append(sucet)

    maxim = 0
    for i in range(3,19):
        n = sucty.count(i)
        if n > maxim:
            maxim = n

    for i in range(3,19):
        p = sucty.count(i)
        c.create_text(x+15,y,text=i, font="arial 15")
        c.create_rectangle(x,y-30,x+30,y-30-(400/maxim)*p,fill="red", outline="")
        x += 40
        y = 500

tkinter.mainloop()
