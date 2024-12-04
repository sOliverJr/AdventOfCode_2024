CURRENT_DAY = '04'


def get_input():
    file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
    return [list(line.strip('\n')) for line in file]


input_list = get_input()
result = 0


def test_from_position(x: int, y: int):
    test_up(x, y)
    test_down(x, y)
    test_left(x, y)
    test_right(x, y)
    test_ddr(x, y)
    test_ddl(x, y)
    test_dur(x, y)
    test_dul(x, y)


def test_up(x: int, y: int):
    global result
    string = ''
    while True:
        if y < 0:
            return
        string += input_list[y][x]
        if not 'XMAS'.startswith(string):
            return
        elif string == 'XMAS':
            result += 1
            return
        y -= 1


def test_down(x: int, y: int):
    global result
    string = ''
    while True:
        if y > len(input_list)-1:
            return
        string += input_list[y][x]
        if not 'XMAS'.startswith(string):
            return
        elif string == 'XMAS':
            result += 1
            return

        y += 1


def test_left(x: int, y: int):
    global result
    string = ''
    while True:
        if x < 0:
            return
        string += input_list[y][x]
        if not 'XMAS'.startswith(string):
            return
        elif string == 'XMAS':
            result += 1
            return

        x -= 1


def test_right(x: int, y: int):
    global result
    string = ''
    while True:
        if x > len(input_list[0])-1:
            return
        string += input_list[y][x]
        if not 'XMAS'.startswith(string):
            return
        elif string == 'XMAS':
            result += 1
            return

        x += 1


def test_ddr(x, y):
    global result
    string = ''
    while True:
        if x > len(input_list[0])-1 or y > len(input_list)-1:
            return
        string += input_list[y][x]
        if not 'XMAS'.startswith(string):
            return
        elif string == 'XMAS':
            result += 1
            return

        x += 1
        y += 1


def test_ddl(x, y):
    global result
    string = ''
    while True:
        if x < 0 or y > len(input_list)-1:
            return
        string += input_list[y][x]
        if not 'XMAS'.startswith(string):
            return
        elif string == 'XMAS':
            result += 1
            return

        x -= 1
        y += 1


def test_dur(x, y):
    global result
    string = ''
    while True:
        if x > len(input_list[0])-1 or y < 0:
            return
        string += input_list[y][x]
        if not 'XMAS'.startswith(string):
            return
        elif string == 'XMAS':
            result += 1
            return

        x += 1
        y -= 1


def test_dul(x, y):
    global result
    string = ''
    while True:
        if x < 0 or y < 0:
            return
        string += input_list[y][x]
        if not 'XMAS'.startswith(string):
            return
        elif string == 'XMAS':
            result += 1
            return

        x -= 1
        y -= 1


for y, line in enumerate(input_list):
    for x, char in enumerate(line):
        if char == 'X':
            test_from_position(x, y)

print(f'Result: {str(result)}')
# Dirty, but first run & try xD
