# Python Crash Course 6-9. Favorite Places: Make a dictionary called favorite_places.
# Think of three names to use as keys in the dictionary, and store one to three 
# favorite places for each person . To make this exercise a bit more interesting, 
# ask some friends to name a few of their favorite places . Loop through the 
# dictionary, and print each person’s name and their favorite places . 
wfave = ['thailand', 'bahamas', 'south florida']
hfave = ['jupiter', 'kanakuk',]
lfave = ['nashville', 'linville', 'alaska']
jfave = ['toadsuck']

fave_places = {'wendy' : wfave, 'haley' : hfave, 'lem' : lfave, 'simple john' : jfave}

for person, fave in fave_places.items():
    if len(fave) == 3:
        print(person.title() + "'s favorite places are " + fave[0].title() + ", " + fave[1].title() + ", and " + fave[2].title() + ".")
    elif len(fave) == 2:
        print(person.title() + "'s favorite places are " + fave[0].title() + ", and " + fave[1].title() + ".")
    elif len(fave) == 1:
        print(person.title() + "'s favorite place is " + fave[0].title() + ".")
