import copy

CURRENT_DAY = '02'


def get_input():
    file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
    return [line.strip('\n') for line in file]


def test_line(line: list):
    ascending = int(line[0]) - int(line[1]) > 0

    for i in range(len(line)-1):
        diff = int(line[i]) - int(line[i+1])
        if (diff < 0 and ascending) or (diff > 0 and not ascending):
            return False
        diff = diff if ascending else abs(diff)
        if not (1 <= diff <= 3):
            return False

    return True


input_list = get_input()

correct_lines = 0
for line in input_list:
    line_values: list = line.split(' ')
    ok = test_line(line_values)

    if not ok:
        for i in range(len(line_values)):
            line_copy = copy.deepcopy(line_values)
            del line_copy[i]
            if test_line(line_copy):
                ok = True
                break

    if ok:
        correct_lines += 1


print(f'Correct lines: {str(correct_lines)}')

# 560 <
# 761 >
# 570 <
# 575
