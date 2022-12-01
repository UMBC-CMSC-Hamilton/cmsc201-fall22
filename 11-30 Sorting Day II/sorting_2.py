"""
    BubbleSort - n^2/2 steps
    InsertionSort - n^2/2 steps
    
    SelectionSort - n^2/2 steps
    MergeSort
    QuickSort
"""

import random


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
        print(a_list)
    return a_list


def test_sorting_function(the_sort, n):
    the_list = [random.randint(0, 99) for _ in range(n)]
    print(the_list)
    copy_of_list = list(the_list)
    the_list = the_sort(the_list)
    copy_of_list.sort()
    if the_list == copy_of_list:
        print(the_list, 'is sorted')


"""

17 5 8 21 39 2 7 6
17 5 8 21 || 39 2 7 6
17 5 || 8 21 || 39 2 || 7 6
17 || 5 || 8 || 21 || 39 || 2 || 7 || 6

Recombine the lists back together
17 || 5 = [5, 17]

[5, 17] || [8, 21] || [2, 39] || [6, 7]
[5, 8, 17, 21] || [2, 6, 7, 39]
[2, 5, 6, 7, 8, 17, 21, 39]
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
    print('splitting', first_half, second_half)
    pt = put_together(merge_sort(first_half), merge_sort(second_half))
    print('put together', pt)
    return pt


"""
    QuickSort
        = faster than mergesort most of the time
            the worst case is actually quadratic O(n^2)
                just like selection, bubble, insertion

        pivot = the_list[0]
        make a less_list, greater_list
            shove equal elements into the greater list
            quick_sort(less_list)
            quick_sort(greater_list)
        
    [4, 3, 9, 1, 2, 8, 7, 5, 4]
    pivot = 4
    [3, 1, 2] + 4 + [9, 8, 7, 5, 4]
    [3, 1, 2]
    pivot = 3
    [1, 2] + 3 + [] = [1, 2, 3]
    pivot = 1
    [] + 1 + [2] = [1, 2]
    
    [9, 8, 7, 5, 4]
    pivot = 9
    [8, 7, 5, 4] + 9 + [] = [4,5, 7, 8, 9]
    pivot = 8
    [7, 5, 4] + 8 + [] = [4, 5, 7, 8]
    pivot = 7
    [5, 4] + 7 + [] = [4, 5, 7]
    pivot = 5
    [4] + 5 + [] = [4, 5]
    
    [1, 2, 3, 4, 5, 7, 8, 9]
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



for _ in range(20):
    test_sorting_function(quick_sort, 10)


"""
python .sort() uses "timsort" -> name of the guy who wrote it

    TimSort = MergeSort + InsertionSort
"""