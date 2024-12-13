import os

# Specify the directory name
current_day = '09'

# Create the directory
directory_name = f'Day{current_day}'
try:
    os.mkdir(directory_name)
    open(f'{directory_name}/day{current_day}_input.txt', "a").close()
    open(f'{directory_name}/day{current_day}_part2.py', "a").close()
    f = open(f'{directory_name}/day{current_day}_part1.py', "a")
    f.write(open("Day08/day08_part1.py", "r").read())
    f.close()
except Exception as e:
    print(f"An error occurred: {e}")
