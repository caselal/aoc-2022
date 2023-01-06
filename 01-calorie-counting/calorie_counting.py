"""
Advent of Code - Day 1: Calorie Counting
"""
# load text file
with open('input.txt', 'r') as input:
    calories = input.read()
    calories_split = calories.splitlines()

elf_calories = 0
elves_calories = []

# sum total calories for each elf
for cal in calories_split:
    if cal == '':
        elves_calories.append(elf_calories)
        elf_calories = 0
    else:
        elf_calories += int(cal)

# return highest calories
most_calories = max(elves_calories)
print(most_calories)
'''Part Two'''
elves_calories_sorted = sorted(elves_calories, reverse=True)
print(sum(elves_calories_sorted[0:3]))

# print(calories_split)
# print(type(calories_split))
# print(len(calories_split))
# print(elves_calories)
