#Ex. 8 Practice Python Make a two-player Rock-Paper-Scissors game. (Hint: Ask 
#for player plays (using input), compare them, print out a message of 
#congratulations to the winner, and ask if the players want to start a new 
#game)

def rock(p2):
    if p2 == "scissors":
        print("Player 1 has rock, Player 2 has scissors. P1 Wins!")
    elif p2 == "paper":
        print("Player 1 has rock, Player 2 has paper. P2 Wins!")
    else:
        print("What did Player 2 throw? Try again!")
        rock_paper_scissors(input("Player 1, rock, paper, or scissors? "), input("Player 2, rock, paper, or scissors? "))
    again = input("Do you want to play again? (y/n) ")
    if again == "y":
        rock_paper_scissors(input("Player 1, rock, paper, or scissors? "), input("Player 2, rock, paper, or scissors? "))
    else:
        print("Thanks for playing!")

def paper(p2):
    if p2 == "scissors":
        print("Player 1 has paper, Player 2 has scissors. P2 Wins!")
    elif p2 == "rock":
        print("Player 1 has paper, Player 2 has rock. P1 Wins!")
    else:
        print("What did Player 2 throw? Try again!")
        rock_paper_scissors(input("Player 1, rock, paper, or scissors? "), input("Player 2, rock, paper, or scissors? "))
    again = input("Do you want to play again? (y/n) ")
    if again == "y":
        rock_paper_scissors(input("Player 1, rock, paper, or scissors? "), input("Player 2, rock, paper, or scissors? "))
    else:
        print("Thanks for playing!")

def scissors(p2):
    if p2 == "paper":
        print("Player 1 has scissors, Player 2 has paper. P1 Wins!")
    elif p2 == "rock":
        print("Player 1 has scissors, Player 2 has rock. P2 Wins!")
    else:
        print("What did Player 2 throw? Try again!")
        rock_paper_scissors(input("Player 1, rock, paper, or scissors? "), input("Player 2, rock, paper, or scissors? "))
    again = input("Do you want to play again? (y/n) ")
    if again == "y":
        rock_paper_scissors(input("Player 1, rock, paper, or scissors? "), input("Player 2, rock, paper, or scissors? "))
    else:
        print("Thanks for playing!")

def rock_paper_scissors(p1.lower(), p2.lower()):
    if p1 == p2:
        print("Tie! Try again!")
        rock_paper_scissors(input("Player 1, rock, paper, or scissors? "), input("Player 2, rock, paper, or scissors? "))
    elif p1 == "rock":
        rock(p2)
    elif p1 == "paper":
        paper(p2)
    elif p1 == "scissors":
        scissors(p2)
    else:
        print("What did P1 throw? Try again!")
        rock_paper_scissors(input("Player 1, rock, paper, or scissors? "), input("Player 2, rock, paper, or scissors? "))

rock_paper_scissors(input("Player 1, rock, paper, or scissors? "), input("Player 2, rock, paper, or scissors? "))
