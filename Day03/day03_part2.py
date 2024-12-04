import re

CURRENT_DAY = '03'


def get_input():
    file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
    return [line.strip('\n') for line in file]


input_list = get_input()
writing = True
result = 0

for line in input_list:
    # line = re.sub("don't\(\)[^d]+do\(\)", '', line)
    char_block = ''
    new_line = ''
    for char in line:
        char_block += char
        if char_block == 'do()':
            writing = True
            char_block = ''
        elif char_block == "don't()":
            writing = False
            char_block = ''
        elif not 'do()'.startswith(char_block) and not "don't()".startswith(char_block):
            char_block = ''

        if writing:
            new_line += char

    matches = re.findall('mul\([0-9]+,[0-9]+\)', new_line)
    for match in matches:
        values = match.replace('mul(', '').replace(')', '').split(',')
        result += int(values[0]) * int(values[1])


print(f'Result: {str(result)}')
# 155803863 >
# 114257865 >
# 89846869 >
# Dachte für jede Linie muss die writing-condition mit true initialisiert werden....
