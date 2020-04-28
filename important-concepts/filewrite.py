import csv

#Might need to use a dictionary if I want headers
with open('fruits.csv', mode='w') as fruit_file:
    fieldnames = ['Type', 'Region', 'Season']
    writer = csv.DictWriter(fruit_file, fieldnames=fieldnames)

    writer.writeheader() #These are the fieldnames
    writer.writerow({'Type': 'Apple', 'Region': 'Georgia', 'Season': 'Summer'})
    writer.writerow({'Type': 'Papaya', 'Region': 'Guacamelee', 'Season': 'All Year'})
    #This is overwriting the file each time the program is run.