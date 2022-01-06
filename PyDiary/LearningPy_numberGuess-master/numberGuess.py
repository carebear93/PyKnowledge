# Random Number Game
import random


# Introduce the game
print ("Welcome to the number guessing game")
# Get and Store use name in a var
name = input ("What is your name: ")
print ("Hi", name, " I am thinking of a number between 1-20, you have 5 chances to guess the number!")


# Create a varible that stores random number between 1, 20
number = random.randint(1,20)
print ("What number am I thinking of?")
#Guess starts at 0
guessTaken = 0

# While guess is less than 6
while guessTaken < 6:
    print ("Take a guess.  ")
    # Allow user input
    guess = input()
    # Record attempt
    guess = int(guess)

    # +1 attempt
    guessTaken = guessTaken +1
    
    # If the guess was less than Number varible inform the user!
    if guess < number:
        print ("Your guess is too low.")
    
    # Same if the guess is higher
    if guess > number:
        print ("Your guess is too high.")

    # If equal, stop
    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken)
    print ("You win")

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number)


        




       
