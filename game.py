import random
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("PLAYER_NAME", default="Player One")

print("Welcome " + username + " to Rock-Paper-Scissors...")
def main():
    choicel = []

    print()
    print("Rock, Paper or Scissors?")
    choice1 = input()
    choice1 = choice1.lower()
    choicel = list(choice1)
    choicel[0] = choicel[0].upper()
    output = "".join(choicel)


    comp = random.randint(1,3)
    if comp == 1:
        coutput = "Rock"
    elif comp == 2:
        coutput = "Paper"
    elif comp == 3:
        coutput = "Scissors"

    print()
    if choice1 == "rock":
        print("Your choice: "+output)
        print("Computer's choice: "+coutput)
        print()
        user = 1
        if comp == 1:
            print("Tie!")
        elif comp == 2:
            print("The computer won.")
        elif comp == 3:
            print("You won! Congrats.")
        print("Thanks for playing.")
    elif choice1 == "paper":
        print("Your choice: "+output)
        print("Computer's choice: "+coutput)
        print()
        user = 2
        if comp == 1:
            print("You won! Congrats.")
        elif comp == 2:
            print("Tie!")
        elif comp == 3:
            print("The computer won.")
        print("Thanks for playing.")
    elif choice1 == "scissors":
        print("Your choice: "+output)
        print("Computer's choice: "+coutput)
        print()
        user = 3
        if comp == 1:
            print("The computer won.")
        elif comp == 2:
            print("You won! Congrats.")
        elif comp == 3:
            print("Tie!")
        print("Thanks for playing.")
    else:
        print("Invalid input, please enter Rock, Paper or Scissors.")
    yn = input("Would you like to try again? [y] ")
    yn = yn.lower()
    if yn == "y":
        main()
main()
