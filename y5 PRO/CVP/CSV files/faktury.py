import json
import matplotlib.pyplot as plt

file = open("CVP/CSV files/faktury_BB.json", 'r', encoding="utf8")
data = json.load(file)
file.close()
subject_per_year = {}
benford_distributoion = [0.301, 0.176, 0.123, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

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
    if year == 'all':
        years_occurence = [0]*9
        for c in subject_per_year[ico].values():
            for i in range(9):
                years_occurence[i] += c[i]
    else:
        years_occurence = subject_per_year[ico][year]
    plt.bar([1,2,3,4,5,6,7,8,9],years_occurence)
    plt.show()
    
def find_deviation(ico):
    dev = 0
    years_occurence = [0]*9
    for c in subject_per_year[ico].values():
        for i in range(9):
            years_occurence[i] += c[i]
    if 0 not in years_occurence:
        real_distribution = [i/sum(years_occurence) for i in years_occurence]
        for i in range(9):
            dev += abs(real_distribution[i] - benford_distributoion[i])
    return dev

deviations = {}
for ico in subject_per_year.keys():
    deviations[ico] = find_deviation(ico)

deviations_sorted = dict(sorted(deviations.items(), key=lambda x: x[1]))
    
for i in range(10):
    print(deviations_sorted.popitem())

plot_graph('00416045   ', 'all')
