"""
Advent of Code - Day 11: Monkey in the Middle
"""
with open('input.txt', 'r') as input:
    notes = input.read()

notes = notes.splitlines()

###########
# Part One
###########
monkey_dict = {}

for line in range(0, len(notes), 7):

    operation = notes[line + 2].split(':')[1].split(sep='=')[1].lstrip()
    test = int(notes[line + 3].split(':')[1].split(sep=' ')[3])
    is_true = notes[line + 4][-8:].capitalize()
    is_false = notes[line + 5][-8:].capitalize()

    items = [
        int(level)
        for level in notes[line + 1].lstrip('Starting items:').split(sep=',')
    ]

    monkey_dict[notes[line].strip(':')] = {
        'items': items,
        'operation': operation,
        'test': test,
        'is_true': is_true,
        'is_false': is_false,
        'number_inspections': 0
    }

rounds = 20
for round in range(rounds):
    for monkey in monkey_dict.values():

        starting_items = monkey['items']
        number_inspections = len(starting_items)

        monkey['number_inspections'] += number_inspections

        for item in starting_items:
            old = item
            new = eval(monkey['operation']) // 3

            toss_to = 'is_true' if new % monkey['test'] == 0 else 'is_false'
            monkey_dict[monkey[toss_to]]['items'].append(new)

        monkey['items'] = []

inspections_list = [
    monkey['number_inspections'] for monkey in monkey_dict.values()
]

inspections_list.sort()
monkey_business = inspections_list[-2] * inspections_list[-1]
print(monkey_business)

###########
# Part Two
###########
