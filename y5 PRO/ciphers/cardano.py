import tkinter

c = tkinter.Canvas(height=800, width=800)
c.pack()

with open('y5 PRO/ciphers/cardano_source.txt', 'r', encoding='utf8') as f:
    matrix = []
    key = []
    matrix2 = []
    for line in f:
        if line == '\n':
            break
        else:
            matrix.append(line.strip())
    for line in f:
        key.append(line.strip())

with open('y5 PRO/ciphers/cardano_source.txt', 'r', encoding='utf8') as f:
    for line in f:
        if line == '\n':
            break
        else:
            matrix2.append(line.strip())
print(matrix2)


for a in range(2):
    x,y = 40,40
    for i,row in enumerate(matrix):
        for j,letter in enumerate(row):
            if key[i][j] == '1':
                c.create_rectangle(x,y,x+40,y+40,)
                c.create_text(x+20,y+20,text=letter)
            else:
                c.create_rectangle(x,y,x+40,y+40, fill='blue')
            x += 40
        y += 40
        x = 40




tkinter.mainloop()