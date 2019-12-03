# Ex 5-10 of Python Crash Course

users = ["chris123", "blueeyeswhitedragon9", "Creep007", "Shinobiaznmaster", "Sariel"]
check_users = []
for name in users:   # Creates a list of all current users in lowercase, for checking for unique usernames
    check_users.append(name.lower())
new_users = ["Chris123", "crEEp007", "nerdybabe4", "ilovelamp", "notebookpioneer"]

for name in new_users:
    if name.lower() in check_users:          # Converts all new usernames to lowercase to check for uniqueness
        print(f"Sorry, {name} is already taken.")
    else:
        print(f"Cool {name}, you'll receive further instructions by email.")