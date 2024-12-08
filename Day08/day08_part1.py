import copy
CURRENT_DAY = '08'


def read_input() -> list:
    input = []
    file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
    for line in file:
        line = line.strip('\n')
        input.append(list(line))

    return input


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

            antinode_one = (antenna_one[0] + difference[0], antenna_one[1] + difference[1])
            antinode_two = (antenna_two[0] + (difference[0] * -1), antenna_two[1] + (difference[1] * -1))
            if 0 <= antinode_one[0] < max_y and 0 <= antinode_one[1] < max_x:
                antinode_map[antenna_one[0] + difference[0]][antenna_one[1] + difference[1]] = '#'
            if 0 <= antinode_two[0] < max_y and 0 <= antinode_two[1] < max_x:
                antinode_map[antenna_two[0] + (difference[0] * -1)][antenna_two[1] + (difference[1] * -1)] = '#'

# Count "antinodes"
for y, row in enumerate(antinode_map):
    for x, element in enumerate(row):
        if element == '#':
            result += 1

print(f'Result: {str(result)}')
# 2092 >
# Python arrays... index[-1] == index[len(index)-1-1]
