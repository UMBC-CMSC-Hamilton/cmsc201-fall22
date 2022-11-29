import random

"""
    Sorting a list

[2, 5, 3, 8, 4] -> [2, 3, 4, 5, 8]

bubble sort
insertion sort
merge sort
"""


def swap(a_list, i, j):
    temp = a_list[i]
    a_list[i] = a_list[j]
    a_list[j] = temp


def bubble_sort_simple(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list) - 1):  # prevents an index error
            if a_list[j] > a_list[j + 1]:
                swap(a_list, j, j + 1)
    
    return a_list


def bubble_sort_advanced(a_list):
    swapped = True
    i = 0
    while swapped:
        swapped = False
        for j in range(len(a_list) - 1):  # prevents an index error
            if a_list[j] > a_list[j + 1]:
                swap(a_list, j, j + 1)
                swapped = True
        print('On loop', i, ': ', a_list)
        i += 1
    
    return a_list


def insertion_sort(a_list):
    for cur in range(1, len(a_list)):
        pull_back = cur
        print(cur, a_list[cur], a_list)
        while pull_back > 0 and a_list[pull_back - 1] > a_list[pull_back]:
            swap(a_list, pull_back - 1, pull_back)
            pull_back -= 1
        print('On loop', cur, ': ', a_list)
    
    return a_list


def merge(first_list, second_list):
    """
        part of merge sort
    :param first_list:
    :param second_list:
    :return:
    """
    first_index = 0
    second_index = 0
    new_list = []
    while first_index < len(first_list) and second_index < len(second_list):
        if first_list[first_index] < second_list[second_index]:
            new_list.append(first_list[first_index])
            first_index += 1
        else:
            new_list.append(second_list[second_index])
            second_index += 1
    
    for i in range(first_index, len(first_list)):
        new_list.append(first_list[i])

    for j in range(second_index, len(second_list)):
        new_list.append(second_list[j])
    
    return new_list
    

def merge_sort(a_list):
    if len(a_list) < 2:
        return a_list
    print(a_list)
    half = len(a_list) // 2
    first_half = merge_sort(a_list[0: half])
    second_half = merge_sort(a_list[half:])
    return merge(first_half, second_half)


for i in range(1):
    my_list = [random.randint(0, 20) for _ in range(10)]
    print(my_list)
    my_list = merge_sort(my_list)
    print(my_list)
