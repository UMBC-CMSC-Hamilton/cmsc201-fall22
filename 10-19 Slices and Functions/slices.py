"""
    Slices - python specific way to get a sublist from a list
            substring out of a string
"""

first_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(first_list[2: 5])
print(first_list[2: 8])
print(first_list[5: 100])  # this is allowed but confusing

print(first_list[4:], first_list[4:len(first_list)]) # defaults to the end of the list
print(first_list[:5], first_list[0:5])

a_list = [3, 4, 8, 9]
copy_list = a_list
copy_list[2] = 100
print(a_list)


a_list = [3, 4, 8, 9]
copy_list = list(a_list)  # actual copy not a reference
copy_list[2] = 100
print(a_list, copy_list)

new_slice = a_list[1:3]
new_slice[0] = 55
print(new_slice, a_list)
"""
    What did i learn?  Slices are actually copies.
"""

# actually just making a copy
# confused me once, so i remember it.
some_list = a_list[:]
# same as some_list = list(a_list)
"""
Slices have a third parameter
"""

new_list = ['a', 'c', 'g', 'r', 't', 'l', 'q']
print(new_list)
reversed_list = new_list[:: -1]  # reverses the list
print(reversed_list)

"""
    Invalid slicing
        if you slice from 5 to 2
        for i in range(5, 2)
    
    If you enter any invalid slice it gives the empty list or
        empty string
"""
print(new_list[5:2])

a_string = 'hellothere'
print(a_string[3:7], a_string[9: 3: -1])

my_string = 'a longer string is like this, it has many characters'
print(len(my_string))
print(my_string[44:5:-3])
print(my_string[:5:-3])
"""

    slice[start:end:step]
    start = 0 if left unwritten step > 0
        start = len(list, string) if step < 0
    end = len(string, list) if step > 0
        end = -1 if step < 0
"""
time_code = "3:59:59"
print(time_code.split(":"))
"""
    01234567
    05:42:29
"""
# very very sensitive to user input
print(time_code[0:2], time_code[3:5], time_code[6:])

"""
    slices do actually make copies
        be careful with memory usage

dont do this:
big_string = 'a' * 1000000
list_of_slices = []
for i in range(len(big_string)):
    print(i)
    list_of_slices.append(big_string[0:i])
"""

# 'th' 'sh' 'ae'

in_string = input('Tell me a string: ')

for i in range(len(in_string)):
    if in_string[i: i + 2] in ['th', 'sh', 'ae']:
        print(f'found at position {i}')
        
