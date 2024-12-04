CURRENT_DAY = '04'


def get_input():
    file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
    return [list(line.strip('\n')) for line in file]


input_list = get_input()
result = 0


def test_forward_slash_diagonal(x: int, y: int):
    string = input_list[y+1][x-1] + input_list[y][x] + input_list[y-1][x+1]
    if string in ['MAS', 'SAM']:
        return True
    else:
        return False


def test_back_slash_diagonal(x: int, y: int):
    string = input_list[y-1][x-1] + input_list[y][x] + input_list[y+1][x+1]
    if string in ['MAS', 'SAM']:
        return True
    else:
        return False


for y, line in enumerate(input_list):
    for x, char in enumerate(line):
        if y == 0 or x == 0 or y == len(input_list)-1 or x == len(input_list[0])-1:
            continue
        if char == 'A':
            if test_forward_slash_diagonal(x, y) and test_back_slash_diagonal(x, y):
                result += 1

print(f'Result: {str(result)}')

# 2044 >
# fyi, arr[-1] returns last value of array in python...
