import game

""" Requires Python 3.10+ """

def main():
    
    print ("Let's play Rock, Paper, Scisscors!")
    
    def matchCase():
        # Run Match Case
        match player:
            case game.option1:
                print("It's a tie!")
            case game.option2:
                print("You Loose!")
            case game.option3:
                print("You Loose!")
            case game.option4:
                print("You Loose")
            case game.option5:
                print("You Win")
            case game.option6:
                print("You Win")
            case game.option7:
                print("You Win")

    while not game.player:
        # Set player to True
        game.player = input("Rock, Paper, Scissors? ")
        if game.player == True:
            matchCase()
        else:
            print("Invalid Input!") 

if __name__ == "__main__":
    main()