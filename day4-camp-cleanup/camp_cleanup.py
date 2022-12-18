"""
Advent of Code - Day 4: Camp Cleanup
"""

# load input file
with open('input.txt', 'r') as input:
    sap = input.read()

sap = sap.splitlines()


# Function to split each line of input into pairs to compare section assignments for each pair
def sub_pair(pair):
    elf_one_start = pair.split(',')[0].split('-')[0]
    elf_one_end = pair.split(',')[0].split('-')[1]
    elf_two_start = pair.split(',')[1].split('-')[0]
    elf_two_end = pair.split(',')[1].split('-')[1]

    elf_one = set(list(range(int(elf_one_start), int(elf_one_end) + 1)))
    elf_two = set(list(range(int(elf_two_start), int(elf_two_end) + 1)))

    return elf_one, elf_two


############
# Part One
############

count_assignment_pairs = 0
for pair in sap:

    sub_pair_one, sub_pair_two = sub_pair(pair)

    if sub_pair_one.issubset(sub_pair_two) or sub_pair_two.issubset(
            sub_pair_one):
        count_assignment_pairs += 1

print(count_assignment_pairs)

############
# Part Two
############
count_assignment_pairs_2 = 0
for pair in sap:

    sub_pair_one, sub_pair_two = sub_pair(pair)

    if len((sub_pair_one & sub_pair_two)) > 0:
        count_assignment_pairs_2 += 1

print(count_assignment_pairs_2)
