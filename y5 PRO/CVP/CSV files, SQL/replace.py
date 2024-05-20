text = '("Chupa Chups";"Strawberry";"5";"20"),("Chupa Chups";"Green Apple";"5";"20"),("Airwaves";"Cool Oasis";"10";"9"),("Orbit";"Hovno";"10";"20"),("Jetgum";"picka";"10";"20")'
while ";" in text:
    text = text.replace(";",",")
print(text)