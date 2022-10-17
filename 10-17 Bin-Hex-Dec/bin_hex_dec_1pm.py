"""

"""

"""
    while number != 0
        next bit = mod by 2
        divide by 2
:param number:
:return:
"""


def convert_dec_to_bin(number):
    result = ''
    while number != 0:
        if number % 2:
            # result = result + '1'
            result = '1' + result
        else:
            result = '0' + result
        number //= 2
    return result


# 1100
print(convert_dec_to_bin(3821))


def convert_dec_to_hex(number):
    HEX_LIST = ['0', '1', '2', '3', '4', '5',
                '6', '7', '8', '9', 'A', 'B',
                'C', 'D', 'E', 'F']
    if number == 0:
        return '0'
    result = ''
    while number != 0:
        result = HEX_LIST[number % 16] + result
        number //= 16  # change the base
    return result


# hex num is actually a string containing 0-9, a-f
def convert_from_hex_to_dec(hex_num):
    current_base = 1
    total = 0
    for i in range(len(hex_num) - 1, -1, -1):
        # print(hex_num[i])
        if '0' <= hex_num[i] <= '9':
            total += current_base * int(hex_num[i])
        elif hex_num[i] == 'a':
            total += current_base * 10
        elif hex_num[i] == 'b':
            total += current_base * 11
        elif hex_num[i] == 'c':
            total += current_base * 12
        elif hex_num[i] == 'd':
            total += current_base * 13
        elif hex_num[i] == 'e':
            total += current_base * 14
        elif hex_num[i] == 'f':
            total += current_base * 15

        current_base *= 16
    return total
    


num = input('Convert me to dec: ')
while num != 0:
    print(convert_from_hex_to_dec(num))
    num = input('Convert me to dec: ')

    