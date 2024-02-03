import json
import matplotlib.pyplot as plt

file = open("CVP/CSV files/faktury_BB.json", 'r', encoding="utf8")
data = json.load(file)
file.close()
subject_per_year = {}

for entry in data:
    year = entry['Dátum_vystavenia'].split('.')[2]
    cena = abs(float(entry['Celková_cena'].replace(" ", "").replace(",", ".")))
    if entry['IČO'] in subject_per_year:
        if year in subject_per_year[entry['IČO']]:
            subject_per_year[entry['IČO']][year][int(str(cena)[0])-1] += 1
        else:
            subject_per_year[entry['IČO']][year] = [0]*9
            subject_per_year[entry['IČO']][year][int(str(cena)[0])-1] += 1
    else:
        subject_per_year[entry['IČO']] = {year: [0]*9}
        subject_per_year[entry['IČO']][year][int(str(cena)[0])-1] += 1


def plot_graph(ico, year):
    plt.bar([1,2,3,4,5,6,7,8,9],subject_per_year[ico][year])
    plt.show()

plot_graph('30204330   ','2022')
