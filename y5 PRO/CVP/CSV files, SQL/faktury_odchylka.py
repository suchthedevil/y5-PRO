import json

ceny = []
file = open("CVP/CSV files/faktury_BB.json", 'r', encoding="utf8")
data = json.load(file)
file.close()

data2 = {}
for entry in data:
    data2[entry['IČO']] = {'meno': entry['Dodávateľ'], 'rok': entry['Dátum_vystavenia'].split('.')[2]}
    data2['Celková_cena'] = entry['Celková_cena']

