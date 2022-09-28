"""
    a little bit more about for loops
    nested for loops
    2 dimensional lists
"""

"""
    prime test
    
    if you have an integer n its only factors are 1 and n, it is prime
        otherwise we say it is composite
"""

an_int = int(input('Tell me an integer: '))
is_prime = False

if an_int <= 0:
    # is prime is not declared here, so declare it above the if
    print('Enter a positive integer. ')
elif an_int == 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, an_int):
        if an_int % i == 0:
            is_prime = False

if is_prime:
    print(f'{an_int} is prime')
else:
    print(f'{an_int} is composite')

"""
    What if we want to modify this example in order to
        calculate all the factors of the number.
"""
factor_list = []
for i in range(1, an_int):
    if an_int % i == 0:
        factor_list.append(i)

print(factor_list)
total = 0
for x in factor_list:
    total += x

if total == an_int:
    print('That is a perfect number')
else:
    print("That is not perfect. ")

"""
    Nesting loops.
        for loop inside of a for loop, that's called nesting
    
"""

for i in range(5):
    for j in range(4):
        print(f'({i}, {j})', end='\t')  # normally end = '\n'
    print()  # this print statement basically gives a new line

"""
    \t = tab
    \n = newline
    \\ = backslash
    \r = carriage return
    
    Linux = \n, Mac = \n
    Windows = \r\n
"""
# no, not on test, too weird for test
print('hello', end='\r')
print('maybe this now')

a_list = [2, 4, 2, 6, 8, 9, 12, 2, 7, 8]
# let's detect if there's duplicates
dup_count = 0
for i in range(len(a_list)):
    for j in range(len(a_list)):
        if i != j and a_list[i] == a_list[j]:
            print(f'Match found at ({i}, {j}), {a_list[i]}')
            dup_count += 1

print('The number of duplicates is: ', dup_count // 2)

# Assume: j > i
dup_count = 0
for i in range(len(a_list)):
    for j in range(i + 1, len(a_list)):
        if i != j and a_list[i] == a_list[j]:
            print(f'Match found at ({i}, {j}), {a_list[i]}')
            dup_count += 1

print(dup_count)

for i in range(len(a_list)):
    for j in range(i + 1, len(a_list)):
        print(f'({i}, {j})', end='\t')
    print()

n = int(input('Tell me the size: '))
for i in range(n, -1, -1):
    for j in range(i + 1):
        print('*', end='')
    print()

for i in range(n):
    # sometimes you may need n - i - 1 or n - i + 1 depending
    for j in range(n - i):
        print('*', end='')
    print()

"""
    Now I want to talk about 2d lists
        A 2d list is a list of lists
"""
#  indices:       0          1
my_2d_list = [[1, 2, 3], [4, 5, 6]]
print(len(my_2d_list))
print(my_2d_list[1], my_2d_list[0])
print(my_2d_list[1][0])

my_2d_list[1].append(45)
my_2d_list[1].append(78)

my_2d_list.append([7, 8, 9])
my_2d_list.append([10, 11, 12])
print(my_2d_list)

total = 0
for i in range(len(my_2d_list)):
    for j in range(len(my_2d_list[i])):
        total += my_2d_list[i][j]

print('The total is', total)

# cool
hypothetically = [[1, 2], [4, 3], [7, 2], [9, 12], [15, 1]]

"""
    Next elements, previous elements, elements with index skip
"""
my_word = input('Tell me word: ')
# capitals mean constants, lower case means variables
# constant is a variable that doesn't change
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
"""
    I want to test to see if two vowels are next to each other.
"""
pairs = 0
for i in range(len(my_word) - 1):
    if my_word[i] in VOWELS and my_word[i + 1] in VOWELS:
        print(my_word[i], my_word[i + 1])
        pairs += 1

pairs = 0
# be careful of negative indices
for i in range(1, len(my_word)):
    if my_word[i] in VOWELS and my_word[i - 1] in VOWELS:
        print(my_word[i], my_word[i - 1])
        pairs += 1

print(pairs)

# anti-diagonal = 3, 6, 2
# diagonal = 1, 6, 12
square_list = [[1, 2, 3],
               [7, 6, 0],
               [2, 5, 12]]

total = 0
for i in range(len(square_list)):
    total += square_list[i][i]

print(total)

"""
    Challenge: do this for the anti-diagonal.
"""