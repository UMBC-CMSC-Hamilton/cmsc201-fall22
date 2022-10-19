def convert_from_dec_to_bin(number):
    if number == 0:
        return '0'
    
    result = ''
    while number != 0:
        if number % 2:
            result = '1' + result
        else:
            result = '0' + result
        number //= 2
    
    return result


def convert_from_dec_to_hex(number):
    if number == 0:
        return '0'
    
    result = ''
    while number != 0:
        if 0 <= number % 16 <= 9:
            result = str(number % 16) + result
        elif number % 16 == 10:
            result = 'A' + result
        elif number % 16 == 11:
            result = 'B' + result
        elif number % 16 == 12:
            result = 'C' + result
        elif number % 16 == 13:
            result = 'D' + result
        elif number % 16 == 14:
            result = 'E' + result
        elif number % 16 == 15:
            result = 'F' + result

        number //= 16
    
    return result


def convert_from_hex_to_dec(hex_num):
    hex_num = hex_num.upper()
    total = 0
    current_power = 1
    for i in range(len(hex_num) - 1, -1, -1):
        if '0' <= hex_num[i] <= '9':
            total += int(hex_num[i]) * current_power
        elif hex_num[i] == 'A':
            total += 10 * current_power
        elif hex_num[i] == 'B':
            total += 11 * current_power
        elif hex_num[i] == 'C':
            total += 12 * current_power
        elif hex_num[i] == 'D':
            total += 13 * current_power
        elif hex_num[i] == 'E':
            total += 14 * current_power
        elif hex_num[i] == 'F':
            total += 15 * current_power

        current_power *= 16
    return total


print(convert_from_dec_to_bin(12))

number = input('Tell me number: ')
while number != 0:
    print(convert_from_hex_to_dec(number), int(number, base=16))
    number = input('Tell me number: ')
