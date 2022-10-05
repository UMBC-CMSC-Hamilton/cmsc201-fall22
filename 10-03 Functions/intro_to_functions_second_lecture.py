"""
    loops = while loops and for loops
   
    what is the purpose of a while?
        if you don't know (indeterminate) how many times the loop
            needs to run
        user validation loops
"""


def dont_run_me():
    command = input('What is thy command? ')
    while command != 'quit':
        command = input('What is thy command? ')
    
    a_list_of_things = []
    # priming the input
    command = input('What is thy command? ')
    while command != 'quit':
        a_list_of_things.append(float(command))
        # this command, this variable has been checked (safe to cast)
        command = input('What is thy command? ')
        # if you put additional code here you have to remember
        # this command is a new string has not been checked
    
    """
        every for loop can be written as a while loop
    """
    
    for i in range(2, 104, 12):
        print(i)
    
    index = 2
    while index < 104:
        print(index)
        index += 12
    
    my_list = [1, 65, 3, 5, 5, 3, 5, 4, 3, 6, 3, 5, 5]
    for x in my_list:
        print(x)
    
    index = 0
    while index < len(my_list):  # range(len(my_list))
        print(my_list[index])
        index += 1


"""
    Converse is not true:
        not every while loop can be made into a for loop
        things above, while num < 0:
        while command != 'quit'
"""

"""
    
    Functions: what is a function?
        you can call them from anywhere in your program,
            they run a little subroutine then they return you
            to your calling address/the line of code that called it

        last piece of any programming langauge
        
            variables, if statements, loops, functions, [classes]
"""


# def = define
# function name is print_nonsense (snake case)
# no parameters here yet
def print_nonsense():
    print('nonsense!~')


def square_me(x):
    """
        you can input a value into the function it creates a variabale
        called x that it uses while the function is running.

        x is a temporary variable, it has a lifetime
        only exists as long as the function is running
        local scope = variable exists inside of a function
    :param x:
    :return:
    """
    print(x ** 2)


#
# for i in range(5):
#     square_me(i)
#     # can't just access a local variable print(x)
#
# a global variable/variable in global scope
a_string = 'how many vowels are in this string which is asking about vowels?'


# count = 0
# # for each loop on a string breaks it into characters
# for c in a_string:
#     if c.lower() == 'a':
#         count += 1
#
# print(f'There are {count} a\'s')
#
# for c in a_string:
#     if c.lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
#         count += 1
# print(f'There are {count} vowels')

def count_the_as(a_string):
    count = 0
    # for each loop on a string breaks it into characters
    for c in a_string:
        if c.lower() == 'a':
            count += 1
    
    print(f'There are {count} a\'s')


def count_the_vowels(a_string):
    count = 0
    for c in a_string:
        if c.lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
            count += 1
    print(f'There are {count} vowels')


count_the_as('what_does_this_do? aarvark')
count_the_vowels('what_does_this_do? aarvark')
count_the_vowels(a_string)
b_string = 'asdfasdfiioouuee'

count_the_vowels(input('Tell me a string: '))
count_the_vowels(b_string)

"""
    returns
        return statements allow us to "output"/return data from a function
        to a point in your code, use it or save in a variable
"""


def cube_me(x):
    return x ** 3


# stick it into a variable
something = cube_me(5)
print(something)
# use it immediately, but then it goes away .... forever...
print(cube_me(7))


def count_evens(a_list):
    count = 0
    for x in a_list:
        if x % 2 == 0:
            count += 1
    
    return count


num_evens = count_evens([1, 9, 6, 8, 3, 14, 3, 7])
# CTRL + ALT + L
print(num_evens)


#         0    1
# p_1 = [x_1, y_1]
# p_2 = [x_2, y_2]
def distance(p_1, p_2):
    the_dist = (p_2[0] - p_1[0]) ** 2 + (p_2[1] - p_1[1]) ** 2
    the_dist **= (1 / 2)
    return the_dist

# print(print('hello'))
print(distance([0, 0], [1, 1]))
print(distance([0, 0], [10, 0]))
print(distance([0, 0], [0, 10]))
print(distance([3.1, 7.9], [15.2, -2.1]))

"""
    multiple returns in a function
"""

"""

    umbrellaabcxy
    
    looking for abc
    Idea: check to see if a letter is 'a'
            if true check to see if next is 'b'
                if true check to see if the next is 'c'

"""

def is_substring(big_string, little_string):
    for start in range(len(big_string) - len(little_string) + 1):
        could_be = True
        for j in range(len(little_string)):
            if big_string[start + j] != little_string[j]:
                could_be = False
        if could_be:
            return True
    
    return False


print(is_substring('umbreallaabcumbrellaagain', 'abc'))
print(is_substring('xyzwkl', 'abc'))


def do_nothing():
    x = 3
    return x
    
my_var = do_nothing()
print(my_var)