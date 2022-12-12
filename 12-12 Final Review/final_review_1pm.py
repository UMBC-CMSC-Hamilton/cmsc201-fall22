dogs = []
cats = []
# on exam
'pupper' in dogs and 'minion' in cats

# not on exam
test_string = ''
# on exam
test_string == test_string.upper() or test_string == test_string.lower()

"""
241 -> 120 -> 60 -> 30 -> 15
       1111 0001
        F1
       
0011 1101
32 + 16 + 8 + 4 + 1 = 61 (dec)
3D in hex

40DE59FA
0100 0000 1101 1110 0101 1001 1111 1010
Must pad into 4s

"""

def a_distance(the_string):
    a_start = -1
    min_dist = len(the_string) + 1
    for i in range(len(the_string)):
        if the_string[i] == 'a' and a_start == -1:
            a_start = i
        elif the_string[i] == 'a' and a_start >= 0:
            distance = i - a_start
            if distance < min_dist:
                min_dist = distance
            a_start = i
    
    return min_dist


def a_distance_simpler(the_string):
    split_stuff = the_string.split('a')
    min_len = len(the_string)
    for i in range(len(split_stuff)):
        if len(split_stuff[i]) < min_len:
            min_len = len(split_stuff[i]) + 1  # maybe 1
    return min_len


def force_sort(a_list, previous=None):
    if not a_list:
        return []
    
    if previous == None:
        return force_sort(a_list[1:], a_list[0])
    elif a_list[0] >= previous:
        return [a_list[0]] + force_sort(a_list[1:], a_list[0])
    else:
        return force_sort(a_list[1:], a_list[0])


def force_sort_nonrec(a_list):
    if not a_list:
        return []
    new_list = [a_list[0]]
    previous = a_list[0]
    for i in range(1, len(a_list)):
        if a_list[i] >= previous:
            new_list.append(a_list[i])
            previous = a_list[i]
    
    return new_list


"""
    open(filename = string, modes)
    modes = 'r' read = just reads the file
            'w' write = blanks the entire file, starts at 0
            'a' append= open the file put the cursor at the end
    close() - close files.
    
    with open('my_file.txt') as f:
        stuff
    # don't need to close because with does it automatically
"""

"""

[21, 17, 9, 5, 2, 41, 77]

Bubble Sort:
[17, 9, 5, 2, 21, 41, 77] - 1st iteration
[9, 5, 2, 17, 21, 41, 77] - 2nd iteration
[5, 2, 9, 17, 21, 41, 77] - 3rd iteration
[2, 5, 9, 17, 21, 41, 77] - 4th iteration
[2, 5, 9, 17, 21, 41, 77] - 5th iteration - stop because no swaps

Selection Sort - find min sort

[21, 17, 9, 5, 2, 41, 77] min = 2, swap 2, 21
[2, 17, 9, 5, 21, 41, 77] min = 5, swap 17, 5
[2, 5, 9, 17, 21, 41, 77] min = 9 no swap
[2, 5, 9, 17, 21, 41, 77] min = 17 no swap
[2, 5, 9, 17, 21, 41, 77] min = 21 no swap
[2, 5, 9, 17, 21, 41, 77] min = 41 no swap
[2, 5, 9, 17, 21, 41, 77] min = 77 no swap

Insertion Sort - pull back sort

[21, 17, 9, 5, 2, 41, 77]
[17, 21, 9, 5, 2, 41, 77] i = 1
[9, 17, 21, 5, 2, 41, 77] i = 2
[5, 9, 17, 21, 2, 41, 77] i = 3
[2, 5, 9, 17, 21, 41, 77] i = 4


another list:
[4, 19, 5, 26, 14]
[4, 19, 5, 26, 14] i = 1 nothing happens
[4, 5, 19, 26, 14] i = 2
[4, 5, 19, 26, 14] i = 3 nothing happens again
[4, 5, 14, 19, 26] i = 4 14 gets pulled back

Asymptotic Analysis:

Remember (sorts):

	BubbleSort
	SelectionSort
	InsertionSort O(n^2) - worst case is n^2
	
	Omega = best case
	BubbleSort, InsertionSort Omega(n)
	
	MergeSort
		Always O and Omega(n lg(n))
	QuickSort
		Omega(n lg(n)) O(n^2)
		
	Linear Search
		Best case is Omega(1)
		Worst case is O(n)
	Binary Search
		O and Omega (lg(n))

"""