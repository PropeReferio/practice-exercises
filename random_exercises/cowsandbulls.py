# Exercise 18 from practicepython.org

import random
secret = list(str(random.randint(1000,10000))) # This is the number to guess

def cowbull():
    guess = list(input("Guess a 4-digit number!"))
    bulls = 0
    cows = 0
    count = 0
    while count <= 3:
        if guess[count] in secret:
            if guess[count] == secret[count]:
                bulls += 1
            else:
                cows += 1
        count += 1

    if bulls == 4:
        print("Congrats, you guessed it!")
    else:
        print("You have {} cows and {} bulls.".format(cows, bulls))
        cowbull()


cowbull()