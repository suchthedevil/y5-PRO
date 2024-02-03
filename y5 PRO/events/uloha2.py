import tkinter, random

c = tkinter.Canvas(height=400,width=600)
c.pack()


def klik(event):
    if 20 <= event.y <= a + 20:
        global k
        k += 1
        where = event.x//a
        c.coords(f"t{where}",(10+a*(empty))//2,(y+y+a)//2)
      

x,y = 10, 20
n = random.randrange(5,15)
a = (500)//n 
numbers = list(range(1,n+1))
random.shuffle(numbers)
numbers.insert(random.randrange(0,n)," ")
for i in range(n+1):
    if numbers[i] == " ":
        empty = i
    c.create_rectangle(x,y,x+a,y+a,fill="yellow", tag=f"s{i}")
    c.create_text((x+x+a)//2,(y+y+a)//2, text=numbers[i], tag=f"t{i}")
    x += a
    

k = 0
c.bind('<ButtonPress>', klik)


tkinter.mainloop()