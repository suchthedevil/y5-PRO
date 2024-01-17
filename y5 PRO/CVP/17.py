"""
import random
def kocka(pocet):
    zoz = 6*[0]
    for i in range(100):
        c = random.randrange(5)
        zoz[c] += 1
    print(zoz)

kocka(100)
"""
