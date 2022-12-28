"""
Advent of Code - Day 7: No Space Left on Device
"""
############
# Part One
############
with open('input.txt', 'r') as file:
    terminal_output = file.read()

terminal_output = terminal_output.splitlines()

current_path = []
current_path_directories = []
device = {}

for input in terminal_output:
    if '$ cd /' in input:
        current_path = ['/']
        device['/'] = 0

    elif '$ cd' in input:
        if '..' in input:
            current_path.pop()
        else:
            current_path.append(input[5:])

    elif '$ ls' in input:
        pass

    elif 'dir' in input.split():
        dir_name = input.split()[1]
        device['/'.join(current_path + [dir_name])] = 0
    else:
        file_size = int(input.split()[0])

        for i, dir in enumerate(current_path):
            current_path_string = '/'.join(current_path[:len(current_path) -
                                                        i])
            device[current_path_string] += file_size

sum_of_directories = 0
for value in device.values():
    if value <= 100000:
        sum_of_directories += value

print("total sum:", sum_of_directories)

############
# Part Two
############
device_size = device.get('/')
unused_space = 70000000 - device.get('/')
space_needed = 30000000
difference = space_needed - unused_space

directory_options = {}
for key, value in device.items():
    if value >= difference:
        directory_options[key] = value

smallest_directory_to_remove = min(directory_options,
                                   key=directory_options.get)

print("directory to remove:", smallest_directory_to_remove)
print("directory size:", directory_options.get(smallest_directory_to_remove))
