def zostupne(zoz):
    prev = zoz[0]
    for i in range(1,len(zoz)):
        if prev < zoz[i]:
            return False
    return True
    
print(zostupne([5, 4, 6, 1, 0, 0]))
