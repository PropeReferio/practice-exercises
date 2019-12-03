# Python Crash Course 8-5. Cities: Write a function called describe_city() 
#that accepts the name of a city and its country . The function should print
#a simple sentence, such as Reykjavik is in Iceland . Give the parameter for 
#the country a default value . Call your function for three different cities, 
#at least one of which is not in the default country .

def describe_city(name, nation = "Murica"):
    print(f"{name} is in {nation}.")

describe_city("Nashville")
describe_city("Sevilla", "Spain")
describe_city(nation = "Turkey", name = "Istanbul")