def solve_word_search(source_file):
    with open(source_file, encoding="utf8") as f:
        words, word_grid, grid = [], [], []
        out = ""
        for line in f:
            if line == "\n":
                break
            words.append(line.rstrip())
        for line in f:
            if line == "\n":
                break
            word_grid.append(line.rstrip())
        h = len(word_grid)
        l = len(word_grid[0])
        for i in range(h):
            grid.append([0]*l)
        for line in f:
            if line[0].isnumeric():
                spaces = line.rstrip()
            else:
                out += line
        #rows
        for w in words:
            for i,line in enumerate(word_grid):
                if w in line:
                    start_index = line.index(w)
                    grid[i][start_index:start_index+len(w)] = [1]*len(w)
                if w[::-1] in line:
                    start_index = line.index(w[::-1])
                    grid[i][start_index:start_index+len(w[::-1])] = [1]*len(w[::-1])
        #columns
        for w in words:
            for i in range(l):
                column = ""
                for j,line in enumerate(word_grid):
                    column += word_grid[j][i]
                if w in column:  
                    start_index = column.index(w)
                    for k in range(start_index,start_index+len(w)):
                        grid[k][i] = 1
                if w[::-1] in column:
                    start_index = column.index(w[::-1])
                    for k in range(start_index,start_index+len(w[::-1])):
                        grid[k][i] = 1
        #diagonals
        diag_letters, diag_letters_2 = {}, {}
        diag_indexes, diag_indexes_2 = {}, {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i-j in diag_letters:
                    diag_letters[i-j] += word_grid[i][j]
                    diag_indexes[i-j].append([i,j])
                else:
                    diag_letters[i-j] = word_grid[i][j]
                    diag_indexes[i-j] = [[i,j]]
                if i+j in diag_letters_2:
                    diag_letters_2[i+j] += word_grid[i][j]
                    diag_indexes_2[i+j].append([i,j])
                else:
                    diag_letters_2[i+j] = word_grid[i][j]
                    diag_indexes_2[i+j] = [[i,j]]

        def diagonals(diag,indexes):
            for d in diag.items():
                for w in words:
                    if w in d[1]:   
                        start_index = d[1].index(w)
                        for k in range(start_index,start_index+len(w)):
                            index = indexes[d[0]][k]
                            grid[index[0]][index[1]] = 1
                    elif w[::-1] in d[1]:  
                        start_index = d[1].index(w[::-1])
                        for k in range(start_index,start_index+len(w[::-1])):
                            index = indexes[d[0]][k]
                            grid[index[0]][index[1]] = 1
           
        diagonals(diag_letters,diag_indexes)
        diagonals(diag_letters_2,diag_indexes_2)
        solved = ""
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    solved += word_grid[i][j]
        s = 0
        for i in spaces:
            out += solved[s:s+int(i)] + " "
            s += int(i)
        print(out)
solve_word_search("projekt_CVP/osemsmerovka 12x12.txt")