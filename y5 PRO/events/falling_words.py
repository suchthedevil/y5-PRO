import tkinter,random
h,w = 600,900
c = tkinter.Canvas(height=h,width=w)
c.pack()
letter = " "
words = ['jablko', 'programovanie', 'koleso','picka','bejbi', 'uloha', 'riesenie'] 
def key_pressed(e):
    global letter
    letter = e.char

game_end = True
def click(e):
    global word,text,id,letter,k,game_end
    if game_end:
        c.delete('all')
        game_end = False
        k = 0
        word = words[k]
        text = "*"*len(word)
        id = c.create_text(w//2,30,text=text,font="Helvetica 20")
        timer()

def timer():
    global word,text,id,letter,k,game_end,r
    if letter in word:
        i = []
        for p,l in enumerate(word):
            if l == letter:
                i.append(p)
        for index in i:
            c.itemconfig(id,text=text[:index]+letter+text[index+1:])
            text=text[:index]+letter+text[index+1:]
    else:
        c.move(id,0,30)
    if text != word:
        c.move(id,0,5)
        if c.coords(id)[1] > h-5:
            c.delete(id)
            c.create_text(w//2,h//2,text="You lost!", font="Helvetica 40", fill='red')
            game_end = True
    else:
        k += 1
        if k == len(words):
            c.delete(id)
            c.create_text(w//2,h//2,text="You won!", font="Helvetica 40", fill='lime')
            game_end = True
        else:
            letter = " "
            word = words[k]
            text = "*"*len(word)
            id = c.create_text(w//2,30,text=text,font="Helvetica 20")
            c.delete(id-1)
    c.after(200,timer)

c.bind_all('<Key>',key_pressed)
c.bind('<1>',click)
tkinter.mainloop()