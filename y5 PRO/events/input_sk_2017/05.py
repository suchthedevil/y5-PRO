import tkinter
from random import shuffle
c = tkinter.Canvas(height=600,width=900)
c.pack()
x, y = 100, 100
n = 10
numbers = [i for i in range(n+1)]
shuffle(numbers)
occupied = []
copy = numbers[:]
for j,i in enumerate(numbers):
    c.create_rectangle(x,y,x+50,y+50,tag=f"s{j}")
    if i != 0:
        c.create_text((2*x+50)//2,(y+150)//2,text=numbers[j],tag=f"t{j}",font="Helvetica 20")
        occupied.append(1)
    else:
        zero = j
        c.create_text((2*x+50)//2,(y+150)//2,text="",font="Helvetica 20")
        occupied.append(0)
    x += 50

def moving(e):
    x = 100
    global zero, copy
    if 100 <= e.x <= 100+(n+1)*50 and 100 <= e.y <= 150:
        index = (e.x-100)//50
        print(index)
        if index != zero:
            c.delete('all')
            numbers[zero] = copy[index]
            numbers[index] = copy[zero]
            copy = numbers[:]
            if numbers == sorted(numbers):
                c.create_text(450,300,text='YOU WON!', fill='lime', font="Helvetica 50")
                c.unbind('<1>',moving)
            for j,i in enumerate(numbers):
                c.create_rectangle(x,y,x+50,y+50,tag=f"s{j}")
                if i != 0:
                    c.create_text((2*x+50)//2,(y+150)//2,text=numbers[j],tag=f"t{j}",font="Helvetica 20")
                    occupied.append(1)
                else:
                    zero = j
                    c.create_text((2*x+50)//2,(y+150)//2,text="",font="Helvetica 20")
                    occupied.append(0)
                x += 50
        
            

        
c.bind('<1>', moving)
tkinter.mainloop()