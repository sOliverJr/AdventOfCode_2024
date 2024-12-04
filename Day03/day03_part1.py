import re

CURRENT_DAY = '03'


def get_input():
    file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
    return [line.strip('\n') for line in file]


input_list = get_input()
result = 0

for line in input_list:
    matches = re.findall('mul\([0-9]+,[0-9]+\)', line)
    for match in matches:
        values = match.replace('mul(', '').replace(')', '').split(',')
        result += int(values[0]) * int(values[1])


print(f'Result: {str(result)}')
# First try
