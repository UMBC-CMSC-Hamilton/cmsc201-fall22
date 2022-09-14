"""
    conditionals are if statements
    syntax: if then a colon
        condition has to evaluate to either True or False
    if <condition>:
        all code inside of if must be tabbed by 1
        this is still inside of the if
        this is also inside

    this is not inside of the if statement anymore

    boolean operators
        not = highest precedence
        and
        or = lowest precedence

    1) algebra
    2) comparison operators
        ==, !=, <, >, <=, >=
    3) logical/boolean operators

    1) elif and else
    2) Nesting if statements
"""

x = int(input('tell me int: '))
"""
if x > 0:
    print('x is positive')
"""
# if i enter -3, nothing happens
# we want code that executes when the if statement is false

if x > 0:
    print('x is positive')
else:  # else then a colon
    print('x is either zero or negative')


x = int(input('Enter numerator: '))
y = int(input('Enter denominator: '))

if y != 0:
    print('The fraction is equal to', x/y)
else:
    print('The denominator is zero, cannot divide.')

correct_password = "secret password1"
password = input('Enter the password: ')
if password == correct_password:
    print('You have logged in')
    logged_in = True
else:
    print('Incorrect password, you have not logged in.')
    logged_in = False

if logged_in:
    my_number = int(input('Pick a number between 1 and 10'))

"""
    What is "elif"?
    
    else if = if the first if statement isn't true, try this one instead.
    else if = linked to the if statement above it, it only checks if its true whenever the if statement
    is false.
"""

x = int(input('Give me number between 1 and 10: '))
if 1 <= x <= 10:
    print('You have chosen correctly.')
elif x > 10:
    print('You are too high.')
else:
    print('Too low!')


"""
    if elif and else only will have one of them execute in a given run.
    
"""
number_of_apples = int(input('How many apples? '))
if number_of_apples < 0:
    print('That doesnt\'t make sense. Pick a non-negative number.')
elif number_of_apples < 12:
    print('You have less than a dozen')
elif number_of_apples == 12:
    print('You have exactly a dozen')
else:
    print('You have more than a dozen.')

""" what happens if we delete the elif statements? """

if number_of_apples < 0:
    print('That doesnt\'t make sense. Pick a non-negative number.')
"""
   This if statement here is separate 
"""
if number_of_apples < 12:
    print('You have less than a dozen')
"""
   This if statement here is separate 
"""
if number_of_apples == 12:
    print('You have exactly a dozen')
else:
    print('You have more than a dozen.')

"""
    Yes you can put if statements inside each other.  Called nesting. 

    You are allowed to use as many elif's as you want. If statements don't really get us anything 
    smarter than this.  
    
    only one if - that's how you start the statement
    only else else - otherwise it doesn't make sense to python
        number of else's is 0 or 1 (don't need to have else, but you can)
        else has to be at the end of the if/elif-s
"""

day_of_week = input('Tell me a day of the week: ')
if day_of_week.lower() == 'monday':
    print('Garfield hates mondays.')
elif day_of_week.lower() == 'tuesday':
    print('Tuesdays are much like mondays, except one more day.')
elif day_of_week.lower() == 'wednesday':
    print('Wednesday, half way through')
elif day_of_week.lower() == 'thursday':
    print('Thursday, almost there')
elif day_of_week.lower() == 'saturday' or day_of_week.lower() == 'sunday':
    print('It\'s the weekend')
elif day_of_week.lower() == 'friday':
    print('Friday, made it to the end')
else:
    print('That is not a day of the week.')

"""
    what is pass?
        pass is no-op noop, nop
        no operation = does nothing
    Why do we need a line of code that does nothing?
        Leave a placeholder for future code.
        in an if statement all the code needs to tabbed in by 1 level
    Pass doesn't actually do anything.
"""
"""
    Nesting if statements:
        put an if statement inside of an if statement, that is called nesting. 
        Preferable to have if-elif-else than to nest
            
"""
right_or_left = input('Do you want to turn right or left? ')
if right_or_left == 'right':
    apples = int(input('How many apples do you take? '))
    if apples >= 12:
        print('You have chosen a dozen or more apples')
    else:
        print('You have chosen less than a dozen.')
elif right_or_left == 'left':
    oranges = int(input('How many oranges do you take? '))
    if oranges == 13:
        print('You have chosen a bakers dozen.')
    else:
        print('You have not chosen a bakers dozen. ')
else:
    print('You need to enter right or left. ')

x = int(input('INT!!! '))
if x > 1:
    print('x is bigger than 1')
    if x > 2:
        print('x is bigger than 2')
        if x > 3:
            print('x is bigger than 3')
            if x > 4:
                print('x is bigger than 4')
                if x > 5:
                    print('x is bigger than 5')
print('Second time: ')
# start with the most specific thing and go to the more general
if x > 5:
    print('x is bigger than 5')
