a_dictionary = {'a': 1, 'b': 2, 'c': 3}

print(a_dictionary.get('d', -1))
# print(a_dictionary['d'])

print(a_dictionary.get('a', -1))

# not your answer
animals = {}
# good
'oxen' in animals and ('emu' in animals or 'ostrich' in animals)
# less good does not distribute, do not do this.
'oxen' in animals and ('emu' or 'ostrich' in animals)

grid = [[1, 2], [1, 'f']]

x_len = len(grid) // 2
y_len = len(grid[len(grid) // 2]) // 2
print(grid[x_len][y_len] in ['a', 'e', 'i', 'o', 'u'])
grid[x_len][y_len] == 'a' or grid[x_len][y_len] == 'e' or grid[x_len][y_len] == 'i' or grid[x_len][y_len] == 'o' or \
grid[x_len][y_len] == 'u'


"""
18)
my_list[x][y]

check that x is between 0 and len(my_list)
check that y is between 0 and len(my_list[x])<< inner list len not outer
"""

intro_string = 'Hello world I am a python programmer'
split_string = intro_string.split()
print(split_string)
print(split_string[2:6])
print('\n'.join(split_string[2:6]))

"""
11 ) add range(len(lines))
13) add colon
15) just switches not switches[row]
18) += instead of =
19) new_lines.append(new_line)
21) new_lines.append(lines[row])
"""

def read_the_text(my_string):
    split_string = my_string.split()
    word_counts = {}
    for word in split_string:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    max_word = split_string[0]
    for word in word_counts:
        if not max_word or word_counts[max_word] < word_counts[word]:
            max_word = word
            
    print(max_word)
    
    return word_counts


def equal_strings(a, b):
    if not a and not b:
        return True
    elif a[0] == b[0]:
        return equal_strings(a[1:], b[1:])
    else:
        return False


