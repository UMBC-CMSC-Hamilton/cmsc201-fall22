"""
    Remember Final:
        12/16 at 6:00 to 8:00 pm
        ITE 104 for Eric's Sections.
        
    Definition of Big-O
    
        f(n) is O(g(n)) when there are two constants C, N_0
            so that:
        
        f(n) <= C g(n) when n > N_0
        f and g are in the same "class of function"
            N_0 allows "eventually"
            
    Asymptotic Analysis cares about how algorithms run time changes
        as the input size grows.
        
        Input size (n) = size of a list, size of a dictionary
            size of a number / number of digits in a number
"""

"""
    Bubble Sort
    Merge Sort
    
    BogoSort
"""

"""
    BogoSort - jumble the data, check if it's sorted, if not, repeat
    
        1) pick a specific permutation of the data (scan through all permutations)
        2) completely randomly pick a new ordering
        
        What is a permutation?
            1 2 3 4     2 1 3 4     3 1 2 4     4 1 2 3
            1 2 4 3     2 1 4 3     3 1 4 2     4 1 3 2
            1 3 2 4     2 3 1 4     3 2 1 4     4 2 1 3
            1 3 4 2     2 3 4 1     3 2 4 1     4 2 3 1
            1 4 2 3     2 4 1 3     3 4 1 2     4 3 1 2
            1 4 3 2     2 4 3 1     3 4 2 1     4 3 2 1
    
        _ _ _ _ => 4 * 3 * 2 * 1 = 24 = 4!
        A permutation is a reordering of a set/list
        How many permutations are there of n things?
            n!
            
            To check if a list is sorted O(n)
            n! * O(n) = O(n * n!) = Runtime of bogosort
    
    Hierarchy of functions: < means (as you go to infinity,
        the bigger function will win)
    Constants < logs < linear < n lg(n) < n^2 < n^3 < n^4 ...
    < 2^n < 3^n < 4^n < ... < n! < n^n < n^{n^2}
    
"""

import itertools
import random
import time

def is_sorted(the_list):
    for i in range(len(the_list) - 1):
        if the_list[i] > the_list[i + 1]:
            return False
    return True


def bogo_sort(the_list):
    for perm in itertools.permutations(the_list):
        print(perm)
        if is_sorted(perm):
            print(perm, 'found it')
            return perm



"""
    Merge Sort always O(n lg(n))
    Quick Sort usually O(n lg(n))
        but can be as bad as O(n^2)
        
        n lg(n) way way way better than n^2
"""


def quick_sort(a_list, level=0):
    if len(a_list) <= 1:
        return a_list
    less_list = []
    greater_list = []
    pivot = a_list[0]
    # excluding the pivot element
    for i in range(1, len(a_list)):  # partition
        if a_list[i] < pivot:
            less_list.append(a_list[i])
        else:
            greater_list.append(a_list[i])
    
    less_list = quick_sort(less_list, level + 1)
    greater_list = quick_sort(greater_list, level + 1)
    result = less_list + [pivot] + greater_list
    return result


"""
sorted or reverse sorted, this is actually its worse case

[8 7 6 5 4 3 2 1]
pivot = 8
[7, 6, 5, 4, 3, 2 , 1] + [8] + [empty greater]
pivot = 7
[6, 5, 4, 3, 2 , 1] + [7] + [empty greater]
pivot = 6
[5, 4, 3, 2 , 1] + [6] + [empty greater]
pivot = 5
[4, 3, 2 , 1] + [5] + [empty greater]
pivot = 4
[3, 2 , 1] + [4] + [empty greater]
pivot = 3
[2 , 1] + [3] + [empty greater]
pivot = 2
[1] + [2] + [empty greater]
list is size 1, the end.

n - 1 steps to get down to the size of 1

"""


