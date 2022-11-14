"""
    Exception Handling.
    
        Errors in python:
            ValueError, TypeError, IndexError, KeyError,
                RecursionError, SyntaxError, IndentationError
                NameError
        Compile-Time Errors - errors that occur when python is
            determining if your program is valid
        Runtime error - Error that you get during the run of your
            program.
"""

"""
print('hello there')
for i in range(10)
    print(i)
SyntaxError is compile time.

def my_function():

print('hello there')

indentation error - prevents our code from running
    also a syntax error, kind of more specific version of syntax
    
Syntax - structure of language.
    SVO - subject verb object = english
    for _ in _:
    def _____fun_name____(parameter list, with commas):
    tab->your code

Semantics - what does it mean?
    what does it do?
"""

"""
    What about runtime errors?
        ValueError, TypeError, NameError, RecursionError,
            KeyError, IndexError
"""

"""
    Here's a big problem:
        user input crashing our program
    
    if you get a ValueError inside of this try, it will go to the
        except code for the ValueError
"""
def never_run():
    x = 1
    while x > 0:
        try:
            x = int(input('>> '))
            print('The int is', x)
        except ValueError:
            print('You have not entered a valid integer')
    
    a_list = [4, 7, 2, 7, 4, 6, 4, 3, 9]
    index = 1
    while index >= 0:
        try:
            index = int(input('Tell me an index: '))
            print(index, a_list[index])
        except ValueError:
            print('You must enter an integer')
        except IndexError:
            print('You must pick a value in bounds')
    
    
    def bad_recursion(n):
        print(n)
        bad_recursion(n - 1)
    
    
    try:
        bad_recursion(10)
    except RecursionError:
        print('TOO MANY!!!!')
    
    
    my_favorite_things = {'apple': 17, 'monkey': 3, 'lightsaber': 300,
                          'guinea pig': 53, 'toaster': 4, 'newspaper': 55}
    key = ''
    while key != 'quit':
        key = input('Give me your key: ')
        try:
            print(key, my_favorite_things[key])
        except KeyError:
            print('That was not in the dictionary')
    
    key = ''
    while key != 'quit':
        key = input('Give me your key: ')
        if key in my_favorite_things:
            print(key, my_favorite_things[key])
        else:
            print('That was not in the dictionary')
    
    
    x = 5
    while x > 0 or my_var < 20:
        try:
            my_var += 1
            print(my_var)
        except NameError:  # runtime error, not compile time - like in all the sane langauges
            my_var = 0
            x = 0
            print('This was not a variable, declaring it')
    
    """
        Short Circuiting
        A or B = A is True or B is True / or both
        True or B = True
        
        A and B = both A and B must be true
        False and B = False
    """
    x = 0
    y = 5
    if x != 0 and y/x > 1:
        print('it is so')
    else:
        print('it is not so')
    
    try:
        print(y // x)
        # important code here
        print('this must print or we all die')
    except ZeroDivisionError:
        print('yep we got it')
        


def count_5s(a_list):
    count = 0
    try:
        for x in a_list:
            if int(x) == 5:
                count += 1
    except ValueError:
        raise AttributeError('One of the items in the list was not castable to int')
    
    return count


try:
    count_5s(['hi', 'robot', 'turnip', 'sandwich', 'flamingo'])
except AttributeError as ae:
    print('The user did something bad')
    print(ae)


try:
    int('x')
except ValueError as value_error:
    print('Please enter an integer value.')
