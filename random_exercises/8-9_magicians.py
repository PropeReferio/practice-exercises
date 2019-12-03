#8-9. Magicians: Make a list of magician’s names . Pass the list to a 
#function called show_magicians(), which prints the name of each magician 
# in the list . 8-10. Great Magicians: Start with a copy of your program from
# Exercise 8-9 . Write a function called make_great() that modifies the list 
# of magicians by adding the phrase the Great to each magician’s name . Call 
# show_magicians() to see that the list has actually been modified . 8-11. 
# Unchanged Magicians: Start with your work from Exercise 8-10 . Call the 
# function make_great() with a copy of the list of magicians’ names . 
# Because the original list will be unchanged, return the new list and store
#  it in a separate list . Call show_magicians() with each list to show that 
# you have one list of the original names and one list with the Great added to
#  each magician’s name .

names = ['angel', 'Raziel', 'Metatron']
great_names = []

def show_magicians(magicians):
    for name in magicians:
        print(name.title())

def make_great(magicians):
    while magicians:
        great = magicians.pop()
        great += " the great"
        great_names.append(great)
    

make_great(names[:])
show_magicians(great_names)
show_magicians(names)