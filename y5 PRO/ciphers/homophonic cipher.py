import random
def sifruj(name):
    with open(name, 'r', encoding='utf8') as f:
        text = f.read()
    with open('y5 PRO/ciphers/homoph.txt', 'r', encoding='utf8') as b:
        key = {}
        for line in b:
            key[line.split()[0][0]] = line.split()[1:]

    result = ''
    for char in text:
        if 'A' <= char.upper() <= 'Z':
            n = random.choice(key[char.upper()])
        else:
            n = char
        result += n
    print(result)

def desifruj(name):
    with open(name, 'r', encoding='utf8') as f:
        text = f.read()
    with open('y5 PRO/ciphers/homoph.txt', 'r', encoding='utf8') as b:
        key = {}
        for line in b:
            key[line.split()[0][0]]=  line.split()[1:]

    result = ''
    c = 0
    while c != len(text)-1:
        if "0" <= text[c] <= "9":
            pair = text[c:c+2]
            c += 2
            for k,l in key.items():
                if pair in l:
                    letter = k
        else:
            letter = text[c]
            c += 1
        result += letter
    print(result)

sifruj('y5 PRO/ciphers/sifruj.txt')
desifruj('y5 PRO/ciphers/desifruj.txt')
