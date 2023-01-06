"""
Advent of Code - Day 10: Cathode-Ray Tube
"""
with open('input.txt') as input:
    program = input.read()

program = program.splitlines()

###########
# Part One
###########

X = 1
cycle = 0
V = []
register = []

for line in program:
    register.append(X)

    if line == 'noop':
        instruction = line
        V.append(0)
    else:
        instruction = line.split(sep=' ')[0]
        V.append(int(line.split(sep=' ')[1]))

    if instruction == 'addx':
        register.append(X)
        X += V[cycle]

    cycle += 1

sum_signal_strengths = 0
signal_strengths = [20, 60, 100, 140, 180, 220]
for signal in signal_strengths:
    sum_signal_strengths += signal * register[signal - 1]

print(sum_signal_strengths)

###########
# Part Two
###########
