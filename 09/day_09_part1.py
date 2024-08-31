"""
Advent of Code - Day 9: Rope Bridge
"""
with open('input.txt') as input:
    motions = input.read()

motions = motions.splitlines()

###########
# Part One
###########
x_head, y_head, x_tail, y_tail = 0, 0, 0, 0
positions_head, positions_tail = {}, {}

for motion in motions:
    direction = motion.split(sep=' ')[0]
    steps = int(motion.split(sep=' ')[1])

    for step in range(steps):
        if direction == 'L':
            x_head -= 1
        elif direction == 'R':
            x_head += 1
        elif direction == 'U':
            y_head += 1
        else:
            y_head -= 1

        x_motion = x_head - x_tail
        y_motion = y_head - y_tail

        # If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction
        # If the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up
        if (abs(x_motion) > 1 or abs(y_motion) > 1):
            if x_motion != 0:
                if x_motion > 0:
                    x_tail += 1
                else:
                    x_tail -= 1
            if y_motion != 0:
                if y_motion > 0:
                    y_tail += 1
                else:
                    y_tail -= 1

        head, tail = (x_head, y_head), (x_tail, y_tail)

        if tail in positions_tail:
            positions_tail[tail] += 1
        else:
            positions_tail[tail] = 1

print(len(positions_tail.keys()))
