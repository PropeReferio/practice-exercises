# EX 6-5 from Python Crash Course

rivers = {
    'Amazon' : 'Brazil',
    'Mississippi' : "Murica",
    'Ganges' : 'India',
    'Nile' : 'Egypt',
    'Thames' : 'England'
    }

for river, country in rivers.items():
    print("The " + river + " runs through " + country + ".")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)