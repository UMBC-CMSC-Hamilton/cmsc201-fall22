"""
    File IO - Input/Output
        It's very slightly different from print/input
"""

the_file = open('sample.txt')
# opens the file sets the cursor at the front of the file and waits
print(the_file.read())
"""
    .read() = reads everything, returns a string
        input = never get endlines
        .read() = possibly get endlines
        .readline() = one string at a time
        .readlines() = list[strings]
        for loop method (secretly calling readline())
"""
the_file.close()

for_example_file = open('../for_examples.py')
# pretending that the file is a list
for line in for_example_file:
    print(line.strip('\n'))
    # remember that reading from a file DOES NOT strip off \n
    # at the end of every line

# why might you want to close a file?
for_example_file.close()

# if you add a second parameter (default parameter)
# defaults to 'r'
the_file_again = open('sample.txt', 'r')
print(the_file_again.readlines())
#  read lines will give us a list of the lines
# notice that since they're strings, we can see the \n
the_file_again.close()

# last method = .readline()

the_file_yet_again = open('sample.txt', 'r')
the_line = the_file_yet_again.readline()
# if the_line is an EMPTY STRING,not just '\n' truly empty
# that means we're done
while the_line:
    print(the_line, end='')
    the_line = the_file_yet_again.readline()
the_file_yet_again.close()


def count_lines(a_file_name):
    with open(a_file_name, 'r') as read_file:
        # read_file = open(a_file_name, 'r')
        # prevents you from forgetting
        count = 0
        for line in read_file:
            count += 1
    # does the file close for you
    
    return count

"""
    Let's talk about writing to files.
    How do we open a file in write mode?
"""

my_write_file = open('second_sample.txt', 'w')
# write opens the file, blanks/deletes whatever you call that
# sets the cursor to the front
in_string = input('Tell me a word: ')
while in_string != 'quit':
    my_write_file.write(in_string + '\n')
    in_string = input('Tell me a word: ')

my_write_file.close()

# a bunch of code
# a mode is APPEND mode, opens the file with write permissions
# DOESNT zero out the file
# gives you the ability to add from the end of the file
#   sets the file pointer/cursor to the end of the file
with open('second_sample.txt', 'a') as second_sample:
    in_string = input('Tell me a word: ')
    while in_string != 'quit':
        second_sample.write(in_string + '\n')
        in_string = input('Tell me a word: ')

# secret operating system buffers
# print things => stdout buffer

"""
    if you ever see them:
    r+ w+ a+ = r+ read mode with write access
    rb wb ab = read/write/append (byte mode)
"""

"""
    a_file.writelines(a_list_of_strings)
    
    for x in a_list_of_strings:
        a_file.write(x)
"""

color_list = ['red','cyan', 'magenta', 'green', 'blue', 'yellow', 'gray', 'purple', 'black', 'white']
for i in range(len(color_list)):
    color_list[i] += '\n'
    
with open('color_file.txt', 'w')as color_file:
    color_file.writelines(color_list)


