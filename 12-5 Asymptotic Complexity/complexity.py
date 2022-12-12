"""
    Asymptotic Complexity
        Programming side Code -> Time
            How fast does the code run as we change the input size?
                Sorting
                    list of size n up to a list of size 10n
                BubbleSort
                SelectionSort
                InsertionSort
                    T(n) = t_0 -> T(10n) = 100 t_0
        Mathematical Side of Asymptotic Complexity
            Big-O -> way to describe "classes" of functions
                A group of functions that all share some kind
                    of property.

    Q: Will I live to see the end of this algorithm?
        Some algorithms are so slow that you dont want to run them
            Make a better algorithm
            Just don't do it.
            Approximate it.
"""

"""
    Let's talk Big-O (Mathematical Side)
    
    f(n) is O(g(n))
    f(n) is in the class of g(n) in terms of O
    
    f(n) <= Cg(n), C is something that we can make up
    
    5n^2 <= C n^2 (problem,without the constant, 5n^2)
        C = 5 or 6 or 7...
    (1/2) n^2 <= n^2
    5n^2 is O(n^2)
    Do mean: we can pick 7 and it works.
    Don't mean: can pick anything.C = 3
        5n^2 <= 3n^2 (what does this mean? nothing, picked a bad C)
    
    O(1) = constant time
        the time of the algorithm doesn't have to do with the input size
        parity checking - checking if a number is even or odd
            input size = the size of the number
            modding a number by 2 doesn't really depend on the
                size of the number, just depends on the last bit
                01010001000100110001 <- 1 at the end, odd
                00100111101101001110 <- 0 at the end, even
        if statements, assignments = constant time
        for loops, while loops - probably not constant
        functions - depends on what is in it.
    
    Linear time O(n)
        min or max = linear time
        2 + 2n <= 3n, eventually
        n = 0, 2 <= 0 false?
        n = 1, 4 <= 2 false again?
        n = 2, 6 <= 6 true, but was it a fluke?
        n = 3, 8 <= 9, maybe not a fluke
        n = 4, 10 <= 12, looks like we're winning here
        start at n = 3 [3, \infty)
    
"""


def find_max(a_list):
    if not a_list:
        return 0
    
    # steps = 2 + 2n
    the_max = a_list[0]
    # O(n) or linear time
    for x in a_list:
        # constant time
        if x > the_max:
            the_max = x
    return


"""
    Also a linear time algorithm
"""


def is_prime(n):
    # n - 2 steps
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


"""
    O(sqrt(n)) = O(n ** (1/2))
"""


def is_prime_improved(n):
    # n = x * y , either n is a perfect square n = x^2
    # 27 = 3 * 9
    for i in range(2, int(n ** (1 / 2))):
        if n % i == 0:
            return False
    
    return True


"""
    linear search: look through a list for an element
        this is linear time, not just because i call it linear
            search.
        Generally you have to look through "at least half of the list"
        n/2 searches on average
        O(n/2) = O(n)
        
"""


def linear_search(a_list, x):
    for y in a_list:
        if y == x:
            return True
    return False


# 3 in a_list

"""
    binary search
        what if we have a sorted list?
        
"""

"""
    n = 2^k
    lg(n) = k
    running time is not O(n) actually O(k)
    n --> running time is O(lg(n))
    lg(n) = log_2(n)
"""
def binary_search(a_list, search_for, start, end):
    if not a_list:
        return False
    if start >= end:
        return False
    
    middle_pos = (start + end) // 2
    print(middle_pos, a_list[middle_pos])
    if search_for == a_list[middle_pos]:
        return True
    elif search_for > a_list[middle_pos]:
        return binary_search(a_list, search_for, middle_pos + 1, end)
    else:  # search_for < a_list[middle_pos]
        return binary_search(a_list, search_for, start, middle_pos)

import random
import time
print(binary_search([1, 2, 3, 4, 5], 2, 0, 5))
print(binary_search([1, 2, 3, 4, 5], 7, 0, 5))

# just setup
my_list = [random.randint(0, 100) for _ in range(2048)]
my_list.sort()
# now we'll run binary search
print(my_list)
print(binary_search(my_list, 201, 0, len(my_list)))

"""
    Merge Sort, Quick Sort (most of the time)
    O(n lg(n))
    Bubble Sort, Selection Sort, Insertion Sort O(n^2)
"""


def put_together(a_list, b_list):
    """
        also referred to as merge
        a_list and b_list are both sorted lists
    :return: a sorted combination of the two lists
    """
    new_list = []
    a_index = 0
    b_index = 0
    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] < b_list[b_index]:
            new_list.append(a_list[a_index])
            a_index += 1
        else:
            new_list.append(b_list[b_index])
            b_index += 1
    
    for i in range(a_index, len(a_list)):
        new_list.append(a_list[i])
    for j in range(b_index, len(b_list)):
        new_list.append(b_list[j])
    
    return new_list


def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    
    half = len(a_list) // 2
    first_half = a_list[0: half]
    second_half = a_list[half: len(a_list)]
    return put_together(merge_sort(first_half), merge_sort(second_half))

def swap(a_list, i, j):
    temp = a_list[i]
    # what this will do is swap the elements at position i andj
    a_list[i] = a_list[j]
    a_list[j] = temp


def selection_sort(a_list):
    """
        find minimum and then swap sort
    """
    for i in range(len(a_list)):
        min_index = i
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j
        if min_index != i:
            swap(a_list, i, min_index)
    return a_list

my_new_list = [random.randint(0, 1000) for _ in range(10000)]
my_copy = list(my_new_list)

start_time = time.process_time()
print("merge sort first")
merge_sort(my_new_list)
print(f"that took {time.process_time() - start_time}")


print("selection sort next")
selection_sort(my_copy)
print(f"that took {time.process_time() - start_time}")
