#  Python Crash Course 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers .
# Think of five names, and use them as keys in your dictionary . Think of a 
# favorite number for each person, and store each as a value in your dictionary . 
# Print each person’s name and their favorite number . For even more fun, poll
# a few friends and get some actual data for your program . 
# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102)
# so each person can have more than one favorite number . 
# Then print each person’s name along with their favorite numbers . 

hfave = [4, 10]
cfave = [3, 9]
jfave = [1, 6, 9]
lfave = [7, 13]
bfave = [6, 4, 2, 1]
fave_numbs = {'helen' : hfave, 'claudia' : cfave, 'john' : jfave, 'lem' : lfave, 'bo' : bfave}

for num in fave_numbs.values():  
    num.sort()         # Sorts all lists of favorite numbers in ascending numerical order.

for name, num in sorted(fave_numbs.items()):                  # Prints statements about each persons favorite numbers.
    if len(num) == 2:
        print(name.title() + "'s favorite numbers are " + str(num[0]) + " and " + str(num[1]) + ".")
    if len(num) == 3:
        print(name.title() + "'s favorite numbers are " + str(num[0]) + ", " + str(num[1]) + ", and " + str(num[2]) + ".")
    if len(num) == 4:
        print(name.title() + "'s favorite numbers are " + str(num[0]) + ", " + str(num[1]) + ", " + str(num[2]) + ", and " + str(num[3]) + ".")