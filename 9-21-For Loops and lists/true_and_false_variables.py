x = None
if x:
    print(f'hello, x = {x} is true')
else:
    print(f'Sadly x = {x} is false')
    
"""
    What evaluates as True / False?
        ints/floats all True except 0 (0.0) which is False
        booleans True == True, False == False, as expected
        strings all True except empty string
        
        What about lists?
            all true except empty list.
        What about dictionaries?
            all true except the empty ones.
        
        None = always false
"""

n = int(input('Number: '))
if n % 2 == 0:
    print('it is even')
else:
    print('it is odd')

if n % 2:
    print('it is odd')
else:
    print('it is even')

if not(n % 2):
    print('it is even')
else:
    print('it is odd')

"""
    Why do computer scientists care about parity/evenness/oddness?
        two player game
        
"""

for turn_count in range(20):
    if not(turn_count % 2):
        print('it is player ones turn')
    else:
        print('it is player twos turn')
    turn_count += 1


"""
    One last thing:
"""

print(__name__)

if __name__ == '__main__':
    print('hi')
    # put all of your code inside this if statement


