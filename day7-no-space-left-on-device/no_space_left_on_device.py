"""
Advent of Code - Day 7: No Space Left on Device
"""

import pprint

with open('input.txt', 'r') as file:
    terminal_output = file.read()

terminal_output = terminal_output.splitlines()

current_path = []
current_path_string = ''
current_path_directories = []
current_path_size = 0
device = {}
total_size_all_directories = 0

for input in terminal_output:
    if '$ cd /' in input:
        path_name = '/'
        current_path.append(path_name)
        current_path_string = ''.join(current_path)
        device[current_path_string] = 0

    elif '$ cd' in input:
        if '..' not in input:
            path_name = input[5:]
            current_path.append(path_name)
            current_path_string = '/'.join(current_path)

        else:
            current_path.pop()
            path_name = current_path[-1]
            current_path_string = '/'.join(current_path)

    elif '$ ls' in input:
        pass
    else:
        if 'dir' in input.split():
            dir_name = input.split()[1]
            device['/'.join([current_path_string, dir_name])] = 0
        else:
            file_size = int(input.split()[0])

            if current_path_string in device:
                device[current_path_string] += file_size

                # update parent directory sizes
                current_path_copy = current_path.copy()
                if len(current_path_copy) > 1:
                    for i in range(len(current_path_copy) - 1):
                        current_path_copy.pop()
                        current_path_copy_string = '/'.join(current_path_copy)
                        device[current_path_copy_string] += file_size

            total_size_all_directories += file_size
            current_path_size += file_size

count_of_directories = 0
sum_of_directories = 0
for key, value in device.items():
    if value <= 100000:
        sum_of_directories += value
        count_of_directories += 1

# print("current path", current_path)
# print("current path string", current_path_string)
# print("current path directories", current_path_directories)
# print("current path size", current_path_size)
# pprint.pprint(device)
# print("total size", total_size_all_directories)
# print("total directories:", len(device))
# print("number of directories 100K or less:", count_of_directories)
print("total sum:", sum_of_directories)
