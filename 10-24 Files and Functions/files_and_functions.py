"""
    File IO - not the moon of jupiter
        Input/Output
        
        We already know some input output,
            console input/output
                input, print
        Everything is "very similar but just different enough
            to be annoying"
"""
"""
    LIMIT(t-> infinity) CL(s) = 0

    a file name is a string.
        generally you'll have the filename . extension
        tells user what kind of file it is
        tells the operating system what kind of file it is (probably)

    How to open a file:
        use the open command
"""
my_sample_file = open('sample.txt')
# what comes out is not exactly the text in the file
# it's a file object that we can read from, or write to.

"""
    3 read methods we're going to use
    
"""
# .read() method reads the entire function at once
# gives you a single string, not separated in any way.
print(my_sample_file.read())
# first difference, read methods will give you line returns
print("and now this", my_sample_file.read())
# keep in mind that if you read again, nothing should come out because
# "read pointer" = cursor is at the end of the file

# how do we reset, and read again? close the file
my_sample_file.close()
#  always close the files that you open

"""
    What if I want to read the file line by line?
        More like input would.
"""
read_file_again = open('sample.txt')
for line in read_file_again:
    print(line.strip())
    # remember that print will add a new line \n
    
"""
    all of the file read functions do not remove any newlines
        or carriage returns
"""
read_file_again.close()

# secret second argument, defaults to 'r'
#   'r' = read mode
reopen_the_file = open('sample.txt', 'r')
my_lines = reopen_the_file.readlines()
print(my_lines)
reopen_the_file.close()
"""
    Want to give you all the possible options, you pick the one that
        works for you.
        
        Not in this class, but in real life: be very careful about
            reading files entirely.
"""

"""
    Last file read method:
        .readline()
"""

reopen_a_last_time = open('sample.txt', 'r')
the_string = reopen_a_last_time.readline()
while the_string:
    print(the_string)
    the_string = reopen_a_last_time.readline()

reopen_a_last_time.close()

"""
    How do we write to files?
        instead of opening them with read mode, you must open
            them in write mode.
        You must use the 'w' modifier.
"""

new_file = open('second_sample.txt', 'w')

in_string = input('tell me something: ')
while in_string != "quit":
    # remember that write will NOT add any newlines
    new_file.write(in_string + '\n')
    in_string = input('tell me something: ')

new_file.close()
# write mode WILL DELETE your data
# in general you will probably have to add newlines


new_file = open('third_sample.txt', 'w')

file_list = []
in_string = input('tell me something: ')
while in_string != "quit":
    # remember that write will NOT add any newlines
    file_list.append(in_string + "\n")
    in_string = input('tell me something: ')

new_file.writelines(file_list)
new_file.close()

"""
    Syntactic Sugar = stuff that does nothing extra
        but it looks cooler, nicer syntax
"""

with open('sample.txt') as the_file:
    print(the_file.read())
    # I didn't close it
    # secret code = the_file.close()


"""
    Last file mode = append mode
        open the file with write permissions
            NOT going to blank out the file
            set the cursor at the end
"""

with open('second_sample.txt', 'a') as append_file:
    file_list = []
    in_string = input('tell me something: ')
    while in_string != "quit":
        # remember that write will NOT add any newlines
        file_list.append(in_string + "\n")
        in_string = input('tell me something: ')
    append_file.writelines(file_list)
