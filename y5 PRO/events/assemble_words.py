import tkinter, random

c = tkinter.Canvas(height=500,width=800)
c.pack()
overlaps = []
check = [0]
words = ['koza','olovo']
word = 'olovo'
x,y = 200,150
for i in range(len(word)):
    c.create_rectangle(x,y,x+50,y+50, fill='cyan')
    x += 55
    tx,ty = random.randrange(50,750), random.randrange(50,450)
    c.create_text(tx,ty,text=word[i], font="Arial 20")
#tag=f"{word[i]}{i}"
def klik(e):
    global dx, dy, letter, tagl
    dx,dy = None, None
    letter = c.bbox('current')
    tagl = c.find_withtag('current')
    #tag2 = c.gettags(tagl[0])
    dx,dy = e.x-letter[0], e.y-letter[1]
    c.lift(tagl)
    c.itemcget(tagl,'text')

#vytovrit string s n prazdnymi vecami, menit pismena podla tahania
pismena = word.split()
def tahanie(e):
    global count
    sur = letter
    if dx != None:
        sirka, vyska = abs(sur[0]-sur[2]), abs(sur[1]-sur[3])
        c.coords(tagl, e.x-dx+sirka,e.y-dy+vyska)
    for i in range(1,len(word)*2+1,2):
        stv_sur = c.coords(i)
        overlap = c.find_overlapping(stv_sur[0],stv_sur[1],stv_sur[2],stv_sur[3])
        if len(overlap) == 2 and overlap not in overlaps:
            overlaps.append(overlap)
            if overlap[0] == overlap[1]-1 and overlap[0] == check[-1]+1:
                check.append(overlap[0])
                check.append(overlap[1])
    if len(check) == 1+2*len(word):
        c.create_text(300,300,text="Hotovo!", font="Arial 20")
    #print(check)

def released(e):
    pass
c.bind('<1>', klik)
c.bind('<B1-Motion>',tahanie)
c.bind('<ButtonRelease>',released)

tkinter.mainloop()