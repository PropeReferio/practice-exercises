# 7-4 Python Crash course Pizza Toppings: Write a loop that prompts 
# the user to enter a 
# series of pizza toppings until they enter a 'quit' value . As they 
# enter each topping, print a message saying you’ll add that topping 
# to their pizza.

active = True

available_toppings = ["Pepperoni", "Sausage", "Extra Cheese", 
"Soyrizo", "Banana Peppers", "Olives", "Garlic", "Pineapple"]
print("Welcome to our pizza joint! The following toppings are "
"available for you, and you can choose up to five toppings: ")
for topping in available_toppings:       # Shows a list of available toppings
    print(topping)

toppings = []
next_topping = (input("What would you like on your pizza? "))
if next_topping in available_toppings: # Ensures the user selection is available
    toppings.append(next_topping)
else:
    print("Sorry, that topping isn't available.")

while active == True:
    if len(toppings) >= 5:   # Causes the loop to end once user has selected 5 toppings
        print("That's 5 toppings!")
        active = False
        break
    next_topping = input("What else would you like? Type 'done' when you're ready. ")
    if next_topping == "done":   # Enables the user to exit the prompt cycle while loop
        break    
    elif next_topping in available_toppings: # Ensures the user selection is available
        toppings.append(next_topping)
    else:
        print("Sorry, that topping isn't available.")
    
print("One pizza coming right up, with these ingredients:") # Prints the users order
for topping in toppings:
    print(topping)