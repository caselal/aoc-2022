"""
Advent of Code - Day 6: Tuning Trouble
"""
with open('input.txt', 'r') as input:
    dsb = input.read()

############
# Part One
############
packet_characters_processed = 0
i = 0
while len(set(dsb[i:i + 4])) < 4:
    i += 1
packet_characters_processed += i + 4

print(packet_characters_processed)

############
# Part Two
############
message_characters_processed = 0
i = 0
while len(set(dsb[i:i + 14])) < 14:
    i += 1
message_characters_processed += i + 14

print(message_characters_processed)
