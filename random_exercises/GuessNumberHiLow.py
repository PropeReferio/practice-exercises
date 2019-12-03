# From Intro to Python Crash Course, Eric Matthes

def guess():
    print("I'm thinking of a number between 1 and 99.")
    import random
    num = random.randint(1,100)
    g = int(input("Guess!"))
    while g != num:
        if g > num:
            print("Nope, you're too high! Try again.")
        else:
            print("Nope, too low! Try again.")
        g = int(input("Guess!"))
    again = input("Great guess! Want to play again?")
    while again != "yes" or "no":
        again = input("What did you say?")
    if again == "yes":
        guess()
    elif again == "no":
        print("Thanks for playing!")

guess()