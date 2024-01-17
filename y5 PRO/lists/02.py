"""
def mocniny(n):
    zoz = []
    for i in range(1,n+1):
        zoz.append(i**2)
    print(zoz)


mocniny(7)
"""
def mocniny(n):
    return [x**2 for x in range(1,n+1)]
    