CURRENT_DAY = '05'

instructions = []
updates = []
update_dicts = []
result = 0


def test_and_sort_update(update: dict) -> (bool, dict):
    for instruction in instructions:
        # if both instruction-elements are in the update-list
        if instruction[0] in update.keys() and instruction[1] in update.keys():
            # if the two elements are not in the right order
            if not update[instruction[0]] < update[instruction[1]]:
                # Switch position of elements that are not in the right order
                pos1 = update[instruction[0]]
                pos2 = update[instruction[1]]
                update[instruction[1]] = pos1
                update[instruction[0]] = pos2
                # retry recursively with new order
                _, new_update = test_and_sort_update(update)
                return False, new_update
    return True, update


file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
reading_instructions = True
for line in file:
    line = line.strip('\n')
    if line == '':
        reading_instructions = False
        continue
    if reading_instructions:
        instructions.append(line.split('|'))
    else:
        updates.append(line.split(','))

for update in updates:
    update_dict = {}
    for i, page in enumerate(update):
        update_dict.update({page: i})
    update_dicts.append(update_dict)

for i, update in enumerate(update_dicts):
    was_sorted, update = test_and_sort_update(update)
    # Make list of page:index-dict sorted by their new index
    # -> if dict has been rearranged, key-order does not match index-order
    update = [el[0] for el in sorted(update.items(), key=lambda item: item[1])]
    if not was_sorted:
        # Add element in center of array
        result += int(update[int(len(update)/2)])


print(f'Result: {str(result)}')
# 10999 >
