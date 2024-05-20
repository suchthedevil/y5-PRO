"""
<space> -> starts the game
type letters on the keyboard to reveal the word
"""

import tkinter
c = tkinter.Canvas(height=600, width=900)
c.pack()

words = ['jozef','jano','tomas lamlech']

x, y = 450, 300
i = 0
revealed = ''

def start(e):
    c.delete('all')
    global x, y, i, word, revealed
    word = words[i % len(words)]
    revealed = ' ' * len(word)
    i += 1
    x -= (len(word) / 2) * (40 + 10)
    for k, l in enumerate(word):
        if l != " ":
            c.create_rectangle(x, y - 20, x + 40, y + 20, fill='cyan')
            c.create_text(x + 20, y, text=l, fill='cyan', tag=f'l{k}')
        else:
            x += 40
        x += 40 + 10
    x, y = 450, 300

def show(e):
    global i, word, revealed
    indexes = []
    for a, j in enumerate(word):
        if e.char == j:
            indexes.append(a)
    for index in indexes:
        revealed = revealed[:index] + e.char + revealed[index + 1:]
        if revealed == word:
            c.itemconfig(f'l{index}', fill='black')
            c.update()
            c.after(300,start(e))
        else:
            c.itemconfig(f'l{index}', fill='black')           

c.bind_all('<Key>', show)
c.bind_all('<space>', start)

tkinter.mainloop()