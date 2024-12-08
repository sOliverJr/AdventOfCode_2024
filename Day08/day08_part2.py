import copy
CURRENT_DAY = '08'


def read_input() -> list:
    input = []
    file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
    for line in file:
        line = line.strip('\n')
        input.append(list(line))

    return input


def set_antinode_on_map(coords: tuple) -> bool:
    global antinode_map
    try:
        if coords[0] < 0 or coords[1] < 0:
            return True
        antinode_map[coords[0]][coords[1]] = '#'
        return False
    except IndexError:
        return True


result = 0
antenna_map = read_input()
antenna_positions = {}
max_y = len(antenna_map)
max_x = len(antenna_map[0])

# Sort antenna-positions by frequency
for y, row in enumerate(antenna_map):
    for x, element in enumerate(row):
        if element != '.':
            antenna_positions.setdefault(element, []).append((y, x))

antinode_map = copy.deepcopy(antenna_map)
for antenna_frequency in antenna_positions.keys():
    for i, antenna_one in enumerate(antenna_positions[antenna_frequency]):
        for ii in range(i):     # For every antenna before the current one
            if i == ii:     # Same antenna
                continue
            antenna_two = antenna_positions[antenna_frequency][ii]
            difference = (antenna_one[0] - antenna_two[0], antenna_one[1] - antenna_two[1])

            # Start from antenna_two to overwrite antenna_one
            out_of_range = False
            current_position = antenna_two
            while not out_of_range:
                new_position = (current_position[0] + difference[0], current_position[1] + difference[1])
                out_of_range = set_antinode_on_map(new_position)
                current_position = new_position

            # Start from antenna_one to overwrite antenna_two
            out_of_range = False
            current_position = antenna_one
            while not out_of_range:
                new_position = (current_position[0] + (difference[0] * -1), current_position[1] + (difference[1] * -1))
                out_of_range = set_antinode_on_map(new_position)
                current_position = new_position

# Count "antinodes"
for y, row in enumerate(antinode_map):
    for x, element in enumerate(row):
        if element == '#':
            result += 1

print(f'Result: {str(result)}')
# First Try, but tested on example, otherwise second try :|
