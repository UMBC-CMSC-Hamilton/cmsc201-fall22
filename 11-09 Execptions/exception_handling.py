"""
    What happens when we do something wrong in python?
        some kind of error happens

    compile time error:
        error that happens before the program runs
            IndentationError
            SyntaxError
    run time errors:
        errors that happen as the program is running
        ValueError, TypeError, IndexError, RecursionError
        KeyError

    Syntax - structure of the language
        when you write a for loop, do you have for _ in _ :
        def func_name(params, others):
"""
def dontrun():
    x = 0
    while x != -1:
        try:
            my_list = [0, 1, 2, 3, 4, 5]
            x = int(input('>>> '))
            print(my_list[x])
        except ValueError as val_error:
            print(val_error)
            print('That was not an integer')
        except IndexError as ind_error:
            print(ind_error)
            print('That was out of bounds.')
            x = int(input('ex>>> '))
            if 0 <= x < len(my_list):
                print(my_list[x])
            else:
                print('You were bad twice')
        
    """
        bare except is dangerous just because you don't know
            what you're catching.
    """
    try:
        # crazy code in here
        pass
    except:
        print('There was an error')
        
    """
        Short Circuiting:
            A or B checks A, checks B asks , is one of them true?/or both
            True or B = True
        if the first prong of an or statement is true, it doesn't check
            the second prong
    """
    x = 1
    """
        NameErrors = variables that are not defined are runtime errors
            you can catch them.
    """
    while x > 0 or my_var < 20:
        x = -5
        try:
            my_var += 1
        except NameError:
            my_var = 0
            print('My var was undefined, so i set it to zero')
        
        print(my_var)
        
    import time
    
    def recursion(n):
        # huge problem no base case, nothing will ever prevent this recursion
        # except for RecursionError
        print(n)
        # time.sleep(0.05)
        recursion(n - 1)
    
    
    try:
        recursion(50)
    except RecursionError:
        print('You did bad')
    
    """
        IndexErrors, KeyErrors
    """
    
    my_dict = {'a': 3, 'b': 7, 'c': 12, 'd': 3, 'e': 15, 'f': 21}
    
    x = input('Tell me a key: ')
    while x != 'quit':
        # in checks whether the variable is a KEY not a value
        try:
            print(x, my_dict[x])
        except KeyError as the_key_error:
            print(the_key_error)
            print(f'{x} is not a key, not even trying it')
        x = input('Tell me a key: ')
    
    
    """
        Right way to do it:
        
        if x in my_dict:
            print(x, my_dict[x])
        else:
            print(f'{x} is not a key, not even trying it')
    
    """
    try:
        x = int(input('Enter int>> '))
        while x != 0:
            try:
                if x < 0:
                    raise ValueError('You can only take a square root of a positive number')
                print(x ** (1/2))
            except ValueError as ve:
                print('You entered a negative x', ve)
            x = int(input('Enter int>> '))
    except ValueError:
        print('You entered a non-integer')


class AuthenticationError(Exception):
    pass


def authenticate():
    password = input('Enter password')
    correct_password = 'hello there'
    attempts = 0
    while password != correct_password:
        password = input('Enter password')
        attempts += 1
        if attempts > 5:
            raise AuthenticationError() # need the parens
            # becuase you're making an error
    
try:
    authenticate()
    print('You are in')
    # catching all the errors of this type
except AuthenticationError:
    print('You are the virus!')


"""
try:
    print('about to raise the new error')
    raise MyNewError()
except MyNewError:
    print('caught it')
"""