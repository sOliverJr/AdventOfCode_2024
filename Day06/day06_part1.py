CURRENT_DAY = '06'


def read_input():
    map = []
    file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
    for line in file:
        line = line.strip('\n')
        map.append(list(line))
    return map


def change_direction(movement: tuple) -> tuple:
    match movement:
        case (-1, 0):
            return 0, 1     # up -> right
        case (0, 1):
            return 1, 0     # right -> down
        case (1, 0):
            return 0, -1    # down -> left
        case (0, -1):
            return -1, 0    # left -> up


result = 0
map = read_input()
current_position_copy = (0, 0)
movement = (-1, 0)  # up

for y, line in enumerate(map):
    for x, position in enumerate(line):
        if position == '^':
            current_position_copy = (y, x)
            map[current_position_copy[0]][current_position_copy[1]] = 'X'
            break

while True:
    next_position = (current_position_copy[0] + movement[0], current_position_copy[1] + movement[1])
    if not (0 <= next_position[0] < len(map) and 0 <= next_position[1] < len(map[0])):
        break
    if map[next_position[0]][next_position[1]] == '#':
        movement = change_direction(movement)
    else:
        map[next_position[0]][next_position[1]] = 'X'
        current_position_copy = next_position

for y, line in enumerate(map):
    for x, position in enumerate(line):
        if position == 'X':
            result += 1

print(f'Result: {str(result)}')
# First try :)
