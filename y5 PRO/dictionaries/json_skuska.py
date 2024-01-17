import json

student1 = {
    'meno': 'Janko Hrasko',
    'adresa': {'ulica': 'Strukova',
               'cislo': 13,
               'obec': 'Fazulovo'},
    'narodeny': {'datum': {'den': 1, 'mesiac': 5, 'rok': 1999},
                 'obec': 'Korytovce'}
}
student2 = {
    'meno': 'Juraj Janosik',
    'adresa': {'ulica': 'Pod sibenicou',
               'cislo': 1,
               'obec': 'Liptovsky Mikulas'},
    'narodeny': {'datum': {'den': 25, 'mesiac': 1, 'rok': 1688},
                 'obec': 'Terchova'}
}
student3 = {
    'meno': 'Margita Figuli',
    'adresa': {'ulica': 'Sturova',
               'cislo': 4,
               'obec': 'Bratislava'},
    'narodeny': {'datum': {'den': 2, 'mesiac': 10, 'rok': 1909},
                 'obec': 'Vysny Kubin'}
}
student4 = {
    'meno': 'Ludovit Stur',
    'adresa': {'ulica': 'Slovenska',
               'cislo': 12,
               'obec': 'Modra'},
    'narodeny': {'datum': {'den': 28, 'mesiac': 10, 'rok': 1815},
                 'obec': 'Uhrovec'}
}

skola = [student1, student2, student3, student4]

with open("dictionaries/subor.json", 'w') as subor:
    json.dump(skola, subor, indent=2)
