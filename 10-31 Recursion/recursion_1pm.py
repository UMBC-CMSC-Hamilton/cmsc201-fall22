"""
    Let's talk about recursion

    Alert: do not do this on project 1 and probably not project 2.
        Not illegal, you are allowed, but beware.
"""

"""
    Fun fact: you can call a function from within itself.
"""
import time

def countdown(n):
    # base case is a piece of code in a recursive function
    # that does not recurse
    if n == 0:
        print('Blastoff')
        return
    """
        Why do we need a base case?
            prevents infinite recursion/ RecursionError (1000x)
    """
    
    print(f'T - {n} seconds')
    time.sleep(1)
    countdown(n - 1)
    """
        recursive case, it calls itself
    """

"""
    factorials
    
    n! = 1 if n = 0
         n * ((n - 1)!) if n > 0
         
    0! = 1 (base case, gamma function)
    1! = 1 * 0! = 1 * 1 = 1
    2! = 2 * 1! = 2  * 1 = 2
    3! = 3 * 2! = 3 * 2 * 1 = 6
    4! = 4 * 3! = 4 * 3 * 2 * 1 = 24
    5! = 5 * 4! = 5 * 24 = 120
    6! = 6 * 5! = 6 * 120 = 720
"""
def rec_fact(n):
    time.sleep(0.5)
    if n == 0:
        print('Base case, returning 1')
        return 1
    else:
        print(f'n = {n} waiting on rec_fact({n - 1})')
        value = n * rec_fact(n - 1)
        print(f'rec_fact({n}) not waiting anymore, value = {value}')
        time.sleep(0.5)
        return value
    

def fact(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


"""
    Fibonacci :)
    fib(0) = fib(1) = 1 [ base cases]
    n >= 2:
    fib(n) = fib(n - 1) + fib(n - 2)
"""

def fibonacci(n):
    if n < 2:
        return 1
    else:
        time.sleep(0.5)
        print(f'fib({n}) Waiting on fib({n - 1}), fib({n - 2}) ')
        val1 = fibonacci(n - 1)
        time.sleep(0.5)
        print(f'fib({n}) Waiting on fib({n - 2}) ')
        time.sleep(0.5)
        val2 = fibonacci(n - 2)
        print(f'fib({n}) calculating result {val1} + {val2} = {val1 + val2}')
        return val1 + val2

def test_fibonacci():
    x = int(input(">> "))
    while x != -1:
        print(fibonacci(x))
        x = int(input(">> "))


def as_and_bs(length, current):
    if length > 0:
        as_and_bs(length - 1, current + 'a')
        as_and_bs(length - 1, current + 'b')
    else:
        print(current)


x = int(input('>> '))
while x > 0:
    as_and_bs(x, '')
    x = int(input('>> '))
