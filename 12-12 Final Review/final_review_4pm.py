"""
[6, 2, 10, 21, 31, 24, 17]

BubbleSort: - do I swap adjacents?
[2, 6, 10, 21, 24, 17, 31] - 1st iteration
[2, 6, 10, 21, 17, 24, 31] - 2nd iteration
[2, 6, 10, 17, 21, 24, 31] - 3rd iteration
[2, 6, 10, 17, 21, 24, 31] - 4th iteration, swapped = False

SelectionSort - find minimum sort
[4, 87, 24, 31, 5, 91, 13]
[4, 87, 24, 31, 5, 91, 13] - 1st iteration, min = 4, i = 0
[4, 5, 24, 31, 87, 91, 13] - 2nd iteration, min = 5, i = 1
[4, 5, 13, 31, 87, 91, 24] - 3rd iteration, min = 13, i = 2
[4, 5, 13, 24, 87, 91, 31] - 4th iteration, min = 24, i = 3
[4, 5, 13, 24, 31, 91, 87] - 5th iteration, min = 31, i = 4
[4, 5, 13, 24, 31, 87, 91] - 6th iteration, min = 87, i = 5

InsertionSort - pullback sort
[4, 87, 24, 31, 5, 91, 13] - same list (before sorting)
[4, 87, 24, 31, 5, 91, 13] - 1st iteration, i = 1
[4, 24, 87, 31, 5, 91, 13] - 2nd iteration, i = 2
[4, 24, 31, 87, 5, 91, 13] - 3rd iteration, i = 3
[4, 5, 24, 31, 87, 91, 13] - 4th iteration, i = 4
[4, 5, 24, 31, 87, 91, 13] - 5th iteration, i = 5 (same thing trying to pullback 91)
[4, 5, 13, 24, 31, 87, 91] - 6th iteration, i = 6
Sorted.
"""
dogs = []
cats = []
# this is your answer
'pupper' in dogs and 'minion' in cats

test_string = ''
# here is the answer
test_string.is_alpha() and \
(test_string == test_string.upper() or test_string == test_string.lower())

birds= []
password = 'password1'
# here's the answer
len(birds) == 0
not birds and (password == 'password1' or password == 'asdf1234')
not birds and password in ['password1', 'asdf1234']

"""
15, 241 into bin
15 -> 7 -> 3 -> 1
all odd
0000 1111

241 -> 120 -> 60 -> 30 -> 15 -> 7 -> 3 -> 1
1111 0001

0011 1101
dec = 3(16) + 13 = 1 + 4 + 8 + 16 + 32 = 61
hex = 3D, 0x3D, 0x3d whatever
    0x1234
    1234 dec

1010 1111
hex = AF
dec = 10(16) + 15 = 175
    also use the binary
    

Remember the table
0000 0  1000 8
0001 1  1001 9
0010 2  1010 10 A
0011 3  1011 11 B
0100 4  1100 12 C
0101 5  1101 13 D
0110 6  1110 14 E
0111 7  1111 15 F

0x40DE59FA
0100 0000 1101 1110 0101 1001 1111 1010

"""


"""
Asymptotic Analysis
    O = worst case
    Omega = best case
    
BubbleSort, InsertionSort
    best: Omega(n) (basically the same as O, except it's a lower bound)
    worst: O(n^2)
    
SelectionSort:
    best== worst == Omega(n^2) also O(n^2)
    
MergeSort:
    best == worst == O(n lg(n)), Omega(n lg(n))
    
QuickSort:
    best : Omega(n lg(n)) (average too)
    worst: O(n^2)
        put in a a sorted list
        
LinearSearch:
    Omega(1) - best case,find it as the first element (or close)
    O(n/2) == O(n) average/worst case

BinarySearch:
    Best Case Omega(1) - could get lucky
    Worst Case O(lg(n))
"""

"""
    Debugging
    
    Line 5: len
    line 6: range(len(my_list[i])) add the [i] part
    line 7: the_element = my_grid[i][j]
    line 8: missing :
    line 9: the_element += 1 to elements[the_element] += 1
    line 10: else rather than elif
    line 13: elements[elem] access the value not the key
    line 14: print elem, 'has matches'
                print(elem, 'has matches')
    line 17: missing outer []
"""

def a_distance(message):
    a_start = -1
    min_a_dist = len(message) + 1
    
    for i in range(len(message)):
        if a_start == -1 and message[i] == 'a':
            a_start = i
        elif message[i] == 'a':
            if i - a_start < min_a_dist:
                min_a_dist = i - a_start
            a_start = i

    return min_a_dist


def alt_a_distance(message):
    split_on_as = message.split('a')
    min_a_dist = len(message) + 1
    for substr in split_on_as:
        if len(substr) < min_a_dist:
            min_a_dist = len(substr) + 1
    
    return min_a_dist


"""
    [1, 2, 5, 3, 9, 7]
    [1] + fs[2, 5, 3, 9, 7]
    fs[2, 5, 3, 9, 7]
    [2] + fs[5, 3, 9, 7]
    fs[5, 3, 9, 7] = [5] + fs[3, 9, 7]
    fs[3, 9, 7] prev = 5
    fs[9, 7] = [9] + fs[7]
    fs[7] prev = 9, drop []
"""


def force_sort_rec(a_list, prev_element=None):
    if not a_list:
        return []
    if prev_element == None:
        return force_sort_rec(a_list, a_list[0] - 1)
    elif prev_element <= a_list[0]:
        return [a_list[0]] + force_sort_rec(a_list[1:], a_list[0])
    else:
        return force_sort_rec(a_list[1:], prev_element)
    
def force_sort(a_list):
    if not a_list:
        return []
    
    prev_element = a_list[0]
    new_list = [prev_element]
    
    for i in range(1, len(a_list)):
        if a_list[i] >= prev_element:
            new_list.append(a_list[i])
            prev_element = a_list[i]

    return new_list

"""
    
    Final Friday Dec 16
        6:00 - 8:00 pm in ITE 104

"""