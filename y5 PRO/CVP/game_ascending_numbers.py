import tkinter, random
h, w = 400, 800
c = tkinter.Canvas(height=h,width=w+200)
c.pack()

x, y = 20, 20
n = random.randrange(5,16)
nums = list(range(1,n+1))
nums.append("*")
random.shuffle(nums)
#a = (w-40)//(n+1)
a = 30

for i in range(n+1):
    c.create_rectangle(x,y,x+a,y+a,fill="yellow")
    c.create_text((x+x+a)//2,(y+y+a)//2, text=nums[i],font="Arial 15", tag=f"s{i}")
    if nums[i] == "*":
        empty_index = i
    x += a

x = 20

def select(event):
    global empty_index
    print(empty_index, end=" ")
    if (y <= event.y <= y+a) and (x <= event.x <= x+(n+1)*a):
        index_clicked = (event.x-20)//a
        print(index_clicked)
        c.coords(f's{index_clicked}',(x+(empty_index)*a+x+(empty_index+1)*a)//2,(y+y+a)//2)
        c.coords(f's{empty_index}',(x+(index_clicked)*a+x+(index_clicked+1)*a)//2,(y+y+a)//2)
        c.itemconfig(f's{index_clicked}',tag=f's{empty_index}') #tu prehadzujem clicked na empty
        c.itemconfig(f's{empty_index}',tag=f's{index_clicked}') #a tu zase empty na clicked ==> nic nemenim
        empty_index = (event.x-20)//a

c.bind("<Button-1>",select)

tkinter.mainloop()