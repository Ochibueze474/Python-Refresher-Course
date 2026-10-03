# Rock, Paper and Scissors Game

import random

options = ("Rock", "Paper", "Scissors")
running = True

while running:

    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter players choice (Rock, Paper, Scissors): ").capitalize()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a Tie!")
    elif player == "Rock" and computer == "Scissors":
        print("You win!")
    elif player == "Paper" and computer == "Rock":
        print("You win!")
    elif player == "Scissors" and computer == "Paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (yes/no): ").lower()
    if not play_again == "yes":
        running = False

print("Thanks for playing")

    