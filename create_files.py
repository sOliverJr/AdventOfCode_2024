import os

current_day = '09'
directory_name = f'Day{current_day}'

part1 = f"""CURRENT_DAY = '{current_day}'


def read_input() -> list:
    input = []
    file = open(f'day{ current_day }_input.txt', 'r')
    for line in file:
        line = line.strip('\\n')
        input.append(list(line))

    return input


result = 0

# Logik

print('Result:' + str(result))
# First run & Try :)
"""

try:
    os.mkdir(directory_name)
    open(f'{directory_name}/day{current_day}_input.txt', "a").close()
    open(f'{directory_name}/day{current_day}_part2.py', "a").close()
    f = open(f'{directory_name}/day{current_day}_part1.py', "a")
    f.write(part1)
    f.close()
except Exception as e:
    print(f"An error occurred: {e}")
