"""
Advent of Code - Day 4: Camp Cleanup
"""

with open('input.txt', 'r') as input:
    sap = input.read()

sap = sap.splitlines()

############
# Part One
############

count_assignment_pairs = 0
for pair in sap:

    sub_pair_one_start = pair.split(',')[0].split('-')[0]
    sub_pair_one_end = pair.split(',')[0].split('-')[1]
    sub_pair_two_start = pair.split(',')[1].split('-')[0]
    sub_pair_two_end = pair.split(',')[1].split('-')[1]

    sub_pair_one = set(
        list(range(int(sub_pair_one_start),
                   int(sub_pair_one_end) + 1)))
    sub_pair_two = set(
        list(range(int(sub_pair_two_start),
                   int(sub_pair_two_end) + 1)))

    if sub_pair_one.issubset(sub_pair_two) or sub_pair_two.issubset(
            sub_pair_one):
        count_assignment_pairs += 1

print(count_assignment_pairs)

############
# Part Two
############
count_assignment_pairs_2 = 0
for pair in sap:

    sub_pair_one_start = pair.split(',')[0].split('-')[0]
    sub_pair_one_end = pair.split(',')[0].split('-')[1]
    sub_pair_two_start = pair.split(',')[1].split('-')[0]
    sub_pair_two_end = pair.split(',')[1].split('-')[1]

    sub_pair_one = set(
        list(range(int(sub_pair_one_start),
                   int(sub_pair_one_end) + 1)))
    sub_pair_two = set(
        list(range(int(sub_pair_two_start),
                   int(sub_pair_two_end) + 1)))

    if len((sub_pair_one & sub_pair_two)) > 0:
        count_assignment_pairs_2 += 1

print(count_assignment_pairs_2)
