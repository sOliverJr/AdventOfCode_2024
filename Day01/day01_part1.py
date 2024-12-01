
CURRENT_DAY = '01'


def get_input():
    file = open(f'day{ CURRENT_DAY }_input.txt', 'r')
    for line in file:
        input = line.split('   ')
        list_one.append(int(input[0]))
        list_two.append(int(input[1]))


list_one = []
list_two = []

get_input()

# Sorry :D
list_one.sort()
list_two.sort()

result = 0

for i in range(len(list_one)):
    result += abs(list_one[i] - list_two[i])

print(f'Result: {str(result)}')
