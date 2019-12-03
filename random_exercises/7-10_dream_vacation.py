# 7-10. Dream Vacation: Write a program that polls users about their dream 
# vacation . Write a prompt similar to If you could visit one place in the 
# world, where would you go? Include a block of code that prints the results 
# of the poll .
active = True
poll_results = {}

while active == True:
    name = input("Hi, what's your name? ")
    dest = input("If you could go anywhere in the world, where would you "
            "go? ")
    poll_results[name] = dest
    again = input("Thanks for your response =] Would another person like "
            "to answer? (yes / no) ").lower()
    if again == "yes":
        continue
    if again == "no":
        active = False

print("Thanks to all who participated! The results are in:")
for name, dest in poll_results.items():
    print(f"{name} wants to go to {dest}!")