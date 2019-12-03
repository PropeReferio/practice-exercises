# Python Crash Course 7-8. Deli: Make a list called sandwich_orders 
# and fill it with the names of various sandwiches . Then make an 
# empty list called finished_sandwiches . Loop through the list of 
# sandwich orders and print a message for each order, such as I made 
# your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches . After all the sandwiches have been 
# made, print a message listing each sandwich that was made . 

orders = ["Tuna Melt", "Pastrami", "Sloppy Joes", "Pastrami", "Muffaletta", 
    "Philly Cheese Steak", "Pastrami", "BLT", "PB&J",]
print("You ordered the following:")
for sandwich in orders: #Lists the customers order
    print(sandwich)

print("Sorry, but we're out of pastrami! We'll make the other sandwiches.")
while "Pastrami" in orders: #removes all pastrami
    orders.remove("Pastrami")

completed_sandwiches = []

while orders:
    for sandwich in orders:
        current_sandwich = orders.pop()           # Removes sandwiches from list of orders, 
        completed_sandwiches.append(current_sandwich)  #adds it to completed list,
        print(f"I made your {current_sandwich}.") #and prints a message about it.

print("Your order's ready. Here they are:")
for sandwich in completed_sandwiches:
    print(sandwich)

