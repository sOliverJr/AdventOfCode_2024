CURRENT_DAY = '05'

instructions = []
updates = []
update_dicts = []
result = 0

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
    valid = True
    for instruction in instructions:
        if instruction[0] in update.keys() and instruction[1] in update.keys():
            if not update[instruction[0]] < update[instruction[1]]:
                valid = False
                break

    if valid:
        result += int(updates[i][int(len(updates[i])/2)])


print(f'Result: {str(result)}')
# First run & try :)
