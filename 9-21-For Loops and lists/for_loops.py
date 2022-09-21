"""
    For loops and lists

        If you have to cycle through a list of things,
            want to go over a set of indices, you may need a for loop.

        For loops are the first way to repeat code.
"""

my_list = ['a', 'b', 'c', 'd', 'e']
#           0    1    2    3    4
# for i loop: indices
for letter_index in range(len(my_list)):
    print(letter_index, my_list[letter_index])

# for each loop - instead of indices, it gives us the element
#       in the list
# problem - we don't know the index in the list.
for letter in my_list:
    print(letter)
    
    
a_count = 0
list_of_words = ['happy', 'robot', 'sandwich', 'fluffy', 'cat']
for word in list_of_words:
    if 'a' in word:
        a_count += 1

print(f'the number of words with a\'s is {a_count}')

"""
    in operator tests for substring
    What is a substring?
        "all" in "allowance"
"""
# is a substring
print('all' in 'allowance')
# not a substring
print('all' in 'axlxl')
# is a substring
print('xyz' in 'aaaaaaxyzaaaaaaa')
# not a substring
print('xyz' in 'xylophone zebra')
# not a substring
print('abc' in 'bac')
if False:
    start = int(input('Where to start? '))
    stop = int(input('Where to stop? '))
    # range starts at the first argument, goes up to the second argument
    # doesn't include it.
    # start, start + 1, start +2 , ... stop - 1
    for i in range(start, stop):
        if i % 1000000 == 0:
            print(i, end=' ')
        
print('done')
# checks to make sure you can reach the start from the stop
# if you can then the loop will run
# if you can't then no. - any invalid range will not run
#  doesn't mean that you will be stopped from running a very
#       very very very long for loop.
print()

"""
    All three argument of range:
        range(start, stop, step)
        start, start + step, start + 2* step, start + 3 * step ...
        passes stop - 1
        
    by default step = 1
"""
for i in range(1, 500, 7):
    print(i)
    
for i in range(10, 0, -1):
    print(i)


for i in range(10, -1, -1):
    print(i)


# 1/25 2/25 3/25... 25/25
for i in range(1, 26):
    print(f'{i}/25 = {i/25}')

# stderr is usually faster than stdout
#  floats aren't allowed inside range
# for i in range(0.0, 1.0, 0.04):
#     print(i)

list_of_things = []
# both create an empty list
#    list_of_things = []
#   list_of_things = list()
n = int(input('Tell me n: '))
for i in range(n):
    # append will add things to the end of a list
    list_of_things.append(input('Tell me thing: '))

print(list_of_things)

new_list = []
for create_index in range(25):
    new_list.append(True)

print(new_list)

"""
    Mutability - a variable/object can change
    
    Basic Data Types == Immutable
        string
        float
        int
        bool
        None
    Mutable = List
"""


# strings are a lot like lists:
my_string = "hello there"
for i in range(len(my_string)):
    print(my_string[i])

# if you want to change an element in a list, you can do this:
new_list[17] = False
print(new_list)

# can i change elements in a string? no actually

# my_string[2] = 'x'


my_favorite_string = input('Tell me a string: ')
# replace all a's with x's
# how do you modify a string?
# convert into a list
print(my_favorite_string)
my_string_list = list(my_favorite_string)
# but you can modify this list
for i in range(len(my_string_list)):
    if my_string_list[i] == 'a':
        my_string_list[i] = 'x'

print(my_string_list)
# not quite done yet.
# use a function called join
print(''.join(my_string_list))
# the empty string is called the "separator" gets inserted between elements of the list

"""
    Which things evaluate as True and False?
        some variables evaluate as true, others as false
"""


