import random, tkinter
def dve_kocky(n):
    ft = {}
    freq = [0]*12
    for i in range(n):
        k1 = random.randrange(1,7)
        k2 = random.randrange(1,7)
        sucet = k1+k2
        freq[sucet-1] += 1
    for i,s in enumerate(freq):
        ft[f'{i+2}'] = freq[i]
    print(ft)
    
dve_kocky(1000)

c = tkinter.Canvas(height=600, width=800)
c.pack()

def tri_kocky(n):
    fr = [0]*16
    for i in range(n):
        sums = sum([random.randrange(1,7),random.randrange(1,7),random.randrange(1,7)])
        fr[sums-3] += 1
    print(fr)

    x,y = 10,550
    c.create_line(x,y,x+15*(40+10)+40,y)
    for i,j in enumerate(fr):
        c.create_text(x+20,y+20, text=i+3, font='Arial 15')
        c.create_rectangle(x,y,x+40,y-2*j,fill='red')
        x += 40+10

tri_kocky(1500)
tkinter.mainloop()