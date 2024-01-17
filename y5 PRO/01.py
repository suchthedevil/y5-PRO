aky = input('Zadaj meno suboru: ')

with open(aky, "r", encoding="utf8") as subor:
    text = subor.read()

print(text)