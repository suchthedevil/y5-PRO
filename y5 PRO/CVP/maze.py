import tkinter
with open('CVP/bludiska.txt','r') as f:
    mapy = {}
    for line in f:
        if ":" in line:
            line = line.split("\t")
            mapy[int(line[0][0])] = [[int(x) for x in line[1].strip().split()]]
            number = int(line[0][0])
        else:
            mapy[number].append([int(x) for x in line.strip().split()])

r = 30
w, h = len(mapy[number][0]), len(mapy[number])
x, y = 35,35
c = tkinter.Canvas(width=w*2*r+10, height=h*2*r+10)
c.pack()

number = 2
for i, line in enumerate(mapy[number]):
    x = 35
    for j, ake in enumerate(line):
        id = c.create_rectangle(x-r,y-r,x+r,y+r, fill='white', tag=f's{i}{j}')
        if ake == 0:
            c.itemconfig(id,fill='black')
        if ake == 2:
            start = (i,j)
            c.itemconfig(id, fill='green')
        if ake == 3:
            finish = (i,j)
            c.itemconfig(id, fill='red')
        x += 2*r
    y += 2*r

solution = [start]
solutions = [[start]]
win = False
field = mapy[number]
row, col = start
while not win:
    for dy,dx in (-1,0), (1,0), (0,-1), (0,1):
        if (0 <= row+dy < len(field)-1) and (0 <= col+dx < len(field[0])):
            #print(col+dx, row+dy)
            if field[row+dy][col+dx] == 1:
                if (row+dy,col+dx) not in solution:
                    row, col = row+dy, col+dx
                    solution.append((row,col))
                    c.itemconfig(f's{row}{col}', fill='yellow')
            elif field[row+dy][col+dx] == 3:
                row, col = row+dy, col+dx
                solution.append((row,col))
                win = True
    c.after(100)
    c.update()

        
    
tkinter.mainloop()