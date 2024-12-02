
CURRENT_DAY = '02'


def get_input():
    file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
    return [line.strip('\n') for line in file]


input_list = get_input()

correct_lines = 0
for line in input_list:
    line_is_correct = True
    line_values = line.split(' ')
    ascending = int(line_values[0]) - int(line_values[1]) > 0

    for i in range(len(line_values)-1):
        diff = int(line_values[i]) - int(line_values[i+1])
        if (diff < 0 and ascending) or (diff > 0 and not ascending):
            line_is_correct = False
            break
        diff = diff if ascending else abs(diff)
        if not (1 <= diff <= 3):
            line_is_correct = False
            break

    if line_is_correct:
        correct_lines += 1


print(f'Correct lines: {str(correct_lines)}')
# First run & try
