otazka = str(input())
ne, ostatne = otazka.split("-")

pocet_ne = ne.count("ne")

if pocet_ne%2 == 0:
    print("ano")
else:
    print("nie")
