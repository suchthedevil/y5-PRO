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
            start = [i,j]
            c.itemconfig(id, fill='green')
        if ake == 3:
            finish = (i,j)
            print(finish)
            c.itemconfig(id, fill='red')
        x += 2*r
    y += 2*r


win = False
field = mapy[number]
visited, curr_path= [start], [start]
bfs_path = {}
while not win and curr_path:
    node  = curr_path.pop(0)
    for dy,dx in (0,1),(0,-1),(1,0),(-1,0):
        row, col = node[1]+dy, node[0]+dx
        next_node = [row,col]
        try:
            if next_node not in visited and field[row][col] == 1:
                curr_path.append(next_node)
                visited.append(next_node)
                bfs_path[f"{next_node}"] = node
                print(bfs_path)
            elif field[row][col] == 3:
                win = True
        except: IndexError
print(bfs_path)
            
tkinter.mainloop()