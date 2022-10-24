"""
    Slices - slices are a way to get a substring or a sublist
        syntax: list[start: end]
"""
my_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_list[3:6])
print(my_list[0:5])
# oddity - instead of IndexError it just scans to the end of the list
print(my_list[5:1000])

my_string = 'hellothere'
print(my_string[2:7])
# [start:], end is going to default to the end of the string or list
print(my_string[5:len(my_string)], my_string[5:])

date_string = '03 / 12 / 2022'
# MM/DD/YYYY
print(date_string.split('/'))
month = date_string[0:2]
day = date_string[3:5]
year = date_string[6:11]
print(month, day, year)

time_string = '05:32:47'
print(time_string.split(':'))

"""
    You can use a slice to make a copy of a list
    python gimmick
"""
a_list = ['a', 'b', 't', 'd', 'r', 'e']
# keep slices in mind
b_list = a_list[0:len(a_list)]  # equivalently [:]
# a_list[:] start = 0 end = len(a_list)
b_list[3] = 'z'
print(a_list, b_list)

my_slice = a_list[3:6]
print(my_slice)
my_slice[0] = 'q'
print(my_slice)
print(a_list)
"""
for x in a_list[2:5]:
    print(x)
   
    Negative steps, negative slices
    
    python allows negative indices
"""

for i in range(-1, -1 * len(a_list) - 1, -1):
    print(i, a_list[i])


print(a_list[-3])
# last element in your list
print(a_list[-1], a_list[len(a_list) - 1])
"""
Rule for indices:
    -len(list) <= index < len(list)
    
    otherwise you get an index error
"""

# Will result in IndexError
# print(a_list[-100])

"""
    slices work like the range object
    start, stop, step
"""
import string
alphabet = (string.ascii_lowercase)
print(alphabet[0: len(alphabet): 2])
print(alphabet[5: 22: 3])

# any invalid slice will just be empty
print(alphabet[17: 5], end='the end')
print(alphabet[22:3:5])
print(alphabet[777:3:5])

# normally you get index errors, but with slices, the philosophy is
# no errors at all
print(alphabet[::-1])
print(alphabet[17:2:-1])
"""
    if the step size is negative
    [end = len(alphabet): start = -1: step =negative]
"""

print(alphabet[20::-5])
"""
    slices with step = 1 (nothing in the step argument)
    slice[start: stop]
"""
