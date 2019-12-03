import random
number, guess = random.randint(1,10), 0

while guess != number:
    guess = int(input("Guess how many fingers I'm holding up behind my back!"))
    if guess != number:
        print("Nope!")
    
    
print("Good Guess!")

