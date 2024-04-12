dungeon = [
'S..#...',
'.#...#.',
'.#.....',
'..##...',
'#.#E.#.']

def BFS(d):
    start = (0,0)
    child_cell = (0,0)
    end = (4,3)
    explored = [start]
    queue = [start]
    path_dic = {}
    while len(queue) != 0:
        curr_cell = queue.pop(0)
        if curr_cell == end:
            break
        for dx,dy in (0,1),(1,0),(0,-1),(-1,0):
            try:
                row, col = curr_cell[0]+dy, curr_cell[1]+dx
                if row >= 0 and col >= 0:
                    child_cell = (row,col)
                    if child_cell not in explored and d[row][col] == "." or d[row][col] == "E":
                        queue.append(child_cell)
                        explored.append(child_cell)
                        path_dic[child_cell] = curr_cell
            except: IndexError
    print(path_dic)
    cell = end
    path = {}
    while cell != start:
        path[path_dic[cell]] = cell
        cell = path_dic[cell]
    solution = []
    for key, value in path.items():
        if value not in solution:
            solution.append(value)
        if key not in solution:
            solution.append(key)
    print(solution)

        



BFS(dungeon)
