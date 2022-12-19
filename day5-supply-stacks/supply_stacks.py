"""
Advent of Code - Day 5: Supply Stacks
"""
# load data file
with open('input.txt', 'r') as input:
    supplies = input.read()

supplies = supplies.splitlines()


# create initial supply stacks
def supply_stacks():
    keys = supplies[8].split()
    stacks = {}
    for key in keys:
        stacks[key] = []

    for i in reversed(range(8)):
        n = 4
        crates = [
            supplies[i][j:j + n].strip('[ ]')
            for j in range(0, len(supplies[i]), n)
        ]
        for crate in keys:
            if crates[int(crate) - 1] != '':
                stacks[crate].append(crates[int(crate) - 1])
    return stacks


def rearrangement_procedure():
    procedure = supplies[move].split()
    num_moves = int(procedure[1])
    from_stk = procedure[3]
    to_stk = procedure[5]
    return procedure, num_moves, from_stk, to_stk


############
# Part One
############
stacks = supply_stacks()
for move in range(10, len(supplies)):
    rearrangement, moves, from_stack, to_stack = rearrangement_procedure()

    for m in range(moves):
        stacks[to_stack].append(stacks[from_stack].pop())

final_stack = []
for stack in list(stacks.keys()):
    final_stack.append(stacks.get(stack)[-1])

print(''.join(final_stack))

############
# Part Two
############
stacks = supply_stacks()
for move in range(10, len(supplies)):
    rearrangement, moves, from_stack, to_stack = rearrangement_procedure()

    stacks[to_stack].extend(stacks[from_stack][-moves:])
    del stacks[from_stack][-moves:]

final_stack_2 = []
for stack in list(stacks.keys()):
    final_stack_2.append(stacks.get(stack)[-1])

print(''.join(final_stack_2))
