"""
    What is recursion?
        recursion is a process where you call a function within itself
"""

import time


def countdown(n):
    """
        All recursions need a base case
            A base case is a part of the recursive function
                that doesn't actually call any recursions
            If we don't have a base case, then you get 'infinite'
                recursions.
            Python will keep track of the number of recursive calls
                it will throw a RecursionError if you call the
                same function recursively 1000 times.
    """
    if n == 0:
        print('Blastoff')
        return
    
    print(f'T - {n} seconds and counting...')
    time.sleep(1)
    countdown(n - 1)


def non_rec_countdown(n):
    for i in range(n, 0, -1):
        print(f'T - {i} seconds and counting...')
        # time.sleep(0.1)
    print('Blastoff')


# non_rec_countdown(1000000)  # not doable with the recursion

"""
Real example of recursion, calculate factorial:

n! = 1 if n == 0
   = n * ((n - 1)!) if n > 1
   
5! = 1 * 2 * 3 * 4 * 5 = 5 * 4 * 3 * 2 * 1
   = 5 * 4! = 120
4! = 4 * 3! = 24
3! = 3 * 2! = 6
2! = 2 * 1! = 2
1! = 1 * 0! = 1

number of ways to choose 0 things out a bag = 1
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_slow(n):
    if n == 0:
        print(f'Base case, n = 0, returning 1')
        return 1
    else:
        print(f'Calling factorial({n - 1}) from factorial({n})')
        time.sleep(0.5)
        fac = factorial_slow(n - 1)
        time.sleep(0.5)
        print(f'Calculating result and returning from factorial({n}) {n * fac}')
        return n * fac


"""
    Fibonacci numbers: add up the two previous things
        Story: rabbits
            immortal
            they are juvenile for one month
            they produce perfect breeding pairs
    fib(0) = fib(1) = 1
    fib(n) = fib(n - 1) + fib(n - 2)
    
    fib(5) = fib(4) + fib(3) = 5 + 3 = 8
    fib(4) = fib(3) + fib(2) = 3 + 2 = 5
    fib(3) = fib(2) + fib(1) = 2 + 1 = 3
    fib(2) = fib(1) + fib(0) = 1 + 1 = 2
"""
def fibonacci(n):
    if n < 2:
        return 1
    else:
        print(f'Calling fibonacci({n - 1})')
        time.sleep(0.25)
        fn_minus_1 = fibonacci(n - 1)
        time.sleep(0.25)
        print(f'Calling fibonacci({n - 2})')
        time.sleep(0.25)
        fn_minus_2 = fibonacci(n - 2)
        time.sleep(0.25)
        print(f'Calculating fibonacci({n}) = {fn_minus_1} + {fn_minus_2}')
        return fn_minus_2 + fn_minus_1
    

x = int(input('>> '))
while x != -1:
    print(fibonacci(x))
    x = int(input('>> '))