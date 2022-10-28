"""
    Dictionaries - python
        Hash, Hash Map, Hash Table
    Dictionary is "like a list"
        except instead of using indices, it uses "keys"
        
    To create a dictionary, you can use:
        {}
        dict()
"""
new_dictionary = {}
other_thing = dict()

"""
    For a list, you can generally only access by index
    indices don't really have any intrinsic meaning
"""
a_list = [2, 6, 3, 7, 4, 3, 7, 4, 2]

"""
    What if we wanted to store grades?
        we can access a grade for a test by the student's name/ID
"""
grade_dict = {}
grade_dict['Eric'] = 75
grade_dict['Sally'] = 92
grade_dict['Roberto'] = 88
"""
    To store things in a dictionary, you use the first assignment.

    The way things are stored is as "key value pairs"
    Use the key like you would an index, to access the value.
    It doesn't go backwards,
"""
print(grade_dict)
print(grade_dict['Roberto'])


# KeyError, 88 is a value not a key
# print(grade_dict[88])


def count_frequency(text):
    words = text.lower().split()
    frequencies = {}
    for word in words:
        # checks to see if word is a key in the dictionary
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    
    return frequencies

frequencies = count_frequency(input(":: "))
print(frequencies)

"""
    Use in keyword to check if an element is a KEY in the dictionary
        in doesn't work with values
"""
print(88 in grade_dict)

hex_conversion = {'0': 0, '1': 1, '2': 2, '3': 3,
                  '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                  '9': 9, 'a': 10, 'b': 11, 'c': 12,
                  'd': 13, 'e': 14, 'f': 15}


# the right answer for hex -> dec conversion

def hex_to_dec(the_hex):
    current_power = 1
    total = 0
    for i in range(len(the_hex) - 1, -1, -1):
        total += hex_conversion[the_hex[i]] * current_power
        current_power *= 16
    
    return total


print(hex_to_dec('aa'))  # 10 * 16 + 10 = 170

"""
    Don't do this on the project
    
    Mutability:
        immutable = int, float, bool, string, None
            pass by value = a copy is made
            if you change it in the function, no change is
                made to the original variable
        mutable = lists, dicts, classes, etc
            pass by reference = it "renames the variable" temporarily
                both names are referencing the exact same list/dict
pass by value
def square_me(x):
    x = x ** 2
    return x

y = 5
print(square_me(y))
print(y)
"""

"""
    Don't use is, use ==, unless you really really want is
    
list_a = [1, 2]
list_b = [1, 2]
print(list_a is list_b, list_a == list_b)

"""


def sign_in(person, timestamp, access_list):
    if person in access_list:
        access_list[person] = [True, timestamp]
    else:
        print(f'{person} is not allowed access')


def sign_out(person, timestamp, access_list):
    if person in access_list:
        if access_list[person][0]:
            access_list[person] = [False, timestamp]
        else:
            print(f'{person} is not signed in.')
    else:
        print(f'{person} is not in the access list')


def add_user(person, access_list):
    access_list[person] = [False, '00:00:00']


def remove_user(person, access_list):
    # in keyword checks keys not values
    if person in access_list:
        del access_list[person]


user_list = {}
add_user('Eric', user_list)
add_user('Sam', user_list)
add_user('Kaleigh', user_list)
print(user_list)
sign_in('Sam', '03:22:59', user_list)
sign_in('Kaleigh', '04:31:22', user_list)
sign_out('Eric', '05:22:33', user_list)
sign_in('Bender', '04:31:22', user_list)
print(user_list)

"""
    Keys MUST BE immutable
        int, bool, string, float
        int, string
            avoid booleans => there are only two, boring table
            avoid floats => roundoff error/calculation nonsense
    Values can be either mutable or immutable.
    
"""

random_dict = {}
random_dict[True] = 35
random_dict[False] = 17
random_dict['happy'] = 45
random_dict[17] = 4
random_dict[3.333333] = 5
random_dict[10 / 3] = 8
print(random_dict)

"""
    Life lessons, beware of something as horrible as this random_dict
"""
#
# list_a = [1, 2]
# random_dict[list_a] = 14
# list_a.append(5)  # [1, 2, 5]
# random_dict[[1, 2]]
# random_dict[[1, 2, 5]]

my_key = 'happy'
word_dict = {}
word_dict[my_key] = 3
print(word_dict)
my_key = 'sad'
print(word_dict)

"""
    Deleting keys:
        use del keyword
"""
del random_dict['happy']
print(random_dict)

remove_user('Richard', user_list)

new_dict = {'a': 5, 'b': 17, 'c': 14, 'd': 81}
for key in new_dict:
    print('The letter', key, ' has value ', new_dict[key])

for word in frequencies:
    if frequencies[word] > 5:
        print(f'The word {word} occurs {frequencies[word]} many times')


"""
    Once in your life, maybe twice:
"""

print(list(new_dict.keys()))
print(list(new_dict.values()))

total = 0
for x in new_dict:
    total += new_dict[x]

print(total/len(new_dict))


total = 0
for x in new_dict.values():
    total += x
    
print(total / len(new_dict))
"""
    If you are using dict.values() ask yourself, can i do
        this with a list instead of a dict?
"""

print(hash('hello'))

print(hash('hello'))
# place you put "hello" is hash(hello) % list size
