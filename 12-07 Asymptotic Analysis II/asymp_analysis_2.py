"""
    Final exam 12/16 6:00 - 8:00 pm
        ITE 104
        
"""
"""
    Asymptotic Analysis
    
    How fast code runs based on the input size.
        n = input size (traditional)
        n = the size of a list, dict
            the size of a particular number, the number of digits
            sorting searching -> list size
            prime -> the number n
            
    Big-O
    
        f(n) is O(g(n)) when
            there are two constants C N_0 so that:
            
            f(n) <= C * g(n) whenever n >= N_0
            either f is in the same class of functions as g
                a constant times g bigger than f.
            
                f is in a smaller class of functions
                
            n is O(n^3)
                Why?
                    n < n^3? n get dominated by n^3
                    
                    lim{n to infinity} n/n^3 = lim 1/n^2 = 0
                    
            n^3 + 2n^2 + 1 is O(n^3)
            pick C = 6
            n^3 + 2n^2 + 1 <= 6n^3, N_0 = 1 something like that
            
    BogoSort - meme algorithm
        
        Consider all of the permutations of the list.
            one of them will be sorted because one permutation of
                anything will basically be sorted
        How many permutations are there for a list of size n?
            n!
        _ _ _ _ => 4 3 2 1 => multiplication principle => 24 = 4!
        
    Hierarchy of Functions:
        Constants O(1) < logs O(lg(n)) < linear O(n)
        < n lg(n) [Log-linear] < n^2 < n^3 < n^4 < n^5 < ...
        < 2^n < 3^n < 4^n < ... < n! < n^n < n^{2n^2}
"""

import time
import random
import itertools


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

def is_sorted(a_list):
    # O(n)
    for i in range(len(a_list) - 1):
        if a_list[i] > a_list[i + 1]:
            return False
    return True


def bogo_sort(a_list):
    # total time : O(n * n!)
    for perm in itertools.permutations(a_list):
        # n! times
        # print(perm)
        if is_sorted(perm): # O(n) function
            print('found it', perm)
            return perm

"""
    Final Exam, memorize this:
    Quadratic sorts:
    
    BubbleSort  - average and worst case O(n^2)
        best case O(n) = "rare case"
            if the list is sorted, very close to sorted
        swaps adjacent elements
    SelectionSort - always O(n^2)
        find min sort
    InsertionSort - average and worst case O(n^2)
        best case O(n)
        pull back sort
    
    Log-Linear sorts:
        MergeSort - Always O(n lg(n))
            Splits the list in half every time
                recombines them in sorted order
        QuickSort - On Average, best O(n lg(n))
            Worst case is O(n^2) - hugely worse than n lg(n)
                fixes (extra):
                    pick random pivot
                    pick median pivot in O(n) time.
            pick pivot, less list and greater list
            quick sort both lists
            concatenate
"""


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


def insertion_sort(a_list):
    for cur in range(1, len(a_list)):
        pull_back = cur
        while pull_back > 0 and a_list[pull_back - 1] > a_list[pull_back]:
            swap(a_list, pull_back - 1, pull_back)
            pull_back -= 1
    
    return a_list

def selection_sort(a_list):
    """
        All cases of selection sort are O(n^2)
        best case, worst case, average case, all cases
    """
    for i in range(len(a_list)):
        min_index = i
        for j in range(min_index + 1, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j
        swap(a_list, min_index, i)
    return a_list

"""
Log_linear sorts
"""


def quick_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    
    pivot = a_list[0]
    less_list = []
    greater_list = []
    for i in range(1, len(a_list)):
        if a_list[i] < pivot:
            less_list.append(a_list[i])
        else:
            greater_list.append(a_list[i])
    less_list = quick_sort(less_list)
    greater_list = quick_sort(greater_list)
    return less_list + [pivot] + greater_list

"""
    Quick Sort + Sorted list:
    
    [1, 2, 3, 4, 5, 6, 7, 8]
    [] + [1] + [2, 3, 4, 5, 6, 7, 8], pivot = 1
    [] + [2] + [3, 4, 5, 6, 7, 8], pivot = 2
    [] + [3] + [4, 5, 6, 7, 8], pivot = 3
    [] + [4] + [5, 6, 7, 8], pivot = 4
    [] + [5] + [6, 7, 8], pivot = 5
    [] + [6] + [7, 8], pivot = 6
    [] + [7] + [8], pivot = 7
"""


# new_list = [random.randint(0, 100) for _ in range(12)]
# bogo_sort(new_list)

size = int(input('>> size? >> '))
my_list = [random.randint(0, 1000) for _ in range(size)]
copy_list = list(my_list)
start_time = time.process_time()
"""
print('Starting insertion sort')
insertion_sort(my_list)
print('insertion sort took', time.process_time() - start_time)
"""

start_time = time.process_time()
print('Starting merge sort')
merge_sort(copy_list)
print('merge sort took', time.process_time() - start_time)

new_list = [random.randint(0, 100) for _ in range(11)]
start_time = time.process_time()
print('Starting bogo sort')
bogo_sort(new_list)
print('bogo sort took', time.process_time() - start_time)
