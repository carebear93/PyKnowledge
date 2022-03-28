import math

# This is the function that will handle the calculations
def calculate(arg):
    # This is the function that will handle the calculations
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    def power(x, y):
        return x ** y
    def square(x):
        return x ** 2
    def square_root(x):
        return math.sqrt(x)
    def cube(x):
        return x ** 3
    def cube_root(x):
        return x ** (1/3)
    def sin(x):
        return math.sin(x)
    def cos(x):
        return math.cos(x)
    def tan(x):
        return math.tan(x)
    def log(x):
        return math.log(x)
    def ln(x):
        return math.log(x, math.e)
    def factorial(x):
        return math.factorial(x)
    def mod(x, y):
        return x % y
    def pi():
        return math.pi
    def e():
        return math.e
    def e_power(x):
        return math.e ** x
    def e_power_minus_one(x):
        return math.e ** (-1 * x)
    def e_power_minus_two(x):
        return math.e ** (-2 * x)
    def e_power_minus_three(x):
        return math.e ** (-3 * x)
    def e_power_minus_four(x):
        return math.e ** (-4 * x)
    def e_power_minus_five(x):
        return math.e ** (-5 * x)
    def e_power_minus_six(x):
        return math.e ** (-6 * x)
    def e_power_minus_seven(x):
        return math.e ** (-7 * x)
    def e_power_minus_eight(x):
        return math

    # This is the dictionary that will hold the functions
    functions = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "power": power,
        "square": square,
        "square_root": square_root,
        "cube": cube,
        "cube_root": cube_root,
        "sin": sin,
        "cos": cos,
        "tan": tan,
        "log": log,
        "ln": ln,
        "factorial": factorial,
        "mod": mod,
        "pi": pi,
        "e": e,
        "e_power": e_power,
        "e_power_minus_one": e_power_minus_one,
        "e_power_minus_two": e_power_minus_two,
        "e_power_minus_three": e_power_minus_three,
        "e_power_minus_four": e_power_minus_four,
        "e_power_minus_five": e_power_minus_five,
        "e_power_minus_six": e_power_minus_six,
        "e_power_minus_seven": e_power_minus_seven,
        "e_power_minus_eight": e_power_minus_eight
    }

# This is the list that will hold the arguments
args = []

# This is the list that will hold the operators
operators = []

# This is the list that will hold the numbers
numbers = []

# This is the list that will hold the functions
functions_list = []