"""
Advent of Code - Day 4: Camp Cleanup
"""

# load input file
with open('input.txt', 'r') as input:
    sap = input.read()

sap = sap.splitlines()


# Function to split each line of input into pairs to compare section assignments for each pair
def sub_pair(pair):
    elf_one_start, elf_one_end = pair.split(',')[0].split('-')
    elf_two_start, elf_two_end = pair.split(',')[1].split('-')
    return int(elf_one_start), int(elf_one_end), int(elf_two_start), int(
        elf_two_end)


############
# Part One
############

count_assignment_pairs = 0
for pair in sap:

    sub_pair_one_start, sub_pair_one_end, sub_pair_two_start, sub_pair_two_end = sub_pair(
        pair)

    if ((sub_pair_one_start >= sub_pair_two_start
         and sub_pair_one_end <= sub_pair_two_end)
            or (sub_pair_two_start >= sub_pair_one_start
                and sub_pair_two_end <= sub_pair_one_end)):
        count_assignment_pairs += 1

print(count_assignment_pairs)

############
# Part Two
############
count_assignment_pairs_2 = 0
for pair in sap:

    sub_pair_one_start, sub_pair_one_end, sub_pair_two_start, sub_pair_two_end = sub_pair(
        pair)

    if ((sub_pair_one_start >= sub_pair_two_start) and
        (sub_pair_one_start <= sub_pair_two_end)) or (
            (sub_pair_two_start >= sub_pair_one_start) and
            (sub_pair_two_start <= sub_pair_one_end)):
        count_assignment_pairs_2 += 1

print(count_assignment_pairs_2)