elif x > 4:
    print('x is bigger than 4')
elif x > 3:
    print('x is bigger than 3')
elif x > 2:
    print('x is bigger than 2')
elif x > 1:
    print('x is bigger than 1')

"""
    What happens if we flip the order?
"""
print('Third time: ')
if x > 1:
    print('x is bigger than 1')
elif x > 2:
    print('x is bigger than 2')
elif x > 3:
    print('x is bigger than 3')
elif x > 4:
    print('x is bigger than 4')
elif x > 5:
    print('x is bigger than 5')
"""
    note here that if you use x = 7 for instance, it will become true when x > 1, 
        and it won't check x > 2, x > 3 ... etc, because it's already found a true one.  
"""

"""
    Mod = modulus division (HW2 may use mod)
        Idea of remainder.
        
    Remember back when you learned division
    
        5/3 = 1.66666666...
        Go back earlier:
        5/3 = 1 Remainder 2 <--- the remainder is 'mod'
        
    17/5 = 3 R 2
    20/4 = 5 R 0
    6 / 7 = 0 R 6
    
    In programming, you may see instances where you want to test if something is divisible
    
    Symbol = % <- mod symbol
"""
print(17 % 5, 20 % 4, 6 % 7)
print(4 % 2, 9 % 5, 8 % 3, 244 % 7)
"""
    Think before we hit go:
        4 / 2 = 2 R 0
        9 / 5 = 1 R 4
            1(5) + 4 = 9
        8 / 3 = 2 R 2
            2(3) + 2 = 8
        244 / 7 = 34 R 6
            244 = 7(34) + (6)
"""

"""
    First thing we often need with mod is to test if a number is even or odd:
        number % 2 == 0 means that the number is divisible by 2 (definition of even)
        number % 2 == 1, number = 2 * N + 1 ==> definition of an odd number.  
"""
x = int(input('Tell me an integer: '))
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')
"""
    0 is an even number (it can be divided by 2) 0/2 = 0 an integer (not a half value)  0 = 2(0)
"""

""" Days of the month 
September 1st = Thursday
September 2nd = Friday
September 3rd = Saturday
September 4th = Sunday
September 5th = Monday
September 6th = Tuesday
September 7th = Wednesday
September 8th = Thursday
September 9th = Friday
September 10th = Saturday
September 11th = Sunday
September 12th = Monday
"""
# all of the thursdays of the month are equal to 1 mod 7, nice
# all of the fridays of the month are 2 mod 7
# all of the saturdays of the month are 3 mod 7
print(1 % 7, 8 % 7, 15 % 7, 22 % 7)
# be careful about that... 7 % 7 = 0 because it has no remainder
print(7 % 7)

day_of_month = int(input('Enter what day of september it is: '))
if day_of_month % 7 == 0:  # 7 won't work, but 0 will work
    print('It is Wednesday')
elif day_of_month % 7 == 1:
    print('It is Thursday')
elif day_of_month % 7 == 2:
    print('It is Friday')
elif day_of_month % 7 == 3:
    print('It is Saturday')
elif day_of_month % 7 == 4:
    print('It is Sunday')
elif day_of_month % 7 == 5:
    print('It is Monday')
elif day_of_month % 7 == 6:
    print('It is Tuesday')


# what happened to wednesday?
"""
    Remember that number % number == 0 <-- 
    0 is a possible answer for mod, always remember that 0 can happen.
"""

"""
    Mod IN PYTHON BEWARE
"""

print(-3 % 7)  # mathematicians version of mod

# -3 / 7 = 7(0) - 3 <-- why not?
# remainders are non-negative in python
# -3/7 = 7(-1) + 4 = -7 + 4 = -3 yes that's right
# C++ doesn't do that

"""
    Choose your own adventure/what character is this?

    Star Trek = I love trek.  but... Star Wars this time.  
"""

furball = input('Are you a gigantic furball? ')
if furball == 'yes':
    print('You are a wookie. ')
    am_i_chewbacca = input('Are you chewbacca? ')
    if am_i_chewbacca == 'yes':
        print('You are indeed Chewbacca, you deserve a medal. ')
    else:
        print('You are another wookie, you also probably deserve a medal.')
elif furball == 'no':
    jedi = input('Are you a jedi? ')
    if jedi == 'yes':
        vader_hand = input('Did Darth Vader cut off your hand? ')
        if vader_hand == 'yes':
            print('You are Luke Skywalker.  ')
            # count dooku also may be in here
        else:
            hello_there = input('Do you say hello there a lot? ')
            if hello_there == 'yes':
                print('You are Obi Wan!')
    else:
        smuggler = input('Are you a smuggler with a heart of gold? ')
        if smuggler == 'yes':
            did_you_shoot_first = input('Did you shoot first? ')
            if did_you_shoot_first == 'yes':
                print('You are Han Solo')
            else:
                print('You are Lando Calrissian')