def put_together(a_list, b_list):
    """
        two sorted lists.
        :return: bigger sorted list
    """
    a_index = 0
    b_index = 0
    new_list = []
    
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
    # print('Splitting', first_half, second_half)
    pt = put_together(merge_sort(first_half), merge_sort(second_half))
    # print('Put Together: ', pt)
    return pt


def swap(a_list, i, j):
    temp = a_list[i]
    # what this will do is swap the elements at position i andj
    a_list[i] = a_list[j]
    a_list[j] = temp


def bubble_sort_simple(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list) - 1):
            if a_list[j] > a_list[j + 1]:
                swap(a_list, j, j + 1)
        print(f'{i}th time: ', a_list)
    
    return a_list


def bubble_sort_adv(a_list):
    # exchange the outer loop for a while loop
    i = 0
    swapped = True
    while swapped and i < len(a_list):
        swapped = False
        for j in range(len(a_list) - 1 - i):
            if a_list[j] > a_list[j + 1]:
                swap(a_list, j, j + 1)
                swapped = True
        i += 1
    
    return a_list


# a_list = [random.randint(0, 10) for _ in range(10)]
# bogo_sort(a_list)

size = int(input(" size: "))
new_list = [random.randint(0, 1000) for _ in range(size)]
copy_list = list(new_list)
"""
start_time = time.process_time()
bubble_sort_adv(new_list)
print('Bubble sort took', time.process_time() - start_time)

start_time = time.process_time()
merge_sort(copy_list)
print('Merge sort took', time.process_time() - start_time)
"""
"""
    100,000 * log(100,000)
    ----------------------
    10,000 * log(10,000)
    = (5/4) * 10 = 12.5
    0.03125 * 12.5 ~= .4 sec

    1,000,000 * log(1,000,000)
    ----------------------
    100,000 * log(100,000)
    = (6/5) * 10 = 12.0
    ~ 6 seconds?
"""

def a_and_b(n, current):
    if n == 0:
        # print(current)
        pass
    else:
        a_and_b(n - 1, current + 'a')
        a_and_b(n - 1, current + 'b')
        
"""
    a_and_b(n) = 2 * a_and_b(n - 1)
    a_and_b(n - 1) = 2 * a_and_b(n - 2)
    ...
    a_and_b(0) = 1
    
    time that it takes is going to be O(2^n)


for i in range(10, 30):
    start_time = time.process_time()
    a_and_b(i, '')
    print(f'on size {i} it took: ', time.process_time() - start_time)
"""
"""
    BubbleSort average and worst O(n^2) time
        O(n) - best case
    InsertionSort average and worst O(n^2) time
        O(n) - best case
    SelectionSort O(n^2) all time
    
    QuickSort - worst case here is O(n^2), average is O(n lg(n))
        [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        neither sorted nor reverse sorted but still worse case
    MergeSort - all the time
        O(nlg(n))
        
    When you increase the size of a list by a factor of 10:
        n^2 sorts / quadratic sorts will take
        (n_new / n_old)^2 * original time
        
        n_new * lg(n_new) / n_old * lg(n_old)
            going to eventually just look like n_new/n_old as
            n-> infinity
"""


def insertion_sort(a_list):
    for cur in range(1, len(a_list)):
        pull_back = cur
        while pull_back > 0 and a_list[pull_back - 1] > a_list[pull_back]:
            swap(a_list, pull_back - 1, pull_back)
            pull_back -= 1
    
    return a_list


def tim_sort(a_list):
    if len(a_list) <= 50:
        return insertion_sort(a_list)
    
    half = len(a_list) // 2
    first_half = a_list[0: half]
    second_half = a_list[half: len(a_list)]
    pt = put_together(tim_sort(first_half),
                      tim_sort(second_half))
    return pt


start_time = time.process_time()
merge_sort(new_list)
print('Merge sort took', time.process_time() - start_time)

start_time = time.process_time()
tim_sort(copy_list)
print('Tim sort took', time.process_time() - start_time)
