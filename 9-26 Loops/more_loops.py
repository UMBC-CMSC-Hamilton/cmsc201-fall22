"""
    for loops
        nested for loops
        2d arrays/lists
    
    while loops
"""

# test if a number is prime
# if a number is prime, the only number that can divide it
#  from 1, ... p - 1 is 1.
a_number = int(input('Enter a number to test: '))

# define variables before if statements or for loops
# if you're only going to define it in some of the branches
# if you're going to use that variable afterward
is_prime = False
if a_number <= 0:
    print('Only Positives Please')
elif a_number == 1:
    print('One is an exception')
else:
    is_prime = True
    for i in range(2, a_number):
        if a_number % i == 0:
            is_prime = False  # flag variable/boolean flag

if is_prime:
    print(f'{a_number} is prime')
else:
    print(f'{a_number} is not prime')

"""
    I want a list of factors of a number
"""
factor_list = []
for i in range(2, a_number):
    if a_number % i == 0:
        factor_list.append(i)

print(factor_list)

# moat, queueing, float, flight
# Let's count the number of times that vowels occur next to each other
the_word = input('Enter a word').lower()
# or: the_word = the_word.lower()

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

count = 0
for i in range(len(the_word) - 1):
    if the_word[i] in VOWELS and the_word[i + 1] in VOWELS:
        print('We found a pair', the_word[i], the_word[i + 1])
        count += 1

print(count)

"""
    You can also nest for loops
"""
"""
\n = new line
\t = tab
\\ = a single backslash
\r = carriage return
\a = doesn't really work anymore :(

Windows = \r\n
"""
for i in range(5):
    for j in range(3):
        print(f'({i}, {j})', end="\t")
    print()

"""
    Want to detect duplicates
"""
count_duplicates = 0
my_list = [2, 6, 7, 9, 12, 4, 6, 8, 6, 3, 1, 9]
for i in range(len(my_list)):
    for j in range(len(my_list)):
        # print(f'[{my_list[i]}, {my_list[j]}]', end='\t')
        if i != j and my_list[i] == my_list[j]:
            print(f'[At Index: ({i}, {j}), the match is: {my_list[i]}, {my_list[j]}]')
            count_duplicates += 1

print(count_duplicates // 2)

"""
len(my_list) = 4
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
    
    
i = 0: j = 1, 2, 3
i = 1: j = 2, 3
i = 2: j = 3
i = 3: j = range(4, 4)

"""
print('does it print?')
for x in range(4, 4):
    print('If this prints I get money')

count_duplicates = 0
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if i != j and my_list[i] == my_list[j]:
            print(f'[At Index: ({i}, {j}), the match is: {my_list[i]}, {my_list[j]}]')
            count_duplicates += 1

"""
    Challenge exercise:
        only print out an additional 1 for each new number that
            occurs
"""

"""
    2d-Lists

    Like we have nested for loops that have an inner and outer loop
    we can have lists inside of lists
"""

# don't index into a number accidentally
# my_fake_2d_list = [1, 2, 3, 4, 5, 6]
# print(my_fake_2d_list[0][2])

#               index 0   index 1
my_2d_list = [[1, 2, 3], [4, 5, 6]]

print(my_2d_list[0])
print(my_2d_list[1])

print(my_2d_list[0][2])

my_2d_list.append([7, 8])
print(my_2d_list)

my_2d_list[1].append(23)
my_2d_list[1].append(77)
print(my_2d_list)

for x in range(len(my_2d_list)):
    # need to take the length of the inner list not the outer list
    for y in range(len(my_2d_list[x])):
        print(x, y, my_2d_list[x][y])


square_list = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

total = 0
for i in range(len(square_list)):
    total += square_list[i][i]

print(total)

"""
    Challenge: write code that checks to see if a 2d list is square
"""