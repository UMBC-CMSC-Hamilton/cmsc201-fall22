import random

"""
    Sorting a list

        bubble sort
        (selection sort)
        insertion sort
        merge sort
        
    take an unsorted list and make it into a sorted list somehow
    
    1st idea is swap
"""

def swap(a_list, i, j):
    temp = a_list[i]
    # what this will do is swap the elements at position i andj
    a_list[i] = a_list[j]
    a_list[j] = temp
    
    
my_list = [3, 5, 6, 1, 2]
swap(my_list, 1, 2)
print(my_list)
"""
    bubble sort
"""

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
        # n - 1 - i <-- because you don't need to check the last i after i iterations
        # they are already sorted
        for j in range(len(a_list) - 1 - i):
            if a_list[j] > a_list[j + 1]:
                swap(a_list, j, j + 1)
                swapped = True
        # print(f'{i}th time: ', a_list)
        i += 1
    
    return a_list


def insertion_sort(a_list):
    # why don't we include 0? because it can't be pulled back
    for cur in range(1, len(a_list)):
        swap_back_pos = cur
        while swap_back_pos > 0 and a_list[swap_back_pos - 1] > a_list[swap_back_pos]:
            swap(a_list, swap_back_pos - 1, swap_back_pos)
            swap_back_pos -= 1
    return a_list
    
    
def insertion_sort_with_break(a_list):
    # why don't we include 0? because it can't be pulled back
    for cur in range(1, len(a_list)):
        for swap_back_pos in range(cur, 0, -1):
            if a_list[swap_back_pos - 1] > a_list[swap_back_pos]:
                swap(a_list, swap_back_pos - 1, swap_back_pos)
            else:
                break
    return a_list


new_rand_list = [random.randint(0, 20) for _ in range(10)]
print(new_rand_list)
insertion_sort_with_break(new_rand_list)
print(new_rand_list)

"""
rand_list = [random.randint(0, 100) for _ in range(1000)]
print(rand_list)
rand_list.sort()
print(rand_list)
"""
i = 2
while i > 0:
    x = int(input('tell me a positive'))
    if x > 0:
        break
    i += 1
    
