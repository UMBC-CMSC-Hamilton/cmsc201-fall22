"""
    Exam is 10-12, Wednesday
        Bring a laptop, or tablet
        
        Hopefully today, we'll release a practice test
            one of the previous exams from the past 2-3 years or so.
        
        Previously it was all on paper.
        
        No discussion next week.
"""

"""
    Let's talk about strings today.
    
    using strings as arrays/lists
    
    strip
    split
    join
    
    for loops and strings
    
    ascii and unicode
    
    maybe slices
"""


def never_run():
    a_string = 'hello I am a string'
    for i in range(len(a_string)):
        print('The current letter is', a_string[i])
        # unfortunately you can't actually assign to an individual
        # string index
    
    # strings are immutable you are not allowed to change them
    # a_string[3] = 'h'
    
    new_string = "hello" + "world"
    # "hello"  "world"   new piece of memory somewhere else "helloworld"
    print(new_string)
    
    word = ''
    for i in range(5):
        # new string is created every time and gets reassigned to the name "word"
        word += input('Tell me something: ')
        print(word)
    
    for i in range(len(word) - 2):
        print(word[i], word[i + 1], word[i + 2])
    
    foo = 3
    bar = 5
    # parties

    
    """
        strip function
        
        lstrip and rstrip - they exist
    """
    string_sample = input("Tell me something: ")
    print(string_sample.strip())
    
    """
        What is whitespace?
            spaces, \n,\r, \t
    """
    
    test_string = "\n\n\t\thello\t\thello again\t \n abcd \n    "
    print(test_string)
    print(test_string.strip(), end='/')
    
    command = input('What is your command? ')
    if command.strip().startswith('run'):
        print('this is a run command')
        
    """
        split
        
            even more useful than strip in a lot of ways
            
            split actually splits the string into a list of substrings
            takes a separator or if you don't put one in, it separates on whitespace
    """
    test_string = input('Tell me a string to split: ')
    while test_string != 'quit':
        print(test_string.split())
        test_string = input('Tell me a string to split: ')
    
    """
        split takes an argument
        
        if you split on non-whitespace then it can give you empty strings
        empty strings remind you that there was something there
    """
    
    test_string = input('Tell me a string to split: ')
    arg = input('Tell me what to split on: ')
    while test_string != 'quit':
        print(test_string.split(arg))
        test_string = input('Tell me a string to split: ')
        arg = input('Tell me what to split on: ')

point_string = input('tell me two numbers like 14, 13')
print(point_string.split(','))
split_string = point_string.split(',')
if len(split_string) == 2:
    x = int(split_string[0])
    y = int(split_string[1])

    print(x, y)
    
int_list = []
for i in range(len(split_string)):
    int_list.append(int(split_string[i]))

print(int_list)

"""
    split + join are like inverse functions
    
    join =
"""

list_of_words = ['happy', 'robot', 'chicken', 'turkey', 'fish', 'salmon', 'tuna']
print(' '.join(list_of_words))

print(list_of_words)

my_example = 'in the beginning there was only C++'
example_list = my_example.split()
print(my_example, example_list)

random_space_words = ['space', 'crew', 'station', 'satellite']
joined_words = ', '.join(random_space_words)
print(random_space_words)
print(joined_words)

# separators can be multiple characters
print('happy'.join(random_space_words))

print('\u2661', '\u2662', '\u2663', '\u2664')


