"""
Advent of Code - Day 9: Rope Bridge
"""
with open('input.txt') as input:
    motions = input.read()

motions = motions.splitlines()

###########
# Part Two
###########
x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
positions_tail = {}
knots = range(10)

for motion in motions:
    direction = motion.split(sep=' ')[0]
    steps = int(motion.split(sep=' ')[1])

    for step in range(steps):
        for knot in knots:
            if knot == 0:
                if direction == 'L':
                    x[knot] -= 1
                elif direction == 'R':
                    x[knot] += 1
                elif direction == 'U':
                    y[knot] += 1
                else:
                    y[knot] -= 1

            else:
                x_motion = x[knot - 1] - x[knot]
                y_motion = y[knot - 1] - y[knot]
                if (abs(x_motion) > 1 or abs(y_motion) > 1):
                    if x_motion != 0:
                        if x_motion > 0:
                            x[knot] += 1
                        else:
                            x[knot] -= 1
                    if y_motion != 0:
                        if y_motion > 0:
                            y[knot] += 1
                        else:
                            y[knot] -= 1

                tail = (x[knot], y[knot])

                if knot == 9:
                    if tail in positions_tail:
                        positions_tail[tail] += 1
                    else:
                        positions_tail[tail] = 1

print(len(positions_tail.keys()))
