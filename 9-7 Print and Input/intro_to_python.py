"""
    print and input

    print is a built in function in python, it allows us to output
        text to the screen
    
    print can print different data types
        strings - collection of characters
        booleans
        floats
        integers
"""
if False:
    print("hello there this is a string")
    print('hello there this is a string')
    print('this is a double quote " ')
    
    # if you put a comma in between it will accept multiple things to print
    # things to print == "arguments"
    print(15, 3, -5, 0)
    print("15")
    
    # plus sign in between strings python will concatenate
    # first string then second string in a bigger new string
    print("hello" + "goodbye")
    
    """
        what is a floating point number?
            3.2 1.582828 -0.35
    """
    print(15 + 3.2)
    
    print(3.2 + 10 / 3)
    print(3.2 + 2.8)
    print(1 / 3 + 2 / 3)
    print(5 - 3)
    print(5 * 3)
    print(5 / 3)
    """
        What about powers?
            ^ NOT POWER - bitwise xor
            ** = powers
    """
    
    print(2 ** 10, 3 ** 5, 5 ** 2, 5 ** (1 / 2))
    print(5 ** 1 / 2)
    print(((1 + 15) ** 2 - 3) / 4)
    
    """
        There are two types of division in python
        
            / - makes a floating point
            // - forces it to be an integer (integer division)
    """
    
    print(7 // 3)
    print(int(2.6))
    print(15 // 2, 450 // 10, -1 // 3)
    
    """
        What the heck is a boolean?
        
        0 == False
        1 == True
    """
    
    print(False, True)
    print(False * False, True * True)
    
    """
        let's talk about input
        
        input is also a built in function
    """
    
    input("hello there: ")
    
    """
        This input statement works but instantly is 'forgotten'
    """
    whatever_you_want = input('tell me something: ')
    print('you typed: ', whatever_you_want)
    var_aa = input('Enter the secret code: ')
    print("The secret code is: ", var_aa)
    
    """
        If i just use input then i can get a string input
        
        if you want an integer, you need to "cast" the input statement
    """
    
    my_age = int(input('What is your age? '))  # put a space on the prompt
    # input always returns a string.  int(input('prompt')) will take that string
    # and TRY to make it into an integer
    print(my_age, 'is a number')
    
    """
        for this class you are NOT required to check data types.
        
        if we have a problem where you an input statement "tell me an integer"
            I promise that all graders / scripts will use an integer there
            i am allowed to give you nonsense of the right type
        "tell me a floating point"
            -> floating point variable
    """
    
    pi_approx = float(input('Tell me some digits of pi: '))
    print(pi_approx)
    
    num = int(input('Give me a numerator: '))
    denom = int(input('Give me a denominator: '))
    
    if denom != 0:
        print(num / denom)
    else:
        print('bad human')
    
    """
        print
        
        input
        
        int()
        float()
        str()
    """
    
my_number = 17
my_string = str(my_number)
print(my_number, my_string)
print(my_number + 3, my_string + "hello")
# print(my_string + 3)

"""
    What is a comment?
    
    Triple String 3x' or 3x"
    Multi-line string/comments
    
    Remember to add some code here that divides some numbers
"""

#  this thing << pound sign // hash tag
# this is a single line comment

my_integer = 15  # this integer is fifteen... we can't figure out who set this



