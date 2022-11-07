"""
    What is recursion?
        recursion is a process which calls itself
                       (function)
    
    G = GNU
    GNU = GNU is Not Unix
        = (GNU is Not Unix) is Not Unix
        
    Linux and Unix, "GNU", GNU public license
"""


import time


def factorial(n):
    if n == 0:
        # base case, prevent infinite recursion
        return 1
    else:
        print(f'factorial({n}) waiting, Calling factorial ({n - 1})')
        time.sleep(0.5)
        fact = factorial(n - 1) # just one recursive call!
        time.sleep(0.5)
        print(f'factorial({n}) calculating result')
        return n * fact
        # non branching recursion

def it_fact(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

# print(factorial(20))
"""
    recursive functions wait in a stack = last in first out
"""

def fibonacci(n):
    if n < 2:
        return 1
    else:
        # when you call more than one recursion I tend to call this "branching recursion"
        return fibonacci(n - 1) + fibonacci(n - 2)
    

def iterative_fibonacci(n):
    prev_prev = 1 # index 0
    prev = 1 # index 1
    current = 1
    for i in range(2, n + 1):
        current = prev + prev_prev
        # correct order to "shift it down"
        prev_prev = prev
        prev = current
        # the other order would overwrite
    
    return current


def test_fib():
    x = int(input('>> '))
    while x != -1:
        print(iterative_fibonacci(x))
        x = int(input('>> '))


def as_and_bs(length, current):
    """
        can it be done iteratively? yes
        should it be done iteratively? it's a little harder...
    """
    if length == 0:
        print(current)
    else:
        as_and_bs(length - 1, current + '0')
        as_and_bs(length - 1, current + '1')

"""
    if a function doesn't return anything, in python:
        it actually has a secret return None at the end.
"""
"""
    let's do something "interesting"
    modify the as and b's process to only use exactly k a's.
    length = the length
    num_as = another input
"""

def k_as_and_bs(length, k, current):
    """
        can it be done iteratively? yes
        should it be done iteratively? it's a little harder...
    """
    count = 0
    
    if length == 0:
        if k == 0:
            print(current)
            return 1
    else:
        # if i add an a to the string, how many more do i need?
            # k - 1 more
        count += k_as_and_bs(length - 1, k - 1, current + 'a')
        # the number of a's doesn't change, need the same number
            # k more
        count += k_as_and_bs(length - 1, k, current + 'b')
    
    return count

def test_k_as_and_bs():
    # my_list = []
    # for x in input('>> ').split():
    #     my_list.append(int(x))
    n, k = [int(x) for x in input('>> ').split()]
    while n != -1:
        print(k_as_and_bs(n, k, ''))
        n, k = [int(x) for x in input('>> ').split()]
    
    print(it_fact(20) // (it_fact(10) * it_fact(10)))


"""
    let's do a string replace function recursively
    big_string, letter to replace, what to replace it with

    two cases:
        either the first thing is the letter
            replace it then recursively call it on the rest of the string
        if not, just add on the first letter of big_string and
            calculate the rest of the replacement
"""
def rec_replace(big_string, letter, replace_with):
    if not big_string:
        return ''
    else:
        """
            the first letter is all we work on
                cut off the first letter, call the function again
                to do the replacement on the "next" letter
            trust exercise = trust that the recursion is going to
                return the correct partial answer to you
                
        """
        print(big_string, big_string[0])
        if big_string[0] == letter:
            return replace_with + rec_replace(big_string[1:], letter, replace_with)
        else:
            # big_string[1:] cuts off the first letter
            return big_string[0] + rec_replace(big_string[1:], letter, replace_with)


print(rec_replace('abbababaabab', 'a', 'z'))


def count_up(n):
    if n == 0:
        return 0
    else:
        c = count_up(n - 1)
        print(f'i am count_up({n}) and I get {c} from the previous step and add one')
        return 1 + c
        # what does the recursion above me need?


print(count_up(10))

"""
    Motivation:
        DFS = depth first search
        Robovac
            path find around a room
            blind, can't see the room
            - search every position
            - searching for some kind of special item
            iterative solution is "not possible"
"""