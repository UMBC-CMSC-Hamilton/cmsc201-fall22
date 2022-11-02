"""
    What is recursion?
        a function that calls itself
        
    Usually better to find a non-recursive algorithm, solution
        to a problem.
    Sometimes it's hard to find that solution,
        sometimes it just doesn't exist
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def non_recursive_factorial(n):
    """
        iterative solution
        "idea of a next thing"
        iterate while there's a next thing to take
    :param n:
    :return:
    """
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


def fibonacci(n):
    """
        1 pair of rabbits
            rabbits are 'juvenile' for one month
            after that they produce 1 additional pair for every month
            rabbits are immortal
        1, 1, 2, 3, 5, 8, ...
        :param n:
        :return:
    """
    # print(f'calculating fib{n}')
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def list_fibonacci(n):
    fib_list = [1, 1]
    for i in range(2, n + 1):
        # fib_list.append(fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2])
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    print(fib_list)
    return fib_list[n]


def test_fibonacci():
    x = int(input("x >> "))
    while x != -1:
        print(list_fibonacci(x), fibonacci(x))
        x = int(input("x >> "))

"""
    I want to write a function that gives me all possibilities
        of a's and b's with a certain length
        
    L = 1 a, b
    L = 2 aa, ab, ba, bb
    L = 3 aaa, aab, aba, abb, baa, bab, bba, bbb
    L = 4 aaaa, aaab, aaba, aabb, abaa, abab, abba, abbb
          baaa, baab, baba, babb, bbaa, bbab, bbba, bbbb
"""
import time

def print_as_and_bs(length, current):
    """
        can be done iteratively, but it's somewhat hard
    """
    if length == 0:
        time.sleep(0.5)
        print(current)
    else:
        time.sleep(0.5)
        print_as_and_bs(length - 1, current + 'a')
        time.sleep(0.5)
        print_as_and_bs(length - 1, current + 'b')


"""
    only want to print things with exactly k b's
"""
def print_as_and_bs_k(length, k, current):
    """
        can be done iteratively, but it's somewhat hard
    """
    # length == 0 and k == 0, length == 0 k > 0 'aaaaaaaaa'
    # only want strings of length "length" so we need to terminate
    # the recursion whenever we see something of the right length
    # only print it if the number of k's is right.
    if length == 0:
        if k == 0:
            print(current)
    elif k < 0:
        return
    else:
        # why? because if i add an 'a' not a b, we don't count it
        print_as_and_bs_k(length - 1, k, current + 'a')
        # if i add a b, how many MORE b's do i need? k - 1
        print_as_and_bs_k(length - 1, k - 1, current + 'b')


def test_as_and_bs():
    x, y = map(int, input("x >> ").split())
    while x != -1:
        print_as_and_bs_k(x, y, '')
        # lazy Eric
        x, y = map(int, input("x >> ").split())

# print(factorial(20) // (factorial(10) * factorial(10)))


def string_replace(the_string, the_letter, the_replacement):
    """
    if the first character in the_string is the_letter
        replace it
        return the_replacement + the_string[1:] (the rest of the string)
    else:
        don't replace it
        return the_string[0] + string_replace(the_string[1:)...
        
    :param the_string: the big string
    :param the_letter: a single character, look for
    :param the_replacement: a string, replace that character
    :return:
    """
    if not the_string:
        print('Empty string, returning')
        return ''
    if the_letter == the_string[0]:
        print(f'In {the_string} found {the_letter}, replacing with {the_replacement}')
        time.sleep(1)
        return the_replacement + string_replace(the_string[1:], the_letter, the_replacement)
    else:
        print(f'In {the_string} did not find {the_letter}')
        time.sleep(1)
        return the_string[0] + string_replace(the_string[1:], the_letter, the_replacement)


my_string, find_letter, replace = input(">> ").split()
print(string_replace(my_string, find_letter, replace))

"""
    python doesn't have a separate string and character type
    everything is just strings
"""