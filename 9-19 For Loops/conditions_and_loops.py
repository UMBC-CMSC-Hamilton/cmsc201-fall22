"""
   If statements, else, elif
   
   nesting
   
   If statements work by check a condition, if the condition is true
        then it executes
    What happens if the condition is false?
        if you have elif statements == else if
            they check whenever the previous if and elif statements
            are false
    Finally there's an else statement.
        all the conditions are false
        just one.
        
"""
if False:
    animal = input('Tell me an animal! ')
    
    if animal == 'chicken':
        print('cluck')
    elif animal == 'cow':
        print('moo')
    elif animal != 'cat':
        print('what kind of thing is this?')
    else:
        print('meow')
    
    
    if animal != 'cat':
        print('what kind of thing is this?')
    elif animal == 'chicken':
        print('cluck')
    elif animal == 'cow':
        print('moo')
    else:
        print('meow')
    
    
    """
        Harry Potter
            we know characters let's make a little guessing game
    """
    
    house = input('Which house are you in? ')
    if house == 'Griffindor':
        scar = input('Are you sporting a stylish scar? ')
        # nesting == sticking one block into another (if into another if)
        if scar == 'yes':
            print('You are Harry Potter')
        else:
            red_head = input('Do you have red hair? ')
            # double nested
            if red_head == 'yes':
                print('You are a Weasley')
            else:
                books = input('Do you really really like books? ')
                # triple nested
                if books == 'yes':
                    print('You are Hermione')
    elif house == 'Slytherin':
        leader = input('Are you the leader? ')
        if leader == 'yes':
            print('You are Malfoy')
        else:
            print('You are either Crab or Goyle.')
    elif house == 'Hufflepuff':
        print('You are Cedric!')
    elif house == 'Ravenclaw':
        print('You are Luna')
    
    
    number = int(input('Tell me a number: '))
    if number == 17:
        print('That number doesnt matter')
    if number % 2 == 1:
        print('The number is odd')
    
    """
    % = mod = represents the remainder
    32 / 2 = 16 R 0 <--
    32 % 2 == 0 Only gives you the remainder
    
    If you mod a number by 2 it tells you whether that number is
        even or odd
        
    number is divisible by 2 <==> it is even! so zero is even
    
    """
    
    print(16 % 7, 31 % 5, 40 % 2, 9 % 4)
    # python specific thing, but also it follows the "rule"
    #   back in elementary school remainders have to be positive.
    print(-3 % 5)
"""
    Rule for remainders is that R >= 0.
    -3 = (-1)*(5) + 2 = -5 + 2
"""

"""
    Theoretically that was review... maybe, watch my youtube lecture.

    Now I want to talk about for loops.
        range "object"
        
    for(int i = 0; i < number; i++)
    
    Let's say we need a range of numbers. 0, 1, 2, 3, 4
    range(n) outputs 0, 1, 2, 3, 4, ... n - 1
        How many numbers are there between 0 and 9 (inclusively)?
            10
    What a loop does is allow us to repeat a certain block of code
    
    We want to add up all the numbers between 1 and n.
"""
n = int(input('Tell me the number: '))
total = 0
for i in range(n + 1):
    # total = total + i
    total += i
    print(i, total)

print(total)

"""
    Basel Problem adding up the squares of the reciprocals
        of the integers
"""
n = int(input('Tell me another number: '))
basel = 0
for i in range(n):
    if i != 0:
        basel += 1 / i ** 2

"""
    There are some secret arguments inside of range.
        range(stop) = 0, 1, 2, 3, 4,.... stop - 1
        range(start, stop) = start, start + 1, start + 2, .. stop - 1
"""

print(basel)

start = int(input('Start: '))
stop = int(input('Stop: '))
for index in range(start, stop):
    print(index)

"""
    Invalid ranges, it's never going to execute

    CTRL + C in GL will kill the process = it will stop your program
"""

"""
    Infinite loop = "loop that will never end"
"""

"""
    For loops and lists "go together" in python
    
    a_list is not exactly the same as a string, float, int, bool
    
    it's a collection of various elements
"""
if False:
    a_list = ['hi', 'bye', 'robot', 'read', 'write', 'scamper']
    int_list = [5, 7, 9, 12, -3, 56, 42]
    float_list = [3.14, 1.618, 2.71828, .999]
    mixed_list = ['stringy', 3.14, 2, 'bye', True]
    
    print(a_list)
    print(int_list)
    print(float_list)
    print(mixed_list)
    
    """
        how do I access any given thing?
            use an index to access elements in the list
            
        
    a_list = ['hi', 'bye', 'robot', 'read', 'write', 'scamper']
               0      1       2        3       4        5
    """
    print(a_list[0], a_list[2], a_list[5])
    # remember that accessing an element out of the range of the list is an IndexError
    # print(a_list[17])
    
    """
        [5, 7, 9, 12, -3, 56, 42]
         0  1  2  3    4   5   6
    """
    for x in int_list:
        print(x)
        
    """
        len keyword gives us the length of a thing
            len(string), len(list), len(dictionary)
            len(int) = TypeError
    """
    
    # stock bit of code
    # range(len(int_list)) takes the length and sticks it into the range
    # range gives us 0, 1, 2, 3, ... len(int_list) - 1
    # reason that it gives us up to length - 1 instead of length is because
    #   if it gave us length it would cause indexerrors for every list.
    for i in range(len(int_list)):
        # first thing we print out is the index
        # second thing we print out is the value of the list at that index
        print(i, int_list[i])
        
    """
        What if you want to change a value in a list?
    """
    # if you access a list by index and then assign, you can overwrite
    # the value
    int_list[4] = 17
    print(int_list)
    
    # this list starts out empty, want to add five things into it
    five_things = []
    for i in range(5):
        thing = input('Enter a thing: ')
        # to add something into a list you use append = sticks the element on to the end
        five_things.append(thing)
    
    print(five_things)

number_of_things = int(input('How many things? '))
all_the_things = []
"""
number_of_things is generated by user input
    users are evil
"""

if number_of_things > 20:
    number_of_things = 20
    """
        \' == gives me an apostrophe, single tick mark
        \n - new line
        \t - tab
        \\ = single backslash
        # doesn't work anymore :(
        \a = computer beep
    """
    print('Bad user, don\'t do that.')

for i in range(number_of_things):
    thing = input('Enter a thing: ')
    # to add something into a list you use append = sticks the element on to the end
    all_the_things.append(thing)

print(all_the_things)