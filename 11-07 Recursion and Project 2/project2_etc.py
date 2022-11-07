"""
    I want you to submit something for project 2 by the end of this
    week
    I want 3 functions programmed.
    You will get +7 on your exam.
    This sunday.

"""

"""
    How do dictionaries work?
        how should we use them?
        
    dictionaries store keys: values
        keys have to be immutable
        keys = student names nice
        values
"""

a_string = 'abcabababbbcabcabacbcabcabcnaahffajacnbcajajadbca'

"""
make a list of positions where we find the data
"""
my_dict = {}

for i in range(len(a_string)):
    if a_string[i] in my_dict:
        # already created a list
        my_dict[a_string[i]].append(i)
    else:
        # can't append if it doesn't exist.
        my_dict[a_string[i]] = [i]
        
print(my_dict)
