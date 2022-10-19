"""
    functions - segment code into little blocks of functionality
        scope = variables we create inside the function
            only live inside that function
            local scope
"""


def count_a(a_string):
    count = 0
    for ch in a_string:
        if ch.lower() == 'a':
            count += 1
    
    return count


def count_fives(a_list):
    count = 0
    for x in a_list:
        if x == 5:
            count += 1
    
    return count


"""
    parameters - function gets as input
    arguments
"""

PI = 3.14159265


def circle_area(r):
    return PI * r ** 2


def circle_circum(r):
    return 2 * PI * r


def calculate_area(length, width):
    return length * width


def calculate_volume(length, width, height):
    return length * width * height


def dot_product(vector_1, vector_2):
    if len(vector_1) != len(vector_2):
        print('Error: Cannot take dot product. ')
        return 0
    
    dot_prod = 0
    for i in range(len(vector_1)):
        dot_prod += vector_1[i] * vector_2[i]
    
    return dot_prod


print(dot_product([1, 2, 3], [4, 5, 6]))
print(dot_product([1, 2], [4, 5, 6, 7]))


def make_board():
    new_board = []
    for i in range(3):
        new_row = []
        for j in range(3):
            new_row.append('_')
        new_board.append(new_row)
    
    return new_board

def display_board(a_board):
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(a_board[i][j], end="|")
            else:
                print(a_board[i][j])


the_game = make_board()
display_board(the_game)


"""
    Mutability
        Remember that:
            int, bool, string, float are all immutable
            
            lists, classes and dictionaries are mutable
"""

def modify_string(a_string: str):
    a_string = a_string.replace('a', 'z')
    print(a_string)
    return a_string


def square_int(x):
    x **= 2
    return x


def add_random_to_list(a_list):
    a_list.append('random stuff')
    return a_list

aardvark = 'aardvark'
print(modify_string(aardvark))
print(aardvark)
"""
    immutable objects/variables are "passed by value"
    a copy is made of that variable
"""

my_int = 5
print(square_int(my_int))
print(my_int)

some_new_list = ['zebra', 'thoroughly', 'salmon', 'tribe']
b_list = some_new_list
b_list.append('happy')

# because a list is mutable it passes by reference and CAN
# be modified by functions
add_random_to_list(some_new_list)
print(some_new_list)

import random
def scary_function(a_list):
    while len(a_list) > 5:
        del a_list[random.randint(0, len(a_list))]

my_very_nice_and_special_list = ['a', 'b', 'd', 'r', 't', 'q','u', 'e', 'r']

throw_away_copy = my_very_nice_and_special_list[:]
scary_function(throw_away_copy)
print(throw_away_copy)
print(my_very_nice_and_special_list)
"""
    immutable things pass by value = makes a copy of the variable
    mutable things pass by reference = passes memory location
"""
