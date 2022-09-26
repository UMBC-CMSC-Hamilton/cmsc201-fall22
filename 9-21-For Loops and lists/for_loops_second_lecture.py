"""
    Things that evaluate to True
    
        All integers are true, except 0, which is false
        All floats are true, except 0.0 which is false
        All strings are true, except empty string, which is false
        Booleans work as 'expected'
            True is True, False evaluates to False
        
        Lists work the same as strings:
            all lists are true except for the empty list.
            even [0, False, 0.0] is true
        None is actually false.
        
"""
if False:
    x = None
    if x:
        print(f'x = {x} is true')
    else:
        print(f'x = {x} is false')
    
    my_int = 0
    if my_int % 2 == 0:
        print(f'{my_int} is even')
    else:
        print(f'{my_int} is odd')
    
    
    if my_int % 2:
        print(f'{my_int} is odd')
    else:
        print(f'{my_int} is even')
    
    if not(my_int % 2):
        # f'' tells python it is "a format string"
        # if you put a variable into curly braces, python looks up
        #       the variable, casts it to a string, inserts it into the overall string
    
        print(f'{my_int} is even')
        # should print the same as print(my_int, 'is even')
    else:
        print(f'{my_int} is odd')

    """
        For loops again
    
        range object
            range(start, stop, step) ***
            range(beginning, ending, increment)
            
            # always excludes stop
            # step size defaults to 1
            # start defaults to 0
            range(start, stop) step = 1
            range(stop) start = 0 step = 1
    """
    for i in range(5, 17, 3):
        print(i)
    print('countdown')
    for i in range(10, -1, -1):
        print(i)
    
    """
        Moral of the Story: print is very slow
            print much slower than most arithmetic calculations
    """
    random_calc = 0
    for i in range(1, 2000000):
        if i % 100000 == 0:
            print(i)
            
        random_calc += i
        
    print(random_calc)
    
    """
        Let's talk about lists again:
        
    """
    
    the_list = []
    # the_list = list()
    
    for i in range(6):
        a_thing = input('Tell me a thing: ')
        # if you want to add an element to a list, use append
        # <list_name>.append(<thing>)
        # specifically to the end of the list
        the_list.append(a_thing)
    
    print(the_list)
    
    
    logged_in = []
    NUM_USERS = 25
    # want to create a list of 25 elements, all False
    for i in range(NUM_USERS):
        logged_in.append(False)
    
    print(logged_in)
    
    index_list = ['a', 'b', 'c', 'd', 'e', 'f']
    #              0    1    2    3    4    5
    print(index_list[1], index_list[3], index_list[4])
    """
        Can i modify a list? Yes
    """
    # # if you want to modify a list, you must use the for-i "mechanic"
    # # for-i loop (i represents an index)
    # for i in range(len(index_list)):
    #     yes_no = input(f'Do you wish to modify the element = {index_list[i]}')
    #     if yes_no == 'yes':
    #         new_element = input('give me a new element: ')
    #         index_list[i] = new_element
    #
    # print(index_list)
    
    # for each loop (x represents an element from the list)
    # x is not actually the element inside the list
    # x is a copy of that element - won't change the list
    for x in index_list:
        yes_no = input(f'Do you wish to modify the element = {x}')
        if yes_no == 'yes':
            new_element = input('give me a new element: ')
            x = new_element
            print(f'The new element is {x}')
    
    print(index_list)

"""
    Mutability in Python
    Define these types as immutable:
        int
        bool
        float
        string
        
"""

my_string = "this is a string, yes"
print(my_string[5], my_string[12], my_string[3])

# not possible - strings are immutable - cannot be changed
# my_string[5] = 'a'

#instead you can convert a string to a list:
my_list = list(my_string)
print(my_list)
# must use for i to modify a list
for i in range(len(my_list)):
    if my_list[i] == 'i':
        my_list[i] = 'x'
    
print(my_list)
print(''.join(my_list))
