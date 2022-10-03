"""
    First midterm is next wednesday 10/12
    
    last time = while loops
        infinite loops = condition of the while is never false
            maybe logically can't be false, even if a user could
                keep a loop running as long as they want
        skipped loop = loop that never runs = condition is false
            before it goes in the first time

the_input = input('hi')
while the_input != 'quit':
    the_input = input('hi')
    
x = 1
while x > 0:
    print(x)
    x += 1
    
    Any for loop can be recoded as a while loop
    
    not all while loops can become for loops
        can't really do a for loop that loops until the user says
            quit
            
    while loops are if statements with the repeat turned on
"""
if False:
    for i in range(2, 231, 4):
        print(i)
    
    index = 2
    while index < 231:
        print(index)
        index += 4
    
    a_list = []
    
    list_index = 0
    while list_index < len(a_list):
        # do whatever you want to the list at index list_index
        list_index += 1

"""
    Functions - what is a function?
        it's a piece of code that we can call and it will run
            whenever we call it.
            
        terminology - notation
"""


# def = define function
# name your function - snake case in python
# notice parentheses after the function name

# purpose number 1 - you can call it multiple times.
# purpose number 2 - break up your program into little readable chunks
#                  - testing

def print_message():
    print('The message is here.')


print_message()
print_message()
print_message()

for i in range(3):
    print('The message is here.')

"""
    Functions can take arguments that change how they run
    in this function x is called the parameter
"""


def is_prime(x):
    """
        x is a local variable = temporary variable
            it has a lifetime
            however long the function runs
        is_it_prime is also a local variable
            when you exit the function, at the end of the function's code
            it returns back to the place where it was called
        all the local variables are destroyed
        
        refer to "lifetime" as scope
        
        any other variable you create is in the global scope
        
    :param x: the integer we are going to test
    :return:  boolean, if x is prime
    """
    is_it_prime = True
    for i in range(2, x):
        if x % i == 0:
            is_it_prime = False
    print(f'is {x} prime?', is_it_prime)
    return is_it_prime

def count_as(my_string):
    count = 0
    for char in my_string:
        if char == 'a' or char == 'A':
            count += 1
    return count


def count_vowels(my_string):
    count = 0
    for char in my_string:
        if char.lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
            count += 1
    # print(count)
    return count

def count_evens(the_list):
    count = 0
    for x in the_list:
        if x % 2 == 0:
            count += 1
    # print('The number of evens is', count)
    return count
    print('hello')  # unreachable code after a return


for i in range(2, 10):
    # i into the parameter for is_prime, we call that an argument
    is_prime(i)

# this count is the global one, it has global scope
# it exists throughout the entire program
# it is not overwritten by the local variables
count = 5
num_as = count_as('hello i am a robot')
print('The number of As is', num_as)
print(count)
num_vowels = count_vowels('hello i am a robot')
print('The number of vowels is', num_vowels)

my_list = [1, 2, 5, 7, 6, 16, 8, 9, 3, 5, 3, 2, 5]
another_list = [8, 7, 3, 5, 43, 3, 5, 4, 354, 56, 4, 33, 5, 4]
num_evens = count_evens(my_list)
print('The number of evens is', num_evens)
num_evens = count_evens(another_list)
print('The number of evens is', num_evens)

"""
    We have to talk about returns
    
"""

def distance(x_1, y_1, x_2, y_2):
    return ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** (1/2)

# what to do with returned values? either put them in a function
# or you can save them to a variable
print(distance(0.4, 3.1, 7.2, 8.9))
print(distance(0, 0, 1, 1))
print(distance(0, 0, 10, 0))
print(distance(0, 0, 0, 10))
print(distance(2, 5, 17, 31))

the_distance = distance(7, 8, 9, 10)
print(the_distance)


def does_it_contain(a_string, a_substring):
    if len(a_substring) > len(a_string):
        return False

    is_substring = False
    for i in range(len(a_string) - len(a_substring) + 1):
        is_substring = True
        for j in range(len(a_substring)):
            if a_string[i + j] != a_substring[j]:
                is_substring = False
        if is_substring:
            return True
    return is_substring

print(does_it_contain('aababcabcd', 'abc'))
print(does_it_contain('xy', 'abc'))
print(does_it_contain('hello there i am a robot', 'there'))