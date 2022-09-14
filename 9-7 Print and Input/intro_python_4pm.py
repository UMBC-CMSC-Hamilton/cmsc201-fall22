"""

print - built in function / keyword
input - built in function / keyword

data types

variables

"""
if False:
    print("here is an example of a string")
    """
        What is a string? - text
            Sequence of characters
            character - single symbol in "text"
        How do we tell the python interpreter that we have a string?
            enclose the string in double quotes
    """
    print("asdf1234=[]@#$%^&*")
    print('single quotes also work')
    print('this is a double quote " inside of a string but it doesn\'t end it')
    """
        print works on strings, is there anything else it can print?
            yes
        prints out variables (we'll get to that)
        
        print out integers, floats, and booleans, (also) strings
    
        What's an integer?
            Whole numbers 1, 2, 3, 4, 5, 6,.. 0, -72
            integers can be positive, negative, zero just no decimal point.
            Not going to overflow unless you get really really really big.
    
        Also it can print floats.
            "decimal points"
            4.1, 3.1415, 2.718, 1.618
            
            round-off error
    """
    
    print(1/3)
    
    print(15, 3, 0, -15, -72, 1000000000000000000000000000)
    
    # be careful of roundoff error, it will always do things when you least expect
    print(4.9 - 4.845 == 0.055)
    
    """
        What are booleans?
            True, False - these are the keywords
        
            True == 1
            False == 0
    """
    print(True, False)
    print(True * True, False * False)
    print(True > False)
    
    # string concatenation - joining two strings together
    print("hello there " + "I am obi wan kenobi")
    print("jello" + "i like jello" + "obi likes jello")
    print("asfd" + " " + "1234")
    
    """
        Does algebra work in programming?
        +, -, * work as expected
        / - floating point division even if the things you divide are both integers.
            the answer will be a float
        // - integer division
        
        power - how does python do powers?
            ^ IS NOT POWER. - bitwise xor
            ** is power
    """
    print(15 + 25, 13 - 7, 45 * 3, 81/9, 80/9)
    print(17//5, 81//9, 19//4, -1//5)
    print(5 ** 2, 2 ** 10, 3 ** 5, 5 ** (1/2))
    """
        Be careful, order of operations does actually work - be advised.
    """
    print(5 + 2 ** 3, (5 + 2) ** 3)
    print(5 ** 1 / 2)
    
    """
        input is another built in function
        
        input(prompt)
            arguments are the "things" that go inside the parentheses
                things - literals or variables
    """
    
    """
        Assignment statements work like this:
        Left Hand Side (LHS) = Right Hand Side (RHS)
                      <-------------
        LHS must be a variable
        RHS must be "evaluable"
        
        How do you declare a variable in python?
            assign the variable for the first time
    """
    x = 3  # no difference between the first assignment and the declaration of the variable
    # declaration of a variable is basically telling the compiler/interpreter
    # that the name "x" is going to be a variable forever after it should understand
    # what x is
    this_is_a_variable = "hello there"
    my_var = 3
    pi_approx = 3.14
    print(this_is_a_variable, my_var, pi_approx)
    
    
    something = input("tell me something: ")
    print("What you typed was", something)
    
    """
    Casting:
        converting from one data type to another
        int(string)
        
    """
    
    my_integer = int(input('Tell me an int: '))
    print(my_integer + 50)
    
    """
        If you ever get a ValueError invalid literal for int...
            it couldn't convert whatever string it was into a number (integer)
            
        You are not required to check if input is the correct data type.
            Assume that all data entered will be of the correct type.
    """
    
    positive_int = int(input('Enter a positive int: '))
    
    digits_of_pi = float(input('Tell me as many digits of pi as you know: '))

numerator = int(input('Tell me the top thing: '))
denom = int(input('Tell me the other thing: '))
print('Your result is ', numerator/denom)

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print('Your name is', first_name, last_name)

"""
    Legal variable names in python?
    
    variables must start with a letter or underscore (no numbers)
    capital letters are fine, lower case are fine
    letters, numbers, underscores
"""

# legal!
_variable = 145
ThisIsAVariable = 5
var1899837192 = 4
