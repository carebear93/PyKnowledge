# A basic calculator program in python
import sys
import os
import math
import calculateFunctions

# This is the main function
def main():
    # Welcome message
    print("Welcome to the calculator!")
    print("Type 'help' for a list of commands.")
    print("Type 'exit' to exit the program.")
    print("")

    # Main user input loop
    while True:
        # Get user input
        user_input = input(">>> ")

        # Check if user wants to exit
        if user_input == "exit":
            print("Closing program")
            sys.exit("Closing program")
        elif user_input == "help":
            print("List of commands:")
            print("+: Addition")
            print("-: Subtraction")
            print("*: Multiplication")
            print("/: Division")
            print("^: Power")
            print("sqrt: Square root")
            print("sin: Sine")
            print("cos: Cosine")
            print("tan: Tangent")
            print("asin: Arcsine")
            print("acos: Arccosine")
            print("atan: Arctangent")
            print("log: Logarithm")
            print("exp: Exponential")
            print("ln: Natural logarithm")
            print("help: This list")
            print("exit: Exit the program")
            print("")
        else:
            # Check if user input is valid
            if user_input[0] == "+" or user_input[0] == "-" or user_input[0] == "*" or user_input[0] == "/" or user_input[0] == "^" or user_input[0] == "sqrt" or user_input[0] == "sin" or user_input[0] == "cos" or user_input[0] == "tan" or user_input[0] == "asin" or user_input[0] == "acos" or user_input[0] == "atan" or user_input[0] == "log" or user_input[0] == "exp" or user_input[0] == "ln":
                # Check if user input is valid
                if calculateFunctions.is_valid_input(user_input):
                    # Calculate the result
                    result = calculateFunctions.calculate(user_input)
                    print(result)
                    print("")
                else:
                    print("Invalid input")
                    print("")
            else:
                print("Invalid input")
                print("")
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Link commands to calculateFunctions.py
        # Addition
        if user_input == "+":
            print("Addition")
            print("")
            print("Enter the first number")
            first_number = input(">>> ")
            print("Enter the second number")
            second_number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.add(first_number, second_number))
            print("")
        # Subtraction
        elif user_input == "-":
            print("Subtraction")
            print("")
            print("Enter the first number")
            first_number = input(">>> ")
            print("Enter the second number")
            second_number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.subtract(first_number, second_number))
            print("")
        # Multiplication
        elif user_input == "*":
            print("Multiplication")
            print("")
            print("Enter the first number")
            first_number = input(">>> ")
            print("Enter the second number")
            second_number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.multiply(first_number, second_number))
            print("")
        # Division
        elif user_input == "/":
            print("Division")
            print("")
            print("Enter the first number")
            first_number = input(">>> ")
            print("Enter the second number")
            second_number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.divide(first_number, second_number))
            print("")
        # Power
        elif user_input == "^":
            print("Power")
            print("")
            print("Enter the base number")
            base_number = input(">>> ")
            print("Enter the exponent")
            exponent = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.power(base_number, exponent))
            print("")
        # Square root
        elif user_input == "sqrt":
            print("Square root")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.square_root(number))
            print("")
        # Sine
        elif user_input == "sin":
            print("Sine")
            print("")
            print("Enter the angle")
            angle = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.sine(angle))
            print("")
        # Cosine
        elif user_input == "cos":
            print("Cosine")
            print("")
            print("Enter the angle")
            angle = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.cosine(angle))
            print("")
        # Tangent
        elif user_input == "tan":
            print("Tangent")
            print("")
            print("Enter the angle")
            angle = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.tangent(angle))
            print("")
        # Arcsine
        elif user_input == "asin":
            print("Arcsine")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.arcsine(number))
            print("")
        # Arccosine
        elif user_input == "acos":
            print("Arccosine")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.arccosine(number))
            print("")
        # Arctangent
        elif user_input == "atan":
            print("Arctangent")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.arctangent(number))
            print("")
        # Logarithm
        elif user_input == "log":
            print("Logarithm")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.logarithm(number))
            print("")
        # Exponential
        elif user_input == "exp":
            print("Exponential")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.exponential(number))
            print("")
        # Natural logarithm
        elif user_input == "ln":
            print("Natural logarithm")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.natural_logarithm(number))
            print("")
        # Factorial
        elif user_input == "!":
            print("Factorial")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.factorial(number))
            print("")
        # Modulus
        elif user_input == "%":
            print("Modulus")
            print("")
            print("Enter the first number")
            first_number = input(">>> ")
            print("Enter the second number")
            second_number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.modulus(first_number, second_number))
            print("")
        # Absolute value
        elif user_input == "abs":
            print("Absolute value")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.absolute_value(number))
            print("")
        # Square
        elif user_input == "sqr":
            print("Square")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.square(number))
            print("")
        # Cube
        elif user_input == "cube":
            print("Cube")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.cube(number))
            print("")
        # Square root of x
        elif user_input == "sqrtx":
            print("Square root of x")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.square_root_of_x(number))
            print("")
        # Cube root of x
        elif user_input == "cbrtx":
            print("Cube root of x")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.cube_root_of_x(number))
            print("")
        # Square root of x
        elif user_input == "sqrtxy":
            print("Square root of x and y")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.square_root_of_x_and_y(number))
            print("")
        # Cube root of x
        elif user_input == "cbrtxy":
            print("Cube root of x and y")
            print("")
            print("Enter the number")
            number = input(">>> ")
            print("")
            print("The result is: " + calculateFunctions.cube_root_of_x_and_y(number))
            print("")
        
        # Invalid input
        else:
            print("Invalid input")
            print("")
            print("Press any key to continue")
            input(">>> ")
            print("")
            print("")
        
        # Clear screen
        os.system('cls')

    
# Run the main function 
if __name__ == "__main__":
    main()

