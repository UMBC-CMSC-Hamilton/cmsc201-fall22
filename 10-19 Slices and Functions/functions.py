"""
    Remember how functions work
        definition:
        def function_name(param1, param2, param3):
            code
            return statement
            
    Local variables don't exist outside of their function
        concept: scope - local scope
        
    Mutability:
        Immutable types:
            int bool float string
            whenever they are passed into a function they are
            "passed by value" - local variable is a copy
        Mutable Types:
            list, dictionaries, classes
            mutable types get "passed by reference"
            local variable is actually just a renamed version
                of the global variable
"""


#                   parameters
# local variables that exist within the function
# given by whatever we pass in to the function
def calculate_area(length, width):
    area = length * width
    length = 20
    return area


# notice here we pass in literal values (not a variable)
print(calculate_area(5, 20))
x = 13
y = 241
print(calculate_area(x, y))
print(x)


def append_random(a_list):
    a_list.append('random')
    print(a_list)


my_list = ['sandwich', 'turnip', 'flower', 'sales', 'rhubarb']
# if you are going to pass a list /or dict into a function
# AND if that function is going to modify the list in a way you
# don't like, then you can make a copy
copy_of_list = my_list[:]
append_random(copy_of_list)
print(my_list)


def dot_product(vector_1, vector_2):
    if len(vector_1) != len(vector_2):
        print('Dimensions are not the same')
        # whenever you hit a return, the function will exit
        return 0  # raise an error
        # nothing after this will happen
    
    total = 0
    for i in range(len(vector_1)):
        total += vector_1[i] * vector_2[i]
    
    return total


print(dot_product([1, 2], [-1, 5]))
print(dot_product([1, 2, 3], [-1, 5]))
"""
    What is a return statement?
        a) ends a function
        b) way to give data back to the outside world/global scope
            if all the local variables die ( no longer are accessible)
            we can keep results and give them back.
"""

d = dot_product([1, 2, 3], [3, 2, 1])
print(d)


def make_grid(n_rows, n_cols, fill_with):
    # 2d list
    new_grid = []
    for i in range(n_rows):
        new_row = []
        for j in range(n_cols):
            new_row.append(fill_with)
        new_grid.append(new_row)
    return new_grid


def display_grid(my_grid):
    for row in range(len(my_grid)):
        for col in range(len(my_grid[row])):
            if len(my_grid[row]) - 1 != col:
                print(my_grid[row][col], end='\t')
            else:
                print(my_grid[row][col])

random_list = [['*', 'f', '*'], ['*', 'a', 'b', '*'], ['*', '*'], ['*', '*'], ['*', '*']]

my_grid = make_grid(5, 2, '*')
display_grid(my_grid)

""" You are allowed to call functions from other functions """


def is_prime(x):
    for i in range(2, int(x ** (1/2)) + 1):
        if x % i == 0:
            return False
        
    return True


def get_primes(num_primes):
    x = 2
    list_of_primes = []
    while len(list_of_primes) < num_primes:
        if is_prime(x):
            list_of_primes.append(x)
        x += 1
        
    return list_of_primes


print(get_primes(100))
