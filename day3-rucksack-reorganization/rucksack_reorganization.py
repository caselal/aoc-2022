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
    rucksack_1 = set(rucksack[:total_items])
    rucksack_2 = set(rucksack[total_items:])
    item_priority = items_dict.get(list(rucksack_1 & rucksack_2)[0])
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
    intersection = set(group[0])
    for sack in group[1:]:
        intersection &= set(sack)
    badge_priority = items_dict.get(intersection.pop())
    sum_of_priorities_2 += badge_priority

print(sum_of_priorities_2)
