#8-12. Sandwiches: Write a function that accepts a list of items a person 
#wants on a sandwich . The function should have one parameter that collects 
#as many items as the function call provides, and it should print a summary 
#of the sandwich that is being ordered . Call the function three times, 
#using a different number of arguments each time . 

def menu_item(name, *ingreds):
    """Prints a statement about additions to a menu."""
    print("We have a new menu item: " + name + "! It comes with the"
    " following:")
    for ingred in ingreds:
        print(ingred)

menu_item("Lobster", "Lobster", "Butter", "Lemon")
menu_item("Chocolate Cake", "Cake", "Ice Cream")