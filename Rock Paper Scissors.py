import random
options =("rock","paper","scissors")
running = True

while running:
    player ="none"
    computer=random.choice(options)


    while player not in options:
        player = input("Enter a choice(rock,paper,scisser):")
        print(f"player:{player}")
        print(f"computer:{computer}")

        if player == computer:
            print("It's a tie!")

        elif player == "rock" and computer =="scisser":
            print("you win")
            

        elif player == "paper" and computer =="rock":
            print("you win")
            
        elif player =="scissors" and omputer =="paper":
            print("you win")

        if not input("player agine?(yes/no):").lower()=="yes":
                     running =False
                     print("Thanks for panning!")
