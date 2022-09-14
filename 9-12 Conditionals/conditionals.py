"""
    Conditionals - if statements
"""

"""
    Aside, back to string formatting:
"""
if False:
    x_is_three = 3
    print('the value of x is', x_is_three)  # good if you're learning
    print(f'the value of x is {x_is_three}')  # nice also a bit "pythonic" <--
    print('the value of x is {}'.format(x_is_three))  # first way
    print('the value of x is ' + str(x_is_three))
    
    my_name = 'Eric'
    my_number = 52
    # if i don't put the f in front of the string, python does nothing
    print('your name is {my_name} and your number is {my_number}')
    # this one should work
    print(f'your name is {my_name} and your number is {my_number}')
    
    """
        variables
        
        what makes a legal python variable?
            letters [capital and lower case are fine] and numbers and underscores
            
        what does legal mean?
            it won't cause an error
    """
    
    ThisIsALegalVariable = True
    how_about_this = 54
    helloVariables = 'something'
    """
        can't start with a number - don't start with a number
            can only start with a letter or underscore
    """
    num_of_people_3 = 3
    
    __hi = 7
    ____bye = 'bye'
    
    """
        There's a difference between legal and to the coding standard
        snake case is lowercase letters numbers separated by underscores
    """
    # good
    number_of_cats = 17  # snake case, python, ruby, scripting languages like that
    digits_of_pi_after_3 = .1415
    height_of_human = 2.3
    # bad
    numberOfCats = 17  # not snake case, Camel case Java-like languages
    # avoid single letter variables when possible / not indexes
    radius = 7
    
    # what does any of this do?
    x = 6
    y = 4
    z = (x + y) ** (1/2) - x - y
    k = x * y * z - z
    
    """
        literal = number, string, float, boolean hard coded
    """
    my_int = int(input('Tell me an int: '))  # not a literal
    my_value = 5  # literal
    my_string = 'hello this is a string'  # literal
    
    """
        Conditionals - if statements
            programs without conditionals basically do one thing.
                flow in a straight line, through all the code
                prints, inputs, calculations, and that's it.
                
        if statements - conditionals are a way to allow programs to make decisions
    """
    my_favorite_number = int(input('Tell me an int: '))
    # if <condition>: (need the if and you need a condition that evaluates to true
    # or false, and then you need a colon)
    # note that in order to check equality you need to use two equal signs
    if my_favorite_number == 17:
        # anything inside an if statement must be tabbed in once
        print('You have picked wisely')
        print('hi')
        print('print me too')
        print('whatever')
        
    print('will this print? ')
    
    """
        There's a difference in most languages between assignment and boolean
        equality checks.
        To assign something use one equal
        To check use two.
    """
    
    """
        Conditional Operators
        What kind of things can we check?
            == (equality)
            != (not equals)
            <, >, <=, >= (numerical inequalities)
    
            String comparisons
    """
    
    test_int = int(input('Tell me another int: '))
    if test_int != 42:
        print('You have not discovered the meaning of life.')
        
    
    test_string = input('What is your message? ')
    if test_string == "the world wonders":
        print('ahahaha')
    
    #  there is a nice built in function called .lower(), .upper()
    if test_string.lower() == "the world wonders":
        print('i am really mad at that')
        print(test_string)
        
    a_string = input('Give me string a: ')
    b_string = input('Give me string b: ')
    
    """
        basically does alphabetical comparison... with a few caveats
            it does actually still care about upper vs lower case
            numbers have ascii values too
        
    """
    
    if a_string < b_string:
        print('its true it is less!')
    
    print(len(a_string), len(b_string))
    
    print(ord('0'))

"""
    Logical Operators
    
    and, or, not
    Truth Tables
    A and B is True means that:
        1) A is True
        2) B is True
    A       True        False
    ___________________________
B
True        True        False
False       False       False

Let's talk about or.
    (inclusive)
    A or B is True means that:
        at least one of A and B are true
        could also be both
        cannot be neither
    
    A       True        False
    ___________________________
B
True        True        True
False       True        False

(eventually you should know this)
xor [not a keyword]
    A       True        False
    ___________________________
B
True        False        True
False       True        False

Last logical operator: unary operator
    not A
    
    A   True    False
    -----------------
not A   False   True
"""


"""
    Order of Precedence - operator precedence
    
    first - algebra
        parentheses
        exponents
        multiplication-division
        addition-subtraction
    second comparison operators
        ==, !=, <, <=, >, >=  - equal precedence
    last one is logical operators
        not - slightly higher precedence
        and, or - equal precedence
"""

if (3 + 2) ** 2 < (5 - 2) ** 3:
    print('this math is true')


a = True
b = False
c = True
d = True
e = False

if (a and b) or c:
    print('hello')

if not a and b:
    print('this will happen')
    
if not a or not b:
    print('to be or not to be')

"""
    a = True
    b = False
    c = True
"""
if (a or c) and (b or c):
    print('huh?')


password = input('tell me the password: ')
secret_number = int(input('secret number: '))

if password == 'password1' and secret_number == 42:
    print('you have gained access to the server')
