""""
1b
2c
3c
4a
"""

my_list = [1, 2, 3, 4, 5]
# this is a for each loop, not a for-i loop
for i in my_list:
    i *= 2  # i is a copy
    print(i)

print(my_list)

# range(len(...))
for index in range(len(my_list)):
    my_list[index] *= 2

print(my_list)

"""
    For each uses the elements from a list
    For - i uses indices
"""

"""
5a
6a
7b (not how many can you write, how many will run!)
8c (comparison operator)
9b
10c
11b
12f

"""

robots = ["T-1000", "Bender", "Marvin", "HAL"]
robots.append('Wall-E')
print(len(robots) == 5)

"""
    remove will remove BY ELEMENT
        NOT By INDEX
"""

robots.remove('Bender')
print(robots)
# doesn't work because it doesn't remove by index
# robots.remove(1)
# print(robots)

random_list = [1, 2, 5, 2, 7, 9]
random_list.remove(2)
print(random_list)
# random_list.remove(17)

del random_list[3]  # target the 7
print(random_list)
"""
13) Marvin
14) True
15) Error (you don't have to specify ValueError)
"""

height = 0
age = 20
"""
An expression that evaluates to True if and
only if the variable age is not less than 15 and the
variable height is greater than 50

expression = the thing that goes into the if statement
"""
age >= 15 and height > 50
not (age < 15) and height > 50  # yes

"""
An expression that evaluates to True if and only if the
list best_activities has 7 or more items,
the first item is "nap" and does not contain the item "chicanery"
"""
best_activities = []  # don't include this

len(best_activities) >= 7 and best_activities[0] == 'nap' and \
'chicanery' not in best_activities

len(best_activities) >= 7 and best_activities[0] == 'nap' and \
not ('chicanery' in best_activities)

"""
18) What do we mean by example?

"""
people = [1, 2, 3, 4]
for i in range(len(people)):
    people[i] += 1

count = 0
my_string = 'aaabbabababbabbabab'
for i in range(len(my_string) - 1):
    if my_string[i] == my_string[i + 1]:
        count += 1

# 20) If you set x = 50, then both biggest and
#       big will print if you make the change to an if statement.
#       otherwise, it will just print biggest.

# 22) ['Nothing', 'Got', 'I']
# don't be tricked
"""
    Nothing
    Got
    I
"""

"""
23)
    10
    8
    6
    4

24)
    6
"""

"""
8) should be range(len(characters))
9) should be == not assignment
13) add colon to end of line
14) change == to != (logic not syntax)
20) add a print statement
21) change else to elif
"""

if __name__ == '__main__':
    list_of_nums = []
    for i in range(5):
        list_of_nums.append(int(input('Enter Number: ')))

    for x in list_of_nums:
        if x % 2 == 0:
            print(x)


num = int(input('Number! '))
temp = num
count = 0
while temp > 1:
    temp //= 2
    count += 1
    
print(f'You can divide {num} by 2 {count} times')