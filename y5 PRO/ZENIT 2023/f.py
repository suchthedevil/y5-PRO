n = int(input())
table = []
for i in range(n):
    line = input()
    table.append(line)

def is_solution(a):
    if "TINEZ" in a or "ZENIT" in a:
        return True
    return False

#zvisly smer

for i in range(n):
    text = ""
    for j in range(n):
        text += table[j][i]
    if is_solution(text):
        print("OK")
        exit()

#vodorovny smer
for word in table:
    if "ZENIT" in word or "TINEZ" in word:
        print("OK")
        exit()

#diagonaly (-_)
for i in range(n):
    text = ""
    for j in range(n-i):
        text += table[i+j][j]
    """
    if is_solution(text):
        print("OK")
        exit()
    """
    text = ''
    for j in range(n-i):
        text += table[j][i+j]
    """
    if is_solution(text):
        print("OK")
        exit()
    """
#diagonaly (_-)
for i in reversed(range(n-1)):
    text = ''
    for j in range(i+1):
        text += table[i-j][j]
    text = ''

c = 0  
for i in reversed(range(n)):
    c += 1
    for j in range(n-i-1,n):
        print(n-c,j)
        c += 1
    print()
        
