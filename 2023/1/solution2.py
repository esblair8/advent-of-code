import re

calibration_values = []

digit_string_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}


def regex_find_first_and_last_digit(str):
    regex_result = re.findall(
        rf'(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))', line)
    return (regex_result[0], regex_result[-1])

with open('test.txt', 'r') as file:
    lines = file.read().split('\n')
    for line in lines:
        digits = regex_find_first_and_last_digit(line)
        first_digit = digit_string_dict.get(digits[0])
        last_digit = digit_string_dict.get(digits[-1])
        value = str(first_digit) + str(last_digit)
        calibration_values.append(value)

print(sum(map(int, calibration_values)))
