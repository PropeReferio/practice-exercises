# Python Crash Course 6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
# name of a pet . In each dictionary, include the kind of animal and the owner’s 
# name . Store these dictionaries in a list called pets . Next, loop through your 
# list and as you do print everything you know about each pet . 

Bowser = {'name' : 'bowser', 'animal' : 'dog', 'owner' : 'Ashton Kutcher'}
Lizzie = {'name' : 'lizzie', 'animal' : 'gecko', 'owner' : 'Lem Stevens'}
Eragon = {'name' : 'eragon', 'animal' : 'dragon', 'owner' : 'Danearys'}

pets = [Bowser, Lizzie, Eragon]

for pet in pets:
    print(pet['name'].title() + " is a " + pet['animal'] + ", and their owner is " + pet['owner'] + ".")

