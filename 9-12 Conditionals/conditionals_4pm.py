"""
    Print formatting
    coding standards and variables
    conditionals
"""
if False:
    the_number_five = 5
    another_number = 17
    print('the variable is', the_number_five)  # this is good
    print('the variable is {}'.format(the_number_five))  # don't need this one anymore
    print(f'the variable is {the_number_five}')  # i like this one too
    print('the variable is ' + str(the_number_five))  # always keep this one in mind
    print(f'the first number is {the_number_five} and the second number is {another_number}')
    
    """
        Coding standards vs legal variables.
        
        you can use letters, numbers, and underscores
            can't use #$%^&* garbage
        cannot start with a number
    """
    
    print(0x52ad, 0b11001010101010)
    
    __the_variable_name = 'hi'
    ThisIsLegal = 'yep'  # capital case... whatever
    iWillMakeItLegal = 'also yes'  # camel case - java
    var235 = 2356
    
    """
    snake case: letters and numbers separated by underscores, lowercase
    
    PEP 8 - standards for python
    tons of legal variable names that do not follow snake case
    
    """
    this_is_snake_case = True
    vector_235 = True
    hello_there = 1234
    
    TotallyNotSnakeCase = False
    
    """
        Conditionals - allow decisions to be made, allow programs to 'branch'
            either the program can run some code, or it can run some other code
            and not run the first code.
            
            print, input, algebra, variables
    
        Conditionals use if statements
    """
    # if <condition> :  <condition> must evaluate to either True or False
    # if the condition is true, the if statement will execute, otherwise not.
    x = int(input('Give me int! '))
    # notice something about it... we have a ==
    #  single equals is "assignment operator" double equals is a "comparison operator"
    # assignment operator will change a variable
    # comparison operator is going to test for equality, inequality
    #       comparisons output boolean values -> True or False
    
    if x == 5:
        # not insensitive to whitespace .. whitespace sensitive
        # tabs matter == 4 spaces
        # all code inside of the if statement must be tabbed in by one
        print('How did you know, I love five.')
        print('This is more code inside the if statement')
        print('And yet more code.')
        print('i hit tab')
        print('hi, i am inside the if statement')
        # in emacs sometimes what you can do is hit tab down tab then down
    
    print('but not this')
    
    if True:
        print('hello there')
    
    if False:
        print('will I execute?')

"""
    comparison operators
    
    ==, != (not equals)
    <, >, <=, >=        <-- the equal sign has to be on the right
"""
x = -8
if x <= 3:
    print('x is less than or equal to 3')

if x != 17:
    print('x is definitely not 17')

if (x ** 2) - 5 > 0:
    print('some equation is positive')

"""
    PE(DM)(AS) - order of operations for algebra.  BODMAS
    
    1) algebra executes first
    2) comparison operators
        all comparison operators have equal precedence.
    3) Logical Operators
"""
x = 4
if 2 < x < 5:
    print('x is between 2 and 5')

"""
    There are three different logical operators: and, or, not

    Truth Tables
    
    A and B = both A is True and B is True
    
    thing.getData() > 3 and my_password == correct_password
    
    AND A   True    False
    B
    True    True    False
    False   False   False
"""

x = 4
y = 9
if x > 3 and y > 7:
    print('x and y are big enough')

"""
    Logical operator - or
    
    A or B (inclusive)
    A can be true, B can be true OR both can be true.

A or    True    False
B
True    True    True
False   True    False


A xor   True    False
B
True    False   True
False   True    False

"""

a = True
b = False
c = True

if a and b or c:
    print('neither here nor there')

if (a and c) or (b and c):
    print('is this a trick? or just a question?')

"""
def a():
    print('a is being checked')
    return True


def b():
    print('b is being checked')
    return False


def c():
    print('c is being checked')
    return True


if a() or c() and b():
    print('maybe? huh whats up with that')
"""

"""
Here's the precedence: (since we're doing python 3, ... yes!)
not
and
or
"""

"""
Let's talk about not.

not is a "unary operator" -

A       True    False
not A   False   True
"""

"""
    a was true, b was false, c was true
"""
if not a or b:
    print('hello there')


if not a and not b:
    print('hello there again')

d = False

if not (a or b) and not (c or d):
    print('hi!!!!')


