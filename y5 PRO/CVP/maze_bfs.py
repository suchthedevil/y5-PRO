import tkinter
with open('y5 PRO/CVP/bludiska.txt','r') as f:
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
            print(finish)
            c.itemconfig(id, fill='red')
        x += 2*r
    y += 2*r


win = False
field = mapy[number]
visited, queue= [start], [start]
bfs_path = {}
while not win and queue:
    node  = queue.pop(0)
    for dy,dx in (0,1),(0,-1),(1,0),(-1,0):
        row, col = node[0]+dy, node[1]+dx
        if row >= 0 and col >= 0:
            next_node = (row,col)
            try:
                if field[row][col] == 3:
                    bfs_path[next_node] = node 
                    win = True
                elif field[row][col] == 1 and next_node not in visited:
                    queue.append(next_node)
                    visited.append(next_node)
                    bfs_path[next_node] = node        #create an adjacency list (dictionary)
            except: IndexError           
node = finish
solution = [finish]
while node != start:
    solution.insert(0,bfs_path[node])
    node = bfs_path[node]
solution.remove(start)
solution.remove(finish)
print(solution)
for n in solution:
    c.itemconfig(f's{n[0]}{n[1]}', fill='yellow')
    c.after(100)
    c.update()       
tkinter.mainloop()