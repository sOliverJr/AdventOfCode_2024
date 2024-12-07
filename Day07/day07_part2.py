import itertools
CURRENT_DAY = '07'


def read_input():
    input = []
    file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
    for line in file:
        line = line.strip('\n').split(': ')
        input.append({
            'result': int(line[0]),
            'elements': [int(number) for number in line[1].split(' ')]
        })
    return input


def test_instruction_set(equation: dict, instruction_set: tuple) -> bool:
    result = equation['elements'][0]
    for i, operation in enumerate(instruction_set):
        if operation == '+':
            result += equation['elements'][i+1]
        elif operation == '*':
            result *= equation['elements'][i+1]
        elif operation == '||':
            result = int(str(result) + str(equation['elements'][i+1]))

    return result == equation['result']


def test_equation(equation: dict) -> bool:
    instructions = list(itertools.product(['+', '*', '||'], repeat=len(equation['elements'])-1))
    for instruction in instructions:
        equation_is_possible = test_instruction_set(equation, instruction)
        if equation_is_possible:
            return True
    return False


result = 0
equations = read_input()

for equation in equations:
    if test_equation(equation):
        result += equation['result']

print(f'Result: {str(result)}')
# Also first run & try - not very complicated today
