"""
    Announcements:
    Format of the exam:
        mixed paper - laptop exam
    
    Possibly - hopefully - definitely today we will release the
        practice exam
    Talk about it monday, i'll go over answers/reasoning etc
    
    No discussions the week of an exam, no discussion next week
        no homework.

"""

"""
Let's talk about strings:
    using strings as arrays/list
    
    strip
        split
        join
        
    ASCII - UNICODE
"""
def never_run():
    a_string = 'I am a great string, I have many characters'
    for i in range(len(a_string)):
        print(a_string[i], end=' ')
        # this is not possible because strings are immutable
        # a_string[i] = 'a'
    
    # new line for no reason
    print()
    
    # for each loop:
    for letter in a_string:
        print(letter, end=' ')
        
    # the difference in general is that if you need the index, use the for-i loop
    # if you don't, you can use the for each loop.
    
    print()
    
    my_list = [2, 4, 5, 6, 8, 9, 10, 12, 14, 16]
    increasing = True
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            increasing = False
            
    if increasing:
        print('The list was in increasing order')
    else:
        print('The list is not increasing')
    
    my_increasing_string = 'hplatzeqry'
    increasing = True
    for i in range(len(my_increasing_string) - 1):
        if my_increasing_string[i] > my_increasing_string[i + 1]:
            increasing = False
            
    if increasing:
        print('The string was in increasing /alphabetical order')
    else:
        print('The list is not increasing')

    """
        <, >, <=, >= all compare strings
        alphabetical order // lexicographic order
    """
    
    print("hello" > "goodbye")
    print("a" < "z")
    print("zebra" < "elephant")
    print("A" < "a")
    # each character has a numerical value (ASCII / UNICODE)
    print(ord('A'), ord('a'), ord('!'), ord('@'), ord('0'), ord(' '), ord('\n'), ord('\r'), ord('\t'))
    
    # this will fix the problem where upper case and lower case have
    # different values
    print('happy' < 'ZEBRA'.lower())
    print('aaaaf' < 'aaaac')
    
    print('end' < 'ending')
    print('z' < 'ending')
    # end of the string counts as number 0, less than all characters
    
    """
        3 functions:
            strip
            split
            join
    
        strip will remove whitespace from the beginning and end of
            a string
    """
    command = input('>> ')
    while command != 'quit':
        print(command.strip())
        command = input('>> ')
    
    # whitespace spaces, \n, \r, \t
    
    # example of killing newlines / carriage returns
    a_new_string = '\n\n\n\t\t\thello\t\t   internal stuff\n\n\t\t\r\r'
    
    print(a_new_string, end='$\n')
    print()
    print(a_new_string.strip(), end='$\n')
    
    refined_thing = command.strip().lower()
    
    """
        split allows us to separate on whitespace
            a single string turns into a list of strings
    """
    
    command = input('>> ')
    while command != 'quit':
        print(command.split())
        command = input('>> ')
    
list_of_numbers = input('Give me a list of numbers: ').split()
# forbidden arts
print([int(x) for x in list_of_numbers])

# currently:
list_of_integers = []
for x in list_of_numbers:
    list_of_integers.append(int(x))
print(list_of_integers)

"""
    What else can split do for you?
        you can split on things that aren't just whitespace
"""

my_string = 'arguably this string and any ancillary artifacts and'

print(my_string.split('a'))

# CSV = comma separated values
line_csv = "Bobson, Bob, 32, 54, 68, 21, 35"
print(line_csv.split(','))
line_csv = "Bobson, Bob\t32\t54\t68\t21\t35"
print(line_csv.split('\t'))

"""
    split can split on multiple letters
"""

print('ear hear fear dear'.split('ea'))

"""
Let's talk about join

    join is the inverse function of split
    split: string -> list[strings]
    join: list[strings] -> string

    string = separator
    separator.join(a list of strings)
"""

words = ['the', 'best', 'words', 'robot', 'key', 'amorphous']

joined_words = ' '.join(words)
print(joined_words)
print(words)


print(', '.join(words))
print('\t'.join(words))
print('an entire string'.join(words))



ea_words = 'ear hear fear dear'.split('ea')
print(ea_words)
print('ea'.join(ea_words))

print('    a    really       spacy      string       '.split())

"""
    ASCII / UNICODE
"""

print('\u2661', '\u2662', '\u2663', '\u2664')