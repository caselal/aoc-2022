"""
Advent of Code - Day 11: Monkey in the Middle
"""
with open('input.txt', 'r') as input:
    notes = input.read()

notes = notes.splitlines()


def monkeys_dict(monkey_notes):
    monkey_dict = {}

    for line in range(0, len(monkey_notes), 7):

        operation = monkey_notes[line +
                                 2].split(':')[1].split(sep='=')[1].lstrip()
        test = int(monkey_notes[line + 3].split(':')[1].split(sep=' ')[3])
        is_true = monkey_notes[line + 4][-8:].capitalize()
        is_false = monkey_notes[line + 5][-8:].capitalize()

        items = [
            int(level)
            for level in monkey_notes[line +
                                      1].lstrip('Starting items:').split(
                                          sep=',')
        ]

        monkey_dict[monkey_notes[line].strip(':')] = {
            'items': items,
            'operation': operation,
            'test': test,
            'is_true': is_true,
            'is_false': is_false,
            'number_inspections': 0
        }
    return monkey_dict


###########
# Part One
###########
monkey_dict_1 = monkeys_dict(notes)
rounds = 20

for round in range(rounds):
    for monkey in monkey_dict_1.values():

        starting_items = monkey['items']
        number_inspections = len(starting_items)

        monkey['number_inspections'] += number_inspections

        for item in starting_items:
            old = item
            new = eval(monkey['operation']) // 3

            toss_to = 'is_true' if new % monkey['test'] == 0 else 'is_false'
            monkey_dict_1[monkey[toss_to]]['items'].append(new)

        monkey['items'] = []

inspections_list = [
    monkey['number_inspections'] for monkey in monkey_dict_1.values()
]

inspections_list.sort()
monkey_business = inspections_list[-2] * inspections_list[-1]
print(monkey_business)

###########
# Part Two
###########
monkey_dict_2 = monkeys_dict(notes)
rounds = 10000
lcm = 1
for monkey in monkey_dict_2.values():
    lcm *= monkey['test']

for round in range(rounds):

    for monkey in monkey_dict_2.values():

        starting_items = monkey['items']
        number_inspections = len(starting_items)

        monkey['number_inspections'] += number_inspections

        for item in starting_items:
            old = item
            new = eval(monkey['operation'])

            toss_to = 'is_true' if new % monkey['test'] == 0 else 'is_false'
            monkey_dict_2[monkey[toss_to]]['items'].append(new % lcm)

        monkey['items'] = []

inspections_list = [
    monkey['number_inspections'] for monkey in monkey_dict_2.values()
]

inspections_list.sort()
monkey_business = inspections_list[-2] * inspections_list[-1]
print(monkey_business)
