"""
    BubbleSort = looks at adjacent elements and swaps
    InsertionSort = pull back sort
    
    MergeSort

"""

"""
    Merge Sort
    
    [8, 3, 5, 17, 22, 4, 6, 12]
    [8, 3, 5, 17] [22, 4, 6, 12]
    [8, 3] [5, 17] [22, 4] [6, 12]
    [8][3] [5][17] [22][4] [6][12]
    [3, 8] [5, 17] [4, 22] [6, 12]
    [3, 5, 8, 17]  [4, 6, 12, 22]
    [3, 4, 5, 6, 8, 12, 17, 22]
    
    [1, 12, 14, 20] [2, 3, 4, 50]
    [1, 2, 3, 4, 12, 14, 20, 50]
"""
import random


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


def test_sort(the_sort, n_size):
    my_list = [random.randint(0, 99) for _ in range(n_size)]
    print(my_list)
    copy_list = list(my_list)
    sorted_list = the_sort(my_list)
    copy_list.sort()
    print(sorted_list)
    if copy_list == sorted_list:
        print('The sort worked.')
    else:
        print('The sort failed.')


"""
Idea of QuickSort:
    pivot = a_list[0]
    Idea!
        I'm going to split the list into things that are
            less than the pivot, and things that are greater.
            
            Then we quicksort the less list and the greater list
            
        Then we recombine less_list + [pivot] + greater_list
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
    
    # print('\t' * level, pivot, less_list, greater_list)
    
    less_list = quick_sort(less_list, level + 1)
    greater_list = quick_sort(greater_list, level + 1)
    # what comes out are two sorted lists
    result = less_list + [pivot] + greater_list
    # print('\t' * level, result)
    return result


def swap(a_list, i, j):
    temp = a_list[i]
    a_list[i] = a_list[j]
    a_list[j] = temp


def selection_sort(a_list):
    """
        findmin sort
    """
    for i in range(len(a_list)):
        min_index = i
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j
        if min_index != i:
            swap(a_list, i, min_index)
    return a_list

import time


print('First merge:')
my_list = [random.randint(0, 999) for _ in range(100000)]
copy_list = list(my_list)
start_time = time.process_time()
print(merge_sort(my_list))
print('That took', time.process_time() - start_time)

print('Now selection:')
start_time = time.process_time()
print(selection_sort(my_list))
print('That took', time.process_time() - start_time)