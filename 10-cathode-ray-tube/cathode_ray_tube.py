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
        V.append(0)
    else:
        V.append(int(line.split(sep=' ')[1]))
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
screen = ''
screen_width = 40
screen_height = 6
for row in range(screen_height):
    for i in range(screen_width):
        sprite_position = range(register[row * screen_width + i] - 1,
                                register[row * screen_width + i] + 2)

        if i in sprite_position:
            pixel = '#'
        else:
            pixel = '.'
        screen = ''.join([screen, pixel])

for row in range(screen_height):
    print(screen[row * screen_width:(row + 1) * screen_width])
