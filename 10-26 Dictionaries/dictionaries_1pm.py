"""

    What is a dictionary?
        We have lists
        Use array brackets to access elements
        But you don't have to use integers, use strings, floats (avoid)

    HashMaps, Hash Tables
"""

my_dictionary = {}  # not [] it's curly braces
other_way = dict()

# inserting elements into a dictionary
my_dictionary["apple"] = 4
my_dictionary["pear"] = 2
print(my_dictionary)
"""
    Instead of having indices we have what are called:
    "key: value" pairs

    To insert elements, you just assign them.
"""

my_dictionary["apple"] = 17
print(my_dictionary)


# print(my_dictionary[17]) Key Error 17 is not a key


def count_words(text_block):
    words = text_block.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts


"""
    To delete something out of a dictionary, you will use the
        del keyword
"""
my_dictionary['rabbit'] = 14
print(my_dictionary)
del my_dictionary['rabbit']
print(my_dictionary)

"""
The access time for any of these elements should be similar
to the access time for a list.
hash tables/dictionaries generally pretty fast
Futurespeak = O(1)
"""

# declare a dictionary, use the Key:value pairs
user_accounts = {'Eric': True, 'Ben': False, 'Sally': True}
del user_accounts['Eric']
print(user_accounts)

"""
    Mutability
    
    immutable: int, float, bool, string, None
        pass by value: a copy is made
    mutable: lists, dictionaries (yep they are)
        pass a dictionary into a function it passes by reference
            you can modify the dictionary in the function
        (usually true): if you have some basic data type -> immutable
        (containers): mutable
            except: datetime and tuples
"""


def add_random_key(my_dict):
    my_dict['random'] = 5


new_dict = {'a': 4, 'b': 7, 'c': 19, 'd': 1}
print(new_dict)
add_random_key(new_dict)
print(new_dict)

exam_grades = {'Eric': 82, 'Jim': 99, 'Sally': 92}

"""
    you can use a for loop to access KEYS not values
        for loops give you keys, not values
        you can use that key to access the dictionary/value
"""
for x in exam_grades:
    print(x, 'got a', exam_grades[x])

weird_thing = [3, 2, 5, 7, ]

user_list = {'Eric': [False, '03:22:15'],
             'Tim': [False, '03:22:15'],
             'Joe': [False, '03:22:15'],
             'Margaret': [False, '03:22:15'],
             }


def swipe_in(person, timestamp, access_list):
    if person in access_list:
        access_list[person][0] = True
        access_list[person][1] = timestamp
    else:
        print(f'{person} is not in the allowed access list')


def swipe_out(person, timestamp, access_list):
    if person in access_list:
        access_list[person] = [True, timestamp]
    else:
        print(f'{person} is not in the allowed access list')

def add_user(person, access_list):
    access_list[person] = [False, '00:00:00']
    

swipe_in('Eric', '05:22:37', user_list)
print(user_list)
swipe_in('Robert', '06:32:57', user_list)
add_user('Jill', user_list)
print(user_list)

"""
    Keys of dictionaries MUST BE IMMUTABLE
   
        bad code:
        my_list = [1, 2]
        other_list = [3, 4]
        the_dict = {my_list: 3, other_list: 4}
        the_dict[[1, 2]] = 5
        my_list.append(5)
        the_dict[[1, 2]]
        the_dict[[1, 2, 5]]  # this is probably "right"
    Values can be whatever, mutable, immutable,
        lists, dictionaries, etc
        
    key = strings, ints
        avoid floats = roundoff error
        avoid bools = only two bools (True, False) not much option
"""

random_thing = {3.33: 'hello'}
random_thing[10/3] = 5
print(random_thing)

"""
    two functions:
        keys()
        values()
"""

print(user_list.keys())
for name in user_list.keys():
    print(name)

# use this instead (cleaner, more pythonic)
for name in user_list:
    print(name)
    
"""
    values method
    dict.values() -> list of values
"""
print(user_list.values())
print(exam_grades.values())
"""
    if i am using .values() a lot, do i need a dictionary?
    or can i just use a list instead?
"""

"""
    GPS position: what's there
    
        tuple = immutable list cannot change it
            everything except assignment, append, delete
"""
one_element_tuple = (5,)

locations = {}
eiffel_tower_gps = (48.8584, 2.2945)
print(eiffel_tower_gps)
locations[eiffel_tower_gps] = 'Eiffel Tower'
print(locations)