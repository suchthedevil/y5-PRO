nazov = input("Zadajte nazov: ")

with open(nazov, "r", encoding="utf8") as subor:
    n = 0
    najdlhsi = 0
    for riadok in subor:
        n += 1
        dlzka = len(riadok)
        if dlzka > najdlhsi:
            najdlhsi = dlzka

print(f'meno suboru: {nazov}\npocet riadkov suboru: {n}\nnajdlhsi ma {najdlhsi} znakov')