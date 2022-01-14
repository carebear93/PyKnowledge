from random import randint

# Create a list of play options
weapon = ["Rock", "Paper", "Scissors"]

# Assign a random play to the computer
computer = weapon[randint(0, 2)]

# Player set to False
player = False

# List all game scenarios
option1 = player == computer
option2 = player == "Rock", computer == "Paper"
option3 = player == "Paper", computer == "Scissors"
option4 = player == "Scissors", computer == "Rock"
option5 = player == "Rock", computer == "Scissors"
option6 = player == "Scissors", computer == "Paper"
option7 = player == "Paper", computer == "Rock"