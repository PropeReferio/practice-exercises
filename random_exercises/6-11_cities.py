# Ex 6-11 Cities Python Crash Course: Make a dictionary called cities . Use 
# the names of three cities as keys in your dictionary . Create a dictionary 
# of information about each city and include the country that the city is in, 
# its approximate population, and one fact about that city . The keys for each 
# city’s dictionary should be something like country, population, and fact . 
# Print the name of each city and all of the information you have stored about it . 

nash_info = {
    'nation' : 'the united states',
    'pop' : 2000000,
    'fact' : 'the country music capital of the world',
}

bogo_info = {
    'nation' : 'colombia',
    'pop' : 8000000,
    'fact' : 'named after an ancient goddess',
}

chic_info = {
    'nation' : 'the united states',
    'pop' : 5000000,
    'fact' : 'the city of the big shoulders',
}

cities = {'nashville' : nash_info, 'bogota' : bogo_info, 'chicago' : chic_info}

for name, info in cities.items():
    print(name.title() + ' is a city in ' + info['nation'].title() + ', with approximately ' + 
    str(info['pop']) + ' people living there. Did you know that ' + info['nation'].title() + 
    ' is ' + info['fact'] + "?")