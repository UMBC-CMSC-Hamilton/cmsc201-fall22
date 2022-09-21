"""
    review first:
    conditionals again, if, elif, else
        nesting
        
    range, lists, and for - "topic for today"
"""
if False:
    animal = input('Tell me an animal: ')
    if animal == 'penguin':
        print('Go back to the south pole')
    elif animal == 'lion':
        print('please dont eat me')
    elif animal == 'pelican':
        print('What is up with you, how has evolution worked?')
    else:
        print('you are a cow')
    
    x = int(input('Tell me x: '))
    
    """
        Order of if statements matters
            only one of the if-elif-else will ever run
        
        How many else clauses can you have?
            only one, maybe zero.
    """
    if x > 3:
        print('x is bigger than 3')
    elif x > 4:
        print('x is bigger than 4')
    elif x > 5:
        print('x is big')
    else:
        print('huh?')
    
    """
        Nesting - put an if statement into another if statement
    """
    
    """
        Rock beats scissors
        scissors beats paper
        paper "covers" rock
    """
    player_one = input("Player one choose rock paper scissors: ")
    player_two = input("Player two choose rock paper scissors: ")
    
    if player_one == 'rock':
        if player_two == 'paper':
            print('Player two wins')
        elif player_two == 'scissors':
            print('Player one wins')
        elif player_two == 'rock':
            print('tie')
        else:  # assume that you entered rock
            print('Player two did not enter a valid thing.')
    elif player_one == 'paper':
        if player_two == 'paper':
            print('tie')
        elif player_two == 'scissors':
            print('Player two wins')
        elif player_two == 'rock':
            print('Player one wins')
        else:  # assume that you entered rock
            print('Player two did not enter a valid thing.')
    elif player_one == 'scissors':
        if player_two == 'paper':
            print('Player one wins')
        elif player_two == 'scissors':
            print('tie')
        elif player_two == 'rock':
            print('Player two wins')
        else:  # assume that you entered rock
            print('Player two did not enter a valid thing.')
    else:
        print('Player one did not enter a valid thing.')
    
    
    small = input('Are you rather small? ')
    if small == 'yes':
        miners = input('Do you really like mining? ')
        if miners == 'yes':
            print('You are Gimli')
        else:
            ring = input('Did you carry a ring of power for a while?')
            if ring == 'yes':
                birthday = input('Did you have a 111th birthday?')
                if birthday == 'yes':
                    print('You are Bilbo')
                else:
                    print('You are Frodo')
            else:
                gardener = input('Are you a gardener? ')
                if gardener == 'yes':
                    print('You are Samwise')
                else:
                    palentir = input('How do you feel about palintirs? good/bad')
                    if palentir == 'good':
                        print('You are pippin')
                    else:
                        print('You are Merry')

"""
    loops - for loops in particular
    
    loops allow us to repeat code multiple times
        loops through a set of options
"""

# range starts at 0, goes up by 1 until it reaches the endpoint - 1
for i in range(5):
    print(i)


total = 0
# for <index variable>
for i in range(10):
    print(i, total)
    # total = total + i
    total += i

print(f'The final answer is: {total}')

"""
    For loops and lists work together in python
"""
a_list = [3, 4, 5, 6, 12, -3, 0, 14]
string_list = ['hello', 'zebra', 'canopy', 'shrimp', 'word']
weird_list = [True, 5, 'zebra', 'cat', 3.14, False]
print(a_list)
print(string_list)
print(weird_list)
"""
    weird list is of "mixed type"
"""

empty_list = []
another_empty_list = list()
empty_list.append("hi")
empty_list.append(3)
empty_list.append('robots')
print(empty_list)

# maybe not allowed:
empty_list.insert(2, 'c')
print(empty_list)

"""
a_list = [3, 4, 5, 6, 12, -3, 0, 14]
          0  1  2  3  4    5  6  7
string_list = ['hello', 'zebra', 'canopy', 'shrimp', 'word']
                0         1        2         3         4
We index into a list to get specific elements
"""
# list brackets (indexing operator)
print(a_list[3], a_list[5], a_list[6])
print(string_list[3], string_list[0])

"""
    Indexing also allows us to modify a list
"""
a_list[6] = 17
print(a_list)

# since there's no 44th element, this will give us an IndexError
# print(a_list[44])
if False:
    five_things = []
    for index in range(5):
        a_thing = input('Tell me a thing: ')
        five_things.append(a_thing)
    
    print(five_things)
    
    a_new_variable = int(input('How many things?!?!? '))
    if 1 <= a_new_variable <= 20:
        some_things = []
        for index in range(a_new_variable):
            a_thing = input('Tell me a thing: ')
            some_things.append(a_thing)
        
        print(some_things)
    else:
        print('Too many things probably.')
    
thing_list = ['a thing', 'the thing', 'crazy thing', 'wild thing', 'car thing', 'something', 'nothing', 'yet another thing', 'interesting list', 'lightsaber', 'laser sword', 'monkey']
thing_count = 0
for x in thing_list:
    """
        For each loop, notice that it takes an element out of the list
        assigns it (temporarily into x)
    """
    print(x)
    # x is a string, in operator returns True if 'thing' is a substring
    if 'thing' in x:
        thing_count += 1

print(thing_count)

print('thing' in 'bigger thing')
print('thing' in 'xtxhxixnxg')


"""
    For-i loop loops by index, not by element
"""
total_squares = 0
for index in range(len(a_list)):
    total_squares += a_list[index] ** 2

print(total_squares)

"""
    Add up all the even numbers from a list
"""
even_total = 0
for index in range(len(a_list)):
    if a_list[index] % 2 == 0:
        even_total += a_list[index]

print(even_total)
