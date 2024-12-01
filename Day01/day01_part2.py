
CURRENT_DAY = '01'
list_one = []
key_count_dict = {}
result = 0

file = open(f'day{CURRENT_DAY}_input.txt', 'r')
for line in file:
    input = line.strip('\n').split('   ')

    list_one.append(int(input[0]))
    key_count_dict.update({input[1]: key_count_dict.setdefault(input[1], 0) + 1})


for i in range(len(list_one)):
    result += list_one[i] * key_count_dict[str(list_one[i])] if str(list_one[i]) in key_count_dict.keys() else 0

print(f'Result: {str(result)}')
