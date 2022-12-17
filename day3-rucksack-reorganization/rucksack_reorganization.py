"""
Advent of Code - Day 3: Rucksack Reorganization
"""

import string

with open('input.txt', 'r') as input:
    rucksacks = input.read()

rucksacks = rucksacks.splitlines()

items_dict = {}
lowercase_items = list(string.ascii_lowercase)
uppercase_items = list(string.ascii_uppercase)
all_items = lowercase_items + uppercase_items
priorities = list(range(1, 52 + 1))
items_dict = dict(zip(all_items, priorities))
'''
Part One
'''
sum_of_priorities = 0
total_items = 0

for rucksack in rucksacks:
    total_items = len(rucksack) // 2
    rucksack_1 = rucksack[:total_items]
    rucksack_2 = rucksack[total_items:]

    for letter in rucksack_1:
        if letter in rucksack_2:
            item_priority = items_dict.get(letter)
    sum_of_priorities += item_priority

print(sum_of_priorities)
'''
Part Two
'''
number_of_rucksacks = len(rucksacks)
group_size = 3
groups_of_elves = [
    rucksacks[i:i + group_size]
    for i in range(0, number_of_rucksacks, group_size)
]
sum_of_priorities_2 = 0
for group in groups_of_elves:
    sack_1, sack_2, sack_3 = list(group[0]), list(group[1]), list(group[2])
    sack_1_unique, sack_2_unique, sack_3_unique = list(
        dict.fromkeys(sack_1)), list(dict.fromkeys(sack_2)), list(
            dict.fromkeys(sack_3))
    for letter in sack_1_unique:
        if (letter in sack_2_unique) and (letter in sack_3_unique):
            badge_priority = items_dict.get(letter)
    sum_of_priorities_2 += badge_priority

print(sum_of_priorities_2)
