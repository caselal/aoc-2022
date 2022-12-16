"""
Advent of Code - Day 2: Rock Paper Scissors
"""

# load text file
with open('input.txt', 'r') as input:
    rounds = input.read()

rounds = rounds.splitlines()
'''
Part One
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
'''

total_score = 0

dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

for round in rounds:

    opponent_hand = round.split(' ')[0]
    my_hand = round.split(' ')[1]

    if (opponent_hand == 'A' and my_hand == 'X') or (
            opponent_hand == 'B' and my_hand == 'Y') or (opponent_hand == 'C'
                                                         and my_hand == 'Z'):
        total_score += (dict.get(my_hand) + 3)

    elif (opponent_hand == 'A'
          and my_hand == 'Y') or (opponent_hand == 'B'
                                  and my_hand == 'Z') or (opponent_hand == 'C'
                                                          and my_hand == 'X'):
        total_score += (dict.get(my_hand) + 6)
    else:
        total_score += (dict.get(my_hand) + 0)

print(total_score)
'''
Part Two
X means you need to lose,
Y means you need to end the round in a draw,
Z means you need to win
'''
new_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
new_total_score = 0

for round in rounds:
    opponent_hand = round.split(' ')[0]
    round_result = round.split(' ')[1]

    if round_result == 'Y':
        my_hand = opponent_hand
        new_total_score += (dict.get(my_hand) + 3)

    elif round_result == 'Z':
        if opponent_hand == 'A':
            my_hand = 'B'
        elif opponent_hand == 'B':
            my_hand = 'C'
        else:
            my_hand = 'A'
        new_total_score += (dict.get(my_hand) + 6)

    else:
        if opponent_hand == 'A':
            my_hand = 'C'
        elif opponent_hand == 'B':
            my_hand = 'A'
        else:
            my_hand = 'B'
        new_total_score += (dict.get(my_hand) + 0)

print(new_total_score)
