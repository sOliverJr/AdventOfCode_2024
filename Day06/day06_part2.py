import copy
from time import time
from alive_progress import alive_bar
CURRENT_DAY = '06'


def timing(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        # print(f'Estimated total brute-force duration: {(t2 - t1) * len(map) * len(map[0]) }s')
        return result

    return wrap_func


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


# @timing
def test_if_map_loops(map_to_test: list[list[str]], current_position: tuple):
    movement = (-1, 0)  # up
    potential_start_of_loop = None
    loops = 0

    while 0 <= current_position[0] < len(map_to_test) and 0 <= current_position[1] < len(map_to_test[0]):
        # Test if map has looped
        if map_to_test[current_position[0]][current_position[1]] == 'X':
            if potential_start_of_loop is None:
                potential_start_of_loop = current_position
            elif current_position == potential_start_of_loop:
                if loops >= 2:
                    return True
                else:
                    loops += 1
        else:
            potential_start_of_loop = None
            loops = 0

        map_to_test[current_position[0]][current_position[1]] = 'X'

        potential_new_position = (current_position[0] + movement[0], current_position[1] + movement[1])
        try:
            if map_to_test[potential_new_position[0]][potential_new_position[1]] == '#':
                movement = change_direction(movement)
                current_position = (current_position[0] + movement[0], current_position[1] + movement[1])
            else:
                current_position = potential_new_position
        except IndexError:
            return False
    return False


result = 0
map = read_input()
current_position = (0, 0)

# Find initial position
for y, line in enumerate(map):
    for x, position in enumerate(line):
        if position == '^':
            current_position = (y, x)
            break


def brute_force():
    global result
    with alive_bar(len(map) * len(map[0]), spinner=None, theme='classic', title='Brute-forcing...') as bar:
        for y, line in enumerate(map):
            for x, position in enumerate(line):
                if position != '#':
                    map_copy = copy.deepcopy(map)
                    map_copy[y][x] = '#'
                    result += 1 if test_if_map_loops(map_copy, copy.deepcopy(current_position)) else 0
                bar()


brute_force()
print(f'Result: {str(result)}')
# 1711 >
# not getting to work...
