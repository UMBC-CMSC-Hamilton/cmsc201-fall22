import random
import time

"""
    Asymptotic Analysis - analyze algorithms from the perspective
        of how long they take (the number of steps)
        
        Input Size (n) want to ask how does the number of steps
            change as the input size "gets large"
            
    Mathematical Aspect -> Big O
    
    Computational Aspect -> Code/Alg -> function that gives us
        time complexity?
"""

"""
    Big-O
    
    What is big-O?
        It's a way to talk about a "class" of functions
        O(n^2)
        f(n) is [in] O(n^2) when there is some constant C > 0
            f(n) <= C * n^2
            
        5n^2 is O(n^2) "quadratic or less"
            5n^2 <= C n^2, you get to pick the constant
                I'm going to pick 17
        5n^2 <= 17 n^2
        3n^2 + 2n + 1 <= C n^2, pick 6 = C
        3n^2 + 2n + 1 <= 6 n^2
            1 <= 6(0)^2 = 0 (no actually)
            need to add "eventually"
            
        f(n) is O(g(n)) if there are constants C and N_0 so that
            f(n) <= C g(n) when n > N_0
        f(n) is "in the same class (or less) as" g(n)
            eventually

        Logs grow slower than lines
        lg(n) is O(n)
        lg(n) < (C = 1) n
            n > 0
        
        O(1) = constant time
            arithmetic, assignments, returns, if statements
            
        23 is O(1)
        23 <= C * 1, pick C = 25
            Any algorithm that doesn't depend on the input size
        
"""


def even_or_odd(n):
    """
        101010010111000111000110 <-- that zero means even
        100101011110000101111111 <-- the one means odd
        
        code or this algorithm is O(1), O(3)
    """
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'


def find_max(a_list):
    """
        n = len(a_list)
        O(n) algorithm = linear time
        
        steps(n) = 4 + 2n
        4 + 2n <= (C = 3)n
        4 <= 0 not true
        N_0 = 4
        4 + 2 * 4 <= 3 * 4 True
    """
    if not a_list:
        return 0
    
    current_max = a_list[0]
    for i in range(len(a_list)):
        if a_list[i] > current_max:
            current_max = a_list[i]
    
    return current_max

"""
the_list = [random.randint(0, 1000) for _ in range(100000000)]
print('list built...')
start_time_ns = time.process_time_ns()
start_time = time.process_time()
find_max(the_list)
print('That find max took', time.process_time_ns() - start_time_ns, 'nanoseconds')
print('That find max took', time.process_time() - start_time, 'seconds')
"""


def is_prime(n):
    """
        O(n)
    """
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def is_prime_opt(n):
    """
        O(sqrt(n))
        
    """
    for x in range(2, int(n ** (1/2)) + 1):
        if n % x == 0:
            return False
    return True

def prime_time():
    five_prime = 115733
    six_prime = 978233
    seven_prime = 8507689
    
    start_time_ns = time.process_time_ns()
    start_time = time.process_time()
    is_prime_opt(five_prime)
    print('That is_prime took', time.process_time_ns() - start_time_ns, 'nanoseconds')
    print('That is_prime took', time.process_time() - start_time, 'seconds')
    
    
    start_time_ns = time.process_time_ns()
    start_time = time.process_time()
    is_prime_opt(six_prime)
    print('That is_prime took', time.process_time_ns() - start_time_ns, 'nanoseconds')
    print('That is_prime took', time.process_time() - start_time, 'seconds')
    
    
    start_time_ns = time.process_time_ns()
    start_time = time.process_time()
    is_prime_opt(seven_prime)
    print('That is_prime took', time.process_time_ns() - start_time_ns, 'nanoseconds')
    print('That is_prime took', time.process_time() - start_time, 'seconds')
    
    fourteen_prime = 48375483959927
    
    start_time_ns = time.process_time_ns()
    start_time = time.process_time()
    is_prime_opt(fourteen_prime)
    print('That is_prime took', time.process_time_ns() - start_time_ns, 'nanoseconds')
    print('That is_prime took', time.process_time() - start_time, 'seconds')
    sixteen_digits = 6071537334198803
    # eighteen_digits = 368416879664541401
    # twenty_eight_prime = 5648019223058001721435769971
    twenty_one_prime = 597808931205647572699
    start_time_ns = time.process_time_ns()
    start_time = time.process_time()
    is_prime_opt(sixteen_digits)
    print('That is_prime took', time.process_time_ns() - start_time_ns, 'nanoseconds')
    print('That is_prime took', time.process_time() - start_time, 'seconds')


def linear_search(a_list, look_for):
    # O(n) algorithm.
    for x in a_list:
        if x == look_for:
            return True
    return False

"""
    Binary Search
    
        [1, 4, 7, 9, 13, 17, 23, 29, 31]
        [17, 23, 29, 31]
        [17, 23]
    if the list is sorted, check the middle element
"""

def binary_search_rec(a_list, search_for, start, end):
    if start >= end:
        return False

    middle_pos = (start + end)//2
    print(start, end, middle_pos, a_list[middle_pos])
    if a_list[middle_pos] == search_for:
        return True
    elif search_for < a_list[middle_pos]:
        return binary_search_rec(a_list, search_for, start, middle_pos - 1)
    else:
        return binary_search_rec(a_list, search_for, middle_pos + 1, end)
    
    
def binary_search(a_list, search_for):
    if not a_list:
        return False
    return binary_search_rec(a_list, search_for, 0, len(a_list))


rand_list = [random.randint(0, 100) for _ in range(128)]
rand_list.sort()
print(rand_list)
print(binary_search(rand_list, 25))

"""

"""