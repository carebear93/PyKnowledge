from random import randint


def main():
    # Create a list of play options
    weapon = ["Rock", "Paper", "Scissors"]

    # Assign a random play to the computer
    computer = weapon[randint(0, 2)]

    # Set player to False
    player = False

    # List all game scenarios
    option1 = player == computer
    option2 = player == "Rock", computer == "Paper"
    option3 = player == "Paper", computer == "Scissors"
    option4 = player == "Scissors", computer == "Rock"
    option5 = player == "Rock", computer == "Scissors"
    option6 = player == "Scissors", computer == "Paper"
    option7 = player == "Paper", computer == "Rock"

    def matchCase():
        match player:
            case option1:
                print("It's a tie!")
            case option2:
                print("You Loose!")
            case option3:
                print("You Loose!")
            case option4:
                print("You Loose")
            case option5:
                print("You Win")
            case option6:
                print("You Win")
            case option7:
                print("You Win")

    while not player:
        # Set player to True
        player = input("Rock, Paper, Scissors?")
        if player == True:
            matchCase()
        else:
            print("Invalid Input!")

    # Player was set to True, but we want it to be False so the loop continues
    player = False
    computer = weapon[randint(0, 2)]


if __name__ == "__main__":
    main()
